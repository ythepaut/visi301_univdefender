####################
##  VISI301 : Projet de programmation
##  Univ Defender
##  Ewan RAKOTOANOSY - Yohann THEPAUT
####################

import pygame

from Affichage import Affichage
from Carte import Carte
from Etudiant import Etudiant
from Partie import Partie

pygame.init()
fenetre = pygame.display.set_mode((1080, 720))

affichage = Affichage(fenetre)
carte = Carte([[1, 130], [775, 130], [775, 490], [1, 490]], "resources/img/carte1.png")
partie = Partie(carte)


execution = True

while execution:
    pygame.time.delay(5)

    partie.rafraichir()

    affichage.rafraichirEcran(partie)

    # LISTENER - Ecoute des évenements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            execution = False


    if evenement.type == pygame.KEYDOWN:        #Ajout etudiant
        if evenement.key == pygame.K_e:
            etudiant = Etudiant(partie.carte.chemin[0], partie)
            partie.ajouterEtudiant(etudiant)




pygame.quit()