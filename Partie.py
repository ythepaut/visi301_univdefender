import pygame

from enums.Statut import Statut
from Etudiant import Etudiant

class Partie:
    """Classe Partie : Gestion de la partie."""


    def __init__(self, carte):
        """Constructeur classe Partie
        :param carte: Carte sur laquelle la partie se joue."""
        #Attributs
        self.carte = carte
        self.etudiants = []
        self.enseignants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 10
        self.vague = 0
        self.dernier_seconde = pygame.time.get_ticks()


    def ajouter_etudiant(self, etudiant):
        """Procedure : Ajouter un etudiant dans la partie
        :param etudiant: Etudiant à ajouter."""
        self.etudiants += [etudiant]
        print("AJOUT Etudiant")

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

        if len(self.etudiants) > 0:

            for etudiant in self.etudiants:
                etudiant.avancer()

        else:

            if self.statut == Statut.VAGUE: #Fin de vague
                self.statut = Statut.ENTRE_VAGUE
                self.timer = 10
                print("Fin de la vague.")
            elif self.statut == Statut.ENTRE_VAGUE and self.timer > 0:

                mtn = pygame.time.get_ticks()               #
                if mtn - self.dernier_seconde >= 1000:      #Delai entre vague
                    self.dernier_seconde = mtn              #

                    self.timer -= 1
                    print("Nouvelle vague dans ", self.timer)


            elif self.statut == Statut.ENTRE_VAGUE and self.timer <= 0:
                self.statut = Statut.VAGUE
                print("Nouvelle vague !")

                nouvelle_vague(self)


def nouvelle_vague(self):
    """Procedure qui lance une nouvelle vague d'ennemis"""

    self.vague += 1

    effectifs = vague_etudiant(self.vague)

    for _ in range(0, effectifs[0]): #Apparition etudiants 1 standart
        etudiant = Etudiant(self.carte.chemin[0], self)
        self.ajouter_etudiant(etudiant)

        test(pygame.time.get_ticks() + 1000)
        #TODO AJOUTER ATTENTE ENTRE CHAQUE APPARITION

    #TODO GESTION DES AUTRES ETUDIANTS


def vague_etudiant(vague):
    """Fonction qui retourne le nombre d'etudiant a faire apparaitre dans la prochaine vague.
    :param vague: Entier : Numero de vague.
    :return: Tableau d'entiers : Nombre d'etudiants par type."""

    #5v mod 20  etudiant standart
    #v - 1      etudiant moyen
    #v div 20   etudiant fort
    resultat = [(vague * 5) % 20, vague - 1, vague // 20]

    return resultat

def test(delai):
    while pygame.time.get_ticks() < delai:
        pass
    print("test")
