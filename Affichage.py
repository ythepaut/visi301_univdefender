"""Module Affichage"""

import os
import pygame
from enums.Menu import Menu
from enums.Matiere import Matiere
from Enseignant import EnseignantUtils

#Constantes
ECRAN_X = 1080
ECRAN_Y = 720
ECRAN_IPS = 60

class Affichage:
    """Classe Affichage : Gestion de l'affichage de la fenetre."""

    def __init__(self):
        """Constructeur classe Affichage"""

        #Attributs
        self.menu = Menu.AUCUN
        self.fenetre = pygame.display.set_mode((ECRAN_X, ECRAN_Y))

        self.msg = ["", 0]  #Message titre à afficher en haut de l'ecran [String Titre, int nb_tick_expiration]
        
        self.ECRAN_IPS = ECRAN_IPS

        pygame.font.init()
        pygame.display.set_caption("Univ Defender")


    def get_ips(self):
        """Fonction qui retourne la frequence d'affichage.
        :return: int
        """
        return self.ECRAN_IPS

    def set_ips(self, ips):
        """Fonction qui modifie la frequence d'affichage.
        :param ips: int
        """
        self.ECRAN_IPS = ips

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
        """Procedure : Rafraichit l'ecran (menus / jeu ...)
        :param partie: Partie par rapport à laquelle on fait l'affichage.
        """

        if self.menu == Menu.AUCUN:
            afficher_partie(self, partie)
        else:
            afficher_menu(self, partie)

        pygame.display.update()

    def afficher_message(self, message, temps):
        """Procudure : Affiche une message en haut de l'ecran.
        :param message: Chaîne de caractères à afficher.
        :param temps: Entier representant la durée d'affichage du message.
        """
        self.msg = [message, pygame.time.get_ticks() + temps*ECRAN_IPS*17]


    def tir(x_1, y_1, x_2, y_2):
        """Procedure : Affiche un trait qui symbolise le tir d'un enseignant
        :param x_1: X origine
        :param y_1: Y origine
        :param x_2: X arrivée
        :param y_2: Y arrivée"""
        pygame.draw.line(self.fenetre, (255, 0, 0), (x_1, y_1), (x_2, y_2))


def afficher_menu(self, partie):
    """Procedure : Affiche les differents menus"""
    menu = self.menu

    afficher_partie(self, partie)
    ombre = pygame.Surface((ECRAN_X, ECRAN_Y), pygame.SRCALPHA)
    ombre.fill((0, 0, 0, 100))
    self.fenetre.blit(ombre, (0, 0))

    if menu == Menu.PAUSE:
        #Cadre
        ombre = pygame.Surface((500, 350), pygame.SRCALPHA)
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
        
        bouton_cartes = pygame.Surface((400, 50), pygame.SRCALPHA)
        bouton_cartes.fill((46, 204, 113, 255))
        self.fenetre.blit(bouton_cartes, (ECRAN_X // 2 - 200, 390 - 25))
        btntxt_reprendre = creer_police(taille=18, gras=True).render("CHANGER DE CARTE", True, (255, 255, 255))
        self.fenetre.blit(btntxt_reprendre, (ECRAN_X // 2 - 200 + 200 - btntxt_reprendre.get_width() // 2, 401 - btntxt_reprendre.get_height()))
        
        #Infos
        info_touche = creer_police(taille=18).render("Clic Gauche : Placer un enseignant", True, (255, 255, 255))
        self.fenetre.blit(info_touche, (ECRAN_X  // 2 - info_touche.get_width() // 2, 455 - info_touche.get_height() // 2))
        info_touche = creer_police(taille=18).render("Clic Droit : Retirer un enseignant", True, (255, 255, 255))
        self.fenetre.blit(info_touche, (ECRAN_X  // 2 - info_touche.get_width() // 2, 480 - info_touche.get_height() // 2))
        info_touche = creer_police(taille=18).render("Molette : Changer d'enseignant", True, (255, 255, 255))
        self.fenetre.blit(info_touche, (ECRAN_X  // 2 - info_touche.get_width() // 2, 505 - info_touche.get_height() // 2))
        info_touche = creer_police(taille=18).render("M : Couper la musique", True, (255, 255, 255))
        self.fenetre.blit(info_touche, (ECRAN_X  // 2 - info_touche.get_width() // 2, 530 - info_touche.get_height() // 2))

    elif menu == Menu.PRINCIPAL:
        #Cadre
        ombre = pygame.Surface((700, 300), pygame.SRCALPHA)
        ombre.fill((0, 0, 0, 128))
        self.fenetre.blit(ombre, (ECRAN_X // 2 - 350, ECRAN_Y // 2 - 150))

        #Titre
        titre_menu = creer_police(taille=30, gras=True).render("SELECTIONNER LA CARTE", True, (255, 255, 255))
        self.fenetre.blit(titre_menu, (ECRAN_X  // 2 - titre_menu.get_width() // 2, 250 - titre_menu.get_height() // 2))

        #Cartes
        carte1 = pygame.image.load(os.path.join("ressources", "img", "miniature_carte1.png"))
        self.fenetre.blit(carte1, (260, 300))
        carte1 = pygame.image.load(os.path.join("ressources", "img", "miniature_carte2.png"))
        self.fenetre.blit(carte1, (570, 300))


    elif menu == Menu.PERDU:
        #Cadre
        ombre = pygame.Surface((500, 300), pygame.SRCALPHA)
        ombre.fill((0, 0, 0, 128))
        self.fenetre.blit(ombre, (ECRAN_X // 2 - 250, ECRAN_Y // 2 - 150))

        #Titre
        titre_menu = creer_police(taille=30, gras=True).render("VOUS AVEZ PERDU :(", True, (255, 255, 255))
        self.fenetre.blit(titre_menu, (ECRAN_X  // 2 - titre_menu.get_width() // 2, 250 - titre_menu.get_height() // 2))

        #Boutons
        bouton_reprendre = pygame.Surface((400, 50), pygame.SRCALPHA)
        bouton_reprendre.fill((46, 204, 113, 255))
        self.fenetre.blit(bouton_reprendre, (ECRAN_X // 2 - 200, 325 - 25))
        btntxt_reprendre = creer_police(taille=18, gras=True).render("REFAIRE UNE PARTIE", True, (255, 255, 255))
        self.fenetre.blit(btntxt_reprendre, (ECRAN_X // 2 - 200 + 200 - btntxt_reprendre.get_width() // 2, 336 - btntxt_reprendre.get_height()))
        
        bouton_cartes = pygame.Surface((400, 50), pygame.SRCALPHA)
        bouton_cartes.fill((46, 204, 113, 255))
        self.fenetre.blit(bouton_cartes, (ECRAN_X // 2 - 200, 390 - 25))
        btntxt_reprendre = creer_police(taille=18, gras=True).render("CHANGER DE CARTE", True, (255, 255, 255))
        self.fenetre.blit(btntxt_reprendre, (ECRAN_X // 2 - 200 + 200 - btntxt_reprendre.get_width() // 2, 401 - btntxt_reprendre.get_height()))




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

        #Affichage filiere
        texte_filiere = creer_police(taille=10).render(str(etudiant.filiere.name).upper(), True, (0, 0, 0))
        self.fenetre.blit(texte_filiere, (etudiant.coords[0] - texte_filiere.get_width() // 2 - 2, etudiant.coords[1] + 25))

    #Actualisation enseignants
    for enseignant in partie.enseignants:
        img_enseignant = pygame.image.load(enseignant.sprite)
        self.fenetre.blit(img_enseignant, (enseignant.coords[0] - 20, enseignant.coords[1] - 20))

        #Affichage si curseur sur l'enseignant
        curseur_x, curseur_y = pygame.mouse.get_pos()
        if ((enseignant.coords[0]-curseur_x)**2 + (enseignant.coords[1]-curseur_y)**2)**0.5 < 20:
            #Portée
            pygame.draw.circle(self.fenetre, (127, 127, 255), enseignant.coords, enseignant.portee, 1)
            #Matiere
            texte_matiere = creer_police(taille=10).render(str(enseignant.matiere.name).capitalize() + "  Niv. " + str(enseignant.tier), True, (0, 0, 0))
            self.fenetre.blit(texte_matiere, (enseignant.coords[0] - texte_matiere.get_width() // 2 - 2, enseignant.coords[1] + 25))


    #Affichage varibles (argent, vies...)
    texte_vies = creer_police().render("❤ " + str(partie.vie), True, (0, 0, 0))
    self.fenetre.blit(texte_vies, (980, 10))

    texte_argent = creer_police().render("✮ " + str(int(partie.argent)), True, (0, 0, 0))
    self.fenetre.blit(texte_argent, (980, 30))


    #Affichage Matiere courante
    sprite = os.path.join("ressources", "img", "enseignant.png")
    if partie.matiere_courante == Matiere.HISTOIRE:
        sprite = os.path.join("ressources", "img", "enseignant_histoire.png")
    elif partie.matiere_courante == Matiere.MATHS:
        sprite = os.path.join("ressources", "img", "enseignant_math.png")
    elif partie.matiere_courante == Matiere.INFO:
        sprite = os.path.join("ressources", "img", "enseignant_info.png")
    img_enseignant_courant = pygame.image.load(sprite)
    self.fenetre.blit(img_enseignant_courant, (1000, 670))
    txt_enseignant_courant = creer_police(taille=12).render(partie.matiere_courante.name, True, (0, 0, 0))
    self.fenetre.blit(txt_enseignant_courant, (1020 - txt_enseignant_courant.get_width() // 2, 650))
    txt_selection = creer_police(taille=16).render("Tour Actuelle", True, (0, 0, 0))
    self.fenetre.blit(txt_selection, (1020 - txt_selection.get_width() // 2, 630))


    #Affichage caracteristiques tour
    curseur_x, curseur_y = pygame.mouse.get_pos()
    if ((1020-curseur_x)**2 + (690-curseur_y)**2)**0.5 < 40:

        enseignantutils = EnseignantUtils()
        cout = enseignantutils.get_prix(partie.matiere_courante)

        if partie.matiere_courante == Matiere.HISTOIRE:
            point_fort = "-"
            point_faible = "-"
        elif partie.matiere_courante == Matiere.INFO:
            point_fort = "MPC"
            point_faible = "MIST"
        elif partie.matiere_courante == Matiere.MATHS:
            point_fort = "MIST"
            point_faible = "MPC"
        elif partie.matiere_courante == Matiere.SPORT:
            point_fort = "MIST/MPC"
            point_faible = "STAPS"
        else:
            point_fort = "-"
            point_faible = "-"

        #Affichage Faible et cout
        txt_description = creer_police(taille=12).render("Fort contre : " + point_fort, True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 650))
        txt_description = creer_police(taille=12).render("Faible contre : " + point_faible, True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 670))
        txt_description = creer_police(taille=12).render("Coût : " + str(cout), True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 690))
    #Affichage caractéristique tour
    else :
        enseignantutils = EnseignantUtils()
        if partie.matiere_courante == Matiere.HISTOIRE:
            portee = enseignantutils.get_portee(partie.matiere_courante)
            degat = enseignantutils.get_degat(partie.matiere_courante)
            cadence = enseignantutils.get_cadence(partie.matiere_courante)
        elif partie.matiere_courante == Matiere.INFO:
            portee = enseignantutils.get_portee(partie.matiere_courante)
            degat = enseignantutils.get_degat(partie.matiere_courante)
            cadence = enseignantutils.get_cadence(partie.matiere_courante)
        elif partie.matiere_courante == Matiere.MATHS:
            portee = enseignantutils.get_portee(partie.matiere_courante)
            degat = enseignantutils.get_degat(partie.matiere_courante)
            cadence = enseignantutils.get_cadence(partie.matiere_courante)
        elif partie.matiere_courante == Matiere.SPORT:
            portee = enseignantutils.get_portee(partie.matiere_courante)
            degat = enseignantutils.get_degat(partie.matiere_courante)
            cadence = enseignantutils.get_cadence(partie.matiere_courante)
        
        
        txt_description = creer_police(taille=12).render("Portée : " + str(portee), True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 650))
        txt_description = creer_police(taille=12).render("Dégats : " + str(degat), True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 670))
        txt_description = creer_police(taille=12).render("Temp entre les tirs : " + str(cadence) +" s", True, (0, 0, 0))
        self.fenetre.blit(txt_description, (900 - txt_description.get_width() // 2, 690))
        

    #Affichage message titre
    if self.msg[0] != "":
        if self.msg[1] < pygame.time.get_ticks():
            self.msg[0] = ""
        else:
            texte_msg = creer_police().render(self.msg[0], True, (0, 0, 0))
            self.fenetre.blit(texte_msg, (ECRAN_X  // 2 - texte_msg.get_width() // 2, 10))




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
