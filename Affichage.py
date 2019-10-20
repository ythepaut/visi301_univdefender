"""Module Affichage"""

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
        pygame.display.set_caption("Univ Defender")


    def get_ips(self):
        """Fonction qui retourne la frequence d'affichage.
        :return: int
        """
        return ECRAN_IPS

    def get_ecran_x(self):
        """Fonction qui retourne la largeur de l'ecran.
        :return: int
        """
        return ECRAN_X

    def get_ecran_y(self):
        """Fonction qui retourne la hauteur de l'ecran.
        :return: int
        """
        return ECRAN_Y


    def rafraichir_ecran(self, partie):
        """Procedure : Rafraichit l'ecran (menus / jeu ...)"""

        if self.menu == Menu.AUCUN:
            afficher_partie(self, partie)
        if self.menu == Menu.PAUSE:
            afficher_menu(self, partie)

        pygame.display.update()


def afficher_menu(self, partie):
    """Procedure : Affiche les differents menus"""
    menu = self.menu

    afficher_partie(self, partie)
    ombre = pygame.Surface((ECRAN_X, ECRAN_Y), pygame.SRCALPHA)
    ombre.fill((0, 0, 0, 100))
    self.fenetre.blit(ombre, (0, 0))

    if menu == Menu.PAUSE:
        #Cadre
        ombre = pygame.Surface((500, 300), pygame.SRCALPHA)
        ombre.fill((0, 0, 0, 128))
        self.fenetre.blit(ombre, (ECRAN_X // 2 - 250, ECRAN_Y // 2 - 150))

        #Titre
        titre_menu = creer_police(taille=30, gras=True).render("PAUSE", True, (255, 255, 255))
        self.fenetre.blit(titre_menu, (ECRAN_X  // 2 - titre_menu.get_width() // 2, 250 - titre_menu.get_height() // 2))

        #Boutons
        bouton_reprendre = pygame.Surface((400, 50), pygame.SRCALPHA)
        bouton_reprendre.fill((46, 204, 113, 255))
        self.fenetre.blit(bouton_reprendre, (ECRAN_X // 2 - 200, 325 - 25))
        btntxt_reprendre = creer_police(taille=18, gras=True).render("REPRENDRE LA PARTIE", True, (255, 255, 255))
        self.fenetre.blit(btntxt_reprendre, (ECRAN_X // 2 - 200 + 200 - btntxt_reprendre.get_width() // 2, 336 - btntxt_reprendre.get_height()))



def afficher_partie(self, partie):
    """Procedure : Affiche tous les elements de la partie."""

    #Actualisation arriere-plan
    arriere_plan = pygame.image.load(partie.carte.arriere_plan)
    self.fenetre.blit(arriere_plan, (0, 0))


    #Actualisation etudiants
    for etudiant in partie.etudiants:
        no_sprite = (pygame.time.get_ticks() // 300) % len(etudiant.sprite)
        img_etudiant = pygame.image.load(etudiant.sprite[no_sprite])
        self.fenetre.blit(img_etudiant, (etudiant.coords[0] - 20, etudiant.coords[1] - 20))

        #Affichage vie
        pygame.draw.rect(self.fenetre, (231, 76, 60), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, 20, 3))   #Rouge
        pygame.draw.rect(self.fenetre, (46, 204, 113), (etudiant.coords[0] - 10, etudiant.coords[1] - 30, (etudiant.vie / etudiant.vie_max)*20, 3))   #Vert


    #Actualisation enseignants
    for enseignant in partie.enseignants:
        img_enseignant = pygame.image.load(enseignant.sprite)
        self.fenetre.blit(img_enseignant, (enseignant.coords[0] - 20, enseignant.coords[1] - 20))

        #Affichage portée
        pygame.draw.circle(self.fenetre, (127, 127, 255), enseignant.coords, enseignant.portee, 1)


    #Affichage varibles (argent, vies...)
    texte_vies = creer_police().render("❤ " + str(partie.vie), True, (0, 0, 0))
    self.fenetre.blit(texte_vies, (980, 10))

    texte_argent = creer_police().render("✮ " + str(int(partie.argent)), True, (0, 0, 0))
    self.fenetre.blit(texte_argent, (980, 30))





def creer_police(police="DejaVu Sans", taille=20, gras=False, italique=False):
    """Fonction qui retourne une police

    :param police: String Nom de la police à utiliser
    :param taille: int Taille de la police
    :param gras: bool (opt) Police en gras
    :param italique: bool (opt) Police en italique

    :return: Police pygame"""

    resultat = pygame.font.SysFont(police, taille)
    resultat.set_bold(gras)
    resultat.set_italic(italique)
    return resultat
