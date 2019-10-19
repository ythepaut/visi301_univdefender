####################
##  VISI301 : Projet de programmation
##  Univ Defender
##  Ewan RAKOTOANOSY - Yohann THEPAUT
####################

import os
import pygame

from Affichage import Affichage
from Carte import Carte
from Enseignant import Enseignant
from Partie import Partie
from enums.Menu import Menu


#Constantes d'affichage
ECRAN_X = 1080
ECRAN_Y = 720
ECRAN_IPS = 60

#Initialisation pygame
pygame.init()
fenetre = pygame.display.set_mode((ECRAN_X, ECRAN_Y))
clock = pygame.time.Clock()

#Creation des instances
affichage = Affichage(fenetre)
carte = Carte([[1, 130], [775, 130], [775, 490], [1, 490]], os.path.join("ressources", "img", "carte1.png"))
partie = Partie(carte)

#Musique
#pygame.mixer.music.load(os.path.join("ressources", "audio", "musique.wav"))
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(0.3)

execution = True


def ecoute_evenements(evenements):
    """Fonction qui traite les évenements et retourne si l'utilisateur veut quitter.
    :param eveenements: Liste des evenements pygame
    :return: Booleen"""

    quitter = False

    for evenement in evenements:

        #Quitter le jeu
        if evenement.type == pygame.QUIT or (evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE):
            quitter = True
        #Pause
        elif evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_p:
            if affichage.menu == Menu.PAUSE:
                affichage.menu = Menu.AUCUN
            elif affichage.menu == Menu.AUCUN:
                affichage.menu = Menu.PAUSE

        #Ajout d'un enseignant
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if affichage.menu == Menu.AUCUN:
                if partie.argent >= 50:
                    x, y = pygame.mouse.get_pos()
                    enseignant = Enseignant([x, y], partie)

                    partie.ajouter_enseignant(enseignant)
                    partie.argent -= 50
                else:
                    print("Vous n'avez pas assez d'argent pour placer cet enseignant !")
    return quitter



#Boucle principale
while execution:

    clock.tick(ECRAN_IPS)  #Frequence d'affichage ecran

    if affichage.menu == Menu.AUCUN:
        partie.rafraichir()
    affichage.rafraichir_ecran(partie)

    execution = execution and partie.execution and not ecoute_evenements(pygame.event.get())

pygame.quit()
