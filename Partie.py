import pygame

from enums.Statut import Statut
from Etudiant import Etudiant

class Partie():
    """Classe Partie : Gestion de la partie."""


    def __init__(self, carte):
        """Constructeur classe Partie
        :param carte: Carte sur laquelle la partie se joue."""
        #Attributs
        self.execution = True
        self.carte = carte
        self.etudiants = []
        self.enseignants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 10
        self.vague = 0
        self.dernier_seconde = pygame.time.get_ticks()
        self.file_attente_vague = []
        self.vie = 10


    def ajouter_etudiant(self, etudiant):
        """Procedure : Ajouter un etudiant dans la partie
        :param etudiant: Etudiant à ajouter."""
        self.etudiants += [etudiant]

    def retirer_etudiant(self, etudiant):
        """Procedure : Retirer un etudiant de la partie
        :param etudiant: Etudiant à retirer."""
        self.etudiants.remove(etudiant)
        del etudiant


    def ajouter_enseignant(self, enseignant):
        """Procedure : Ajouter un enseignant dans la partie
        :param enseignant: Enseignant à ajouter."""
        self.enseignants += [enseignant]

    def retirer_enseignant(self, enseignant):
        """Procedure : Retirer un enseignant de la partie
        :param enseignant: Enseignant à retirer."""
        self.enseignants.remove(enseignant)
        del enseignant



    def rafraichir(self):
        """Procedure : Fait avancer le jeu (Temps entre-vague, faire avancer les etudiant, faire tirer les profs...)"""

        #Apparition des etudiants dans la vague
        if (len(self.file_attente_vague) > 0 and self.file_attente_vague[0][0] <= pygame.time.get_ticks()):
            self.ajouter_etudiant(self.file_attente_vague[0][1])
            self.file_attente_vague.pop(0)

        #Faire tirer les enseignants
        if len(self.enseignants) > 0:
            
            for enseignant in self.enseignants:
                enseignant.tirer()

        #Faire avancer les etudiants
        if len(self.etudiants) > 0:

            for etudiant in self.etudiants:
                etudiant.avancer()

        #Gestion transition vague car plus d'etudiants
        else:

            if self.statut == Statut.VAGUE: #Fin de vague
                self.statut = Statut.ENTRE_VAGUE
                self.timer = 10
                print("Fin de la vague.")

            elif self.statut == Statut.ENTRE_VAGUE and self.timer > 0:

                mtn = pygame.time.get_ticks()               #
                if mtn - self.dernier_seconde >= 1000:      #Delai entre vague
                    self.dernier_seconde = mtn              #

                    print("Nouvelle vague dans ", self.timer)
                    self.timer -= 1


            elif self.statut == Statut.ENTRE_VAGUE and self.timer <= 0:
                self.statut = Statut.VAGUE
                self.vague += 1
                print("Nouvelle vague !")

                effectifs = effectifs_vague(self.vague)

                for i in range(0, effectifs[0]):

                    etudiant = Etudiant(self.carte.chemin[0], self)
                    self.file_attente_vague += [(pygame.time.get_ticks() + 500*i, etudiant)]


    def perdre_vie(self):
        """Procedure qui fait perdre une vie au joueur et le notifie."""
        if self.vie == 0:
            self.execution = False
            print("Fin de la partie ! Vous n'avez plus de vies")
        else:
            self.vie -= 1
            print("Vous avez perdu une vie ! Il vous en reste ", self.vie)


def effectifs_vague(vague):
    """Fonction qui retourne le nombre d'etudiant a faire apparaitre dans la prochaine vague.
    :param vague: Entier : Numero de vague.
    :return: Tableau d'entiers : Nombre d'etudiants par type."""

    resultat = [(vague * 5) % 20, vague - 1, vague // 20]
    return resultat
