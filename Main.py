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


#Initialisation pygame
pygame.init()
clock = pygame.time.Clock()


#Creation des instances
affichage = Affichage()
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

    :return: Booleen
    """

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

        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:  #Clic gauche ?
            x, y = pygame.mouse.get_pos()

            if affichage.menu == Menu.AUCUN:
                #Ajout d'un enseignant
                if partie.argent >= 50:
                    enseignant = Enseignant([x, y], partie)

                    partie.ajouter_enseignant(enseignant)
                    partie.argent -= 50
                else:
                    print("Vous n'avez pas assez d'argent pour placer cet enseignant !")

            elif affichage.menu == Menu.PAUSE:
                #Reprendre la partie
                if x > (affichage.get_ecran_x() // 2 - 200) and x < (affichage.get_ecran_x() // 2 + 200) and y > 300 and y < 350:
                    affichage.menu = Menu.AUCUN

    return quitter


#Boucle principale
while execution:

    clock.tick(affichage.get_ips())  #Frequence d'affichage ecran

    if affichage.menu == Menu.AUCUN:
        partie.rafraichir()
    affichage.rafraichir_ecran(partie)

    execution = execution and partie.execution and not ecoute_evenements(pygame.event.get())

pygame.quit()
