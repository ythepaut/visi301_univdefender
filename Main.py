####################
##  VISI301 : Projet de programmation
##  Univ Defender
##  Ewan RAKOTOANOSY - Yohann THEPAUT
####################

import os
import pygame

from Affichage import Affichage
from Carte import Carte
from Etudiant import Etudiant
from Enseignant import Enseignant
from Partie import Partie

#Constantes
ECRAN_X = 1080
ECRAN_Y = 720
ECRAN_IPS = 60

pygame.init()
fenetre = pygame.display.set_mode((ECRAN_X, ECRAN_Y))


affichage = Affichage(fenetre)
carte = Carte([[1, 130], [775, 130], [775, 490], [1, 490]], os.path.join("ressources", "img", "carte1.png"))
partie = Partie(carte)

execution = True

clock = pygame.time.Clock()

while execution:

    clock.tick(ECRAN_IPS)  #Frequence d'affichage ecran


    partie.rafraichir()
    affichage.rafraichir_ecran(partie)


    # LISTENER - Ecoute des évenements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT or (evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE):    #Quitter la partie ?
            execution = False

        if evenement.type == pygame.KEYDOWN:        #TEMP : Ajout manuel etudiant
            if evenement.key == pygame.K_e:
                etudiant = Etudiant(partie.carte.chemin[0], partie)
                partie.ajouter_etudiant(etudiant)

        if evenement.type == pygame.MOUSEBUTTONDOWN:#TEMP : Ajout manuel enseignant
            x, y = pygame.mouse.get_pos()
            enseignant = Enseignant([x, y], partie)
            partie.ajouter_enseignant(enseignant)

    execution = execution and partie.execution 

pygame.quit()
