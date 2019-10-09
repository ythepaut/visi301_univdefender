from enums.Statut import Statut
import pygame

from Etudiant import Etudiant

class Partie:
    """Classe Partie : Gestion de la partie."""


    def __init__(self, carte):
        """Constructeur classe Partie
        :param carte: Carte sur laquelle la partie se joue."""
        #Attributs
        self.carte = carte
        self.etudiants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 10


    def ajouterEtudiant(self, etudiant):
        """Procedure : Ajouter un etudiant dans la partie
        :param etudiant: Etudiant à ajouter."""
        self.etudiants += [etudiant]

    def retirerEtudiant(self, etudiant):
        """Procedure : Retirer un etudiant de la partie
        :param etudiant: Etudiant à retirer."""
        self.etudiants.remove(etudiant)
        del etudiant



    def rafraichir(self):
        """Procedure : Fait avancer le jeu (Temps entre-vague, faire avancer les etudiant, faire tirer les profs...)"""

        if len(self.etudiants) > 0:

            for etudiant in self.etudiants:
                etudiant.avancer()

            pygame.time.delay(10)

        else:

            if self.statut == Statut.VAGUE: #Fin de vague
                self.statut = Statut.ENTRE_VAGUE
                self.timer = 10
                print("Fin de la vague.")
            elif self.statut == Statut.ENTRE_VAGUE and self.timer > 0:
                self.timer -= 1
                print("Nouvelle vague dans ", self.timer)
                pygame.time.delay(1000)
            elif self.statut == Statut.ENTRE_VAGUE and self.timer <= 0:
                self.statut = Statut.VAGUE

                etudiant = Etudiant(self.carte.chemin[0], self)
                self.ajouterEtudiant(etudiant)

                print("Nouvelle vague !")
