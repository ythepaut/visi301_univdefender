import os
import pygame
from enums.Menu import Menu

class Affichage:
    """Classe Affichage : Gestion de l'affichage de la fenetre."""

    def __init__(self, fenetre):
        """Constructeur classe Affichage
        :param fenetre: Fenetre pygame que l'on va actualiser."""
        #Attributs
        self.menu = Menu.AUCUN
        self.fenetre = fenetre

        pygame.display.set_caption("Univ Defender")


    def rafraichir_ecran(self, partie):
        """Procedure qui affiche l'ensemble des elements de la fenetre (arriere plan, etudiants, profs)."""
        if self.menu == Menu.AUCUN:

            #Actualisation arriere-plan
            arriere_plan = pygame.image.load(partie.carte.arriere_plan)
            self.fenetre.blit(arriere_plan, (0, 0))

            #Actualisation etudiants
            for etudiant in partie.etudiants:
                img_etudiant = pygame.image.load(os.path.join("ressources", "img", "etudiant.png"))
                self.fenetre.blit(img_etudiant, (etudiant.coords[0] - 20, etudiant.coords[1] - 20))

            #Actualisation enseignants
            for enseignant in partie.enseignants:
                img_enseignant = pygame.image.load(os.path.join("ressources", "img", "enseignant.png"))
                self.fenetre.blit(img_enseignant, (enseignant.coords[0], enseignant.coords[1]))

            pygame.display.update()
            print("MAJ Affichage")
