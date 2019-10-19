import pygame
from enums.Menu import Menu

#Constantes
ECRAN_X = 1080
ECRAN_Y = 720
ECRAN_IPS = 60

class Affichage:
    """Classe Affichage : Gestion de l'affichage de la fenetre."""

    def __init__(self):
        """Constructeur classe Affichage
        :param fenetre: Fenetre pygame que l'on va actualiser."""
        #Attributs
        self.menu = Menu.AUCUN
        self.fenetre = pygame.display.set_mode((ECRAN_X, ECRAN_Y))

        pygame.font.init()
        self.police = pygame.font.SysFont('DejaVu Sans', 20)

        pygame.display.set_caption("Univ Defender")


    def get_ips(self):
        """Fonction qui retourne la frequence d'affichage."""
        return ECRAN_IPS



    def rafraichir_ecran(self, partie):
        """Procedure : Rafraichit l'ecran (menus / jeu ...)"""

        if self.menu == Menu.AUCUN:
            afficher_partie(self, partie)
        if self.menu == Menu.PAUSE:
            afficher_menu(self)

        pygame.display.update()


def afficher_menu(self):
    """Procedure : Affiche les differents menus"""
    menu = self.menu

    if menu == Menu.PAUSE:
        titre_menu = self.police.render("PAUSE", True, (0, 0, 0))
        self.fenetre.blit(titre_menu, (500, 300))


def afficher_partie(self, partie):
    """Procedure : Affiche tous les elements de la partie."""

    #Actualisation arriere-plan
    arriere_plan = pygame.image.load(partie.carte.arriere_plan)
    self.fenetre.blit(arriere_plan, (0, 0))


    #Actualisation etudiants
    for etudiant in partie.etudiants:
        img_etudiant = pygame.image.load(etudiant.sprite)
        self.fenetre.blit(img_etudiant, (etudiant.coords[0] - 20, etudiant.coords[1] - 20))

        #Affichage vie
        pygame.draw.rect(self.fenetre, (231, 76, 60), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, 20, 5))   #Rouge
        pygame.draw.rect(self.fenetre, (46, 204, 113), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, (etudiant.vie / etudiant.vie_max)*20, 5))   #Vert


    #Actualisation enseignants
    for enseignant in partie.enseignants:
        img_enseignant = pygame.image.load(enseignant.sprite)
        self.fenetre.blit(img_enseignant, (enseignant.coords[0] - 20, enseignant.coords[1] - 20))

        #Affichage portée
        pygame.draw.circle(self.fenetre, (127, 127, 255), enseignant.coords, enseignant.portee, 1)


    #Affichage varibles (argent, vies...)
    texte_vies = self.police.render("❤ " + str(partie.vie), True, (0, 0, 0))
    self.fenetre.blit(texte_vies, (980, 10))

    texte_argent = self.police.render("✮ " + str(int(partie.argent)), True, (0, 0, 0))
    self.fenetre.blit(texte_argent, (980, 30))