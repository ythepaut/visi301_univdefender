"""Module Partie"""

import pygame
import random

from enums.Statut import Statut
from enums.Menu import Menu
from enums.Matiere import Matiere
from enums.Filiere import Filiere
from Etudiant import Etudiant

class Partie():
    """Classe Partie : Gestion de la partie."""


    def __init__(self, carte, affichage):
        """Constructeur classe Partie
        :param carte: Carte sur laquelle la partie se joue.
        :param affichage: Classe qui gere l'affichage de la partie actuelle."""
        #Attributs
        self.carte = carte
        self.affichage = affichage
        self.etudiants = []
        self.enseignants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 5
        self.vague = 0
        self.dernier_seconde = pygame.time.get_ticks()
        self.file_attente_vague = []
        self.dernier_apparition = 0
        self.vie = 10
        self.argent = 10000
        self.matiere_courante = Matiere.HISTOIRE


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

    def get_enseignant(self, coords):
        """Fonction qui retourne un enseignant aux coordonnées.
        :param coords: Coordonnées de l'enseignant recherché.
        :return: Enseignant."""
        resultat = None
        for enseignant in self.enseignants:
            if enseignant.coords == coords:
                resultat = enseignant
        return resultat



    def rafraichir(self):
        """Procedure : Fait avancer le jeu (Temps entre-vague, faire avancer les etudiant, faire tirer les profs...)"""

        #Apparition des etudiants dans la vague
        if (len(self.file_attente_vague) > 0 and self.file_attente_vague[0][0] <= pygame.time.get_ticks()):

            mtn = pygame.time.get_ticks()               #
            if mtn - self.dernier_apparition >= 500:    #Delai entre les apparitions
                self.dernier_apparition = mtn           #

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
        elif len(self.file_attente_vague) == 0:

            if self.statut == Statut.VAGUE: #Fin de vague
                self.statut = Statut.ENTRE_VAGUE
                self.timer = 5
                self.argent += 25 + 10*(self.vague)**0.5
                self.affichage.afficher_message("Fin de la vague.", 3)

            elif self.statut == Statut.ENTRE_VAGUE and self.timer > 0:

                mtn = pygame.time.get_ticks()               #
                if mtn - self.dernier_seconde >= 1000:      #Delai entre vague
                    self.dernier_seconde = mtn              #

                    self.affichage.afficher_message("Nouvelle vague dans " + str(self.timer), 1)
                    self.timer -= 1


            elif self.statut == Statut.ENTRE_VAGUE and self.timer <= 0:
                self.statut = Statut.VAGUE
                self.vague += 1
                self.affichage.afficher_message("Nouvelle vague ! (" + str(self.vague) + ")", 3)

                effectifs = effectifs_vague(self.vague)

                for i in range(len(effectifs)-1, -1, -1):
                    for j in range(0, effectifs[i]):
                        etudiant = Etudiant(self.carte.chemin[0], self, i+1, random.choice(list(Filiere)))
                        self.file_attente_vague += [(pygame.time.get_ticks() + 500*j, etudiant)]


    def perdre_vie(self):
        """Procedure qui fait perdre une vie au joueur et le notifie."""
        if self.vie == 0:
            self.affichage.menu = Menu.PERDU
            self.affichage.afficher_message("Fin de la partie ! Vous n'avez plus de vies", 10)
        else:
            self.vie -= 1
            self.affichage.afficher_message("Vous avez perdu une vie ! Il vous en reste " + str(self.vie), 3)


def effectifs_vague(vague):
    """Fonction qui retourne le nombre d'etudiant a faire apparaitre dans la prochaine vague.

    :param vague: Entier : Numero de vague.

    :return: Tableau d'entiers : Nombre d'etudiants par type.
    """

    resultat = [(vague * 3) % 15, (vague - 1) % 20, vague // 5]
    return resultat
