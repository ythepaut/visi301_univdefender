"""Module Principal"""

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
carte = Carte([[80, 200], [840, 200], [840, 480], [70, 480]], [[130, 130], [190, 130], [250, 130], [310, 130], [370, 130], [430, 130], [490, 130], [550, 130], [610, 130], [670, 130], [730, 130], [790, 130], [850, 130], [910, 130], [130, 270], [190, 270], [250, 270], [310, 270], [370, 270], [430, 270], [490, 270], [550, 270], [610, 270], [770, 270], [910, 190], [910, 250], [910, 310], [910, 370], [910, 430], [910, 490], [910, 550], [850, 550], [790, 550], [730, 550], [670, 550], [610, 550], [550, 550], [490, 550], [430, 550], [370, 550], [310, 550], [250, 550], [190, 550], [130, 550], [130, 410], [190, 410], [250, 410], [310, 410], [370, 410], [430, 410], [490, 410], [550, 410], [610, 410], [770, 410]], os.path.join("ressources", "img", "carte1.png"))
partie = Partie(carte, affichage)


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

    continuer = execution

    for evenement in evenements:

        #Quitter le jeu
        if evenement.type == pygame.QUIT or (evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE):
            continuer = False
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
                    emplacement = carte.emplacement_le_plus_proche((x, y))
                    if emplacement is not None:
                        if not carte.est_emplacement_utilise(emplacement):
                            enseignant = Enseignant(emplacement, partie)
                            carte.utiliser_emplacement(emplacement)
                            partie.ajouter_enseignant(enseignant)
                            partie.argent -= 50
                            affichage.afficher_message("Enseignant ajouté.", 2)
                        else:
                            affichage.afficher_message("Emplacement deja utilisé", 2)
                    else:
                        affichage.afficher_message("Veuillez cliquer sur un emplacement valide", 2)
                else:
                    affichage.afficher_message("Vous n'avez pas assez d'argent pour placer cet enseignant !", 2)

            elif affichage.menu == Menu.PAUSE:
                #Reprendre la partie
                if x > (affichage.get_ecran_x() // 2 - 200) and x < (affichage.get_ecran_x() // 2 + 200) and y > 300 and y < 350:
                    affichage.menu = Menu.AUCUN

            elif affichage.menu == Menu.PERDU:
                #Recommencer la partie
                if x > (affichage.get_ecran_x() // 2 - 200) and x < (affichage.get_ecran_x() // 2 + 200) and y > 300 and y < 350:
                    affichage.__init__()
                    carte.__init__(carte.chemin, carte.emplacements, carte.arriere_plan)
                    partie.__init__(carte, affichage)
                    affichage.menu = Menu.AUCUN

    return continuer


#Boucle principale
while execution:

    clock.tick(affichage.get_ips())  #Frequence d'affichage ecran

    if affichage.menu == Menu.AUCUN:
        partie.rafraichir()
    affichage.rafraichir_ecran(partie)

    execution = ecoute_evenements(pygame.event.get())

pygame.quit()
