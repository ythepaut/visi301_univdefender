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

execution = True




def ecoute_evenements(evenements):
    """Fonction qui traite les évenements et retourne si l'utilisateur veut quitter.
    :param eveenements: Liste des evenements pygame
    :return: Booleen"""

    quitter = False

    for evenement in evenements:
        if evenement.type == pygame.QUIT or (evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE):    #Quitter la partie ?
            quitter = True

        if evenement.type == pygame.MOUSEBUTTONDOWN:    #TEMP : Ajout manuel enseignant
            if partie.argent >= 50:
                x, y = pygame.mouse.get_pos()
                enseignant = Enseignant([x, y], partie)
                partie.ajouter_enseignant(enseignant)
                partie.argent -= 50
            else:
                print("Vous n'avez pas assez d'argent pour placer cet enseignant !")
    return quitter



while execution:

    clock.tick(ECRAN_IPS)  #Frequence d'affichage ecran

    partie.rafraichir()
    affichage.rafraichir_ecran(partie)

    execution = execution and partie.execution and not ecoute_evenements(pygame.event.get())

pygame.quit()
