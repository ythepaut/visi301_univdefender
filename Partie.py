from enums.Statut import Statut
import pygame

from Etudiant import Etudiant

class Partie:


    def __init__(self, carte):
        #Attributs
        self.carte = carte
        self.etudiants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 10


    def ajouterEtudiant(self, etudiant):
        self.etudiants += [etudiant]

    def retirerEtudiant(self, etudiant):
        self.etudiants.remove(etudiant)
        del etudiant



    def rafraichir(self):

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
