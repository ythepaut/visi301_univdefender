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
        pygame.font.init()
        self.police = pygame.font.SysFont('DejaVu Sans', 20)

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

                #Affichage vie
                pygame.draw.rect(self.fenetre, (231, 76, 60), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, 20, 5))   #Rouge
                pygame.draw.rect(self.fenetre, (46, 204, 113), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, etudiant.vie / 5, 5))   #Vert


            #Actualisation enseignants
            for enseignant in partie.enseignants:
                img_enseignant = pygame.image.load(os.path.join("ressources", "img", "enseignant.png"))
                self.fenetre.blit(img_enseignant, (enseignant.coords[0] - 20, enseignant.coords[1] - 20))

                #Affichage portée
                pygame.draw.circle(self.fenetre, (127, 127, 255), enseignant.coords, enseignant.portee, 1)


            #Affichage varibles (argent, vies...)
            texte_vies = self.police.render(str(partie.vie) + ' ❤', True, (0, 0, 0))
            self.fenetre.blit(texte_vies, (1000, 10))
            
            texte_argent = self.police.render(str(partie.argent) + ' ✮', True, (0, 0, 0))
            self.fenetre.blit(texte_argent, (1000, 30))

            pygame.display.update()
