import os
import pygame
from enums.Menu import Menu
from Utils import Utils

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

            arriere_plan = pygame.image.load(partie.carte.arriere_plan)
            self.fenetre.blit(arriere_plan, (0, 0))

            for etudiant in partie.etudiants:
                img_etudiant = pygame.image.load(os.path.join("resources", "img", "etudiant.png"))
                self.fenetre.blit(img_etudiant, (etudiant.coords[0] - 20, etudiant.coords[1] - 20))

            pygame.display.update()
            print("update")
            Utils.update_ticks(Utils)
