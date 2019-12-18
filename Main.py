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
from Enseignant import Enseignant, EnseignantUtils
from Partie import Partie
from enums.Menu import Menu
from enums.Matiere import Matiere


#Initialisation pygame
pygame.init()
clock = pygame.time.Clock()


#Creation des instances
affichage = Affichage()
carte1 = Carte([[80, 200], [840, 200], [840, 480], [70, 480]], [[130, 130], [190, 130], [250, 130], [310, 130], [370, 130], [430, 130], [490, 130], [550, 130], [610, 130], [670, 130], [730, 130], [790, 130], [850, 130], [910, 130], [130, 270], [190, 270], [250, 270], [310, 270], [370, 270], [430, 270], [490, 270], [550, 270], [610, 270], [770, 270], [910, 190], [910, 250], [910, 310], [910, 370], [910, 430], [910, 490], [910, 550], [850, 550], [790, 550], [730, 550], [670, 550], [610, 550], [550, 550], [490, 550], [430, 550], [370, 550], [310, 550], [250, 550], [190, 550], [130, 550], [130, 410], [190, 410], [250, 410], [310, 410], [370, 410], [430, 410], [490, 410], [550, 410], [610, 410], [770, 410]], os.path.join("ressources", "img", "carte1.png")) ##Carte Niveau 1
carte2 = Carte([[285,30], [285,150],[515,150],[515,360],[675,360],[675,185],[920,185],[920,540],[630,540],[630,605],[380,605],[380,375],[220,375],[220,480], [70, 480]], [[219,153],[282,211],[437,92],[578,213],[459,349],[596,427],[738,238],[829,122],[859,328],[980,478],[861,484],[683,482],[689,601],[504,671],[436,552],[317,561],[298,432],[334,312],[161,372],[220,541]], os.path.join("ressources", "img", "carte2.png")) ##Carte Niveau 2
carte = carte2
partie = Partie(carte, affichage)

enseignantutils = EnseignantUtils()


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
                if partie.argent >= enseignantutils.get_prix(partie.matiere_courante):
                    emplacement = carte.emplacement_le_plus_proche((x, y))
                    if emplacement is not None:
                        if not carte.est_emplacement_utilise(emplacement):
                            enseignant = Enseignant(emplacement, partie, 1, partie.matiere_courante)
                            carte.utiliser_emplacement(emplacement)
                            partie.ajouter_enseignant(enseignant)
                            partie.argent -= enseignantutils.get_prix(partie.matiere_courante)
                            affichage.afficher_message("Enseignant ajouté.", 2)
                        else:
                            enseignant = partie.get_enseignant(emplacement)
                            if partie.argent >= enseignant.prix * (enseignant.tier + 1):
                                partie.argent -= enseignant.prix * (enseignant.tier + 1)
                                enseignant.evoluer()
                                affichage.afficher_message("Enseignant évolué.", 2)
                            else:
                                affichage.afficher_message("Il vous manque " + str(enseignant.prix * (enseignant.tier + 1)) + " pour améliorer.", 2)
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

        elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 3:    #Clic droit ?
            x, y = pygame.mouse.get_pos()
            if affichage.menu == Menu.AUCUN:
                #Retirer un enseignant
                emplacement = carte.emplacement_le_plus_proche((x, y))
                if carte.est_emplacement_utilise(emplacement):
                    enseignant = partie.get_enseignant(emplacement)
                    if enseignant is not None:
                        partie.retirer_enseignant(enseignant)
                        partie.argent += 25
                        affichage.afficher_message("Vous avez licencié cet enseignant.", 2)
                        carte.liberer_emplacement(emplacement)

        elif evenement.type == pygame.MOUSEBUTTONDOWN and (evenement.button == 5 or evenement.button == 4): #Changement de matiere enseignant :
            if evenement.button == 5:
                partie.matiere_courante = Matiere((partie.matiere_courante.value+1) % len(Matiere))
            else:
                partie.matiere_courante = Matiere((partie.matiere_courante.value-1) % len(Matiere))

    return continuer


#Boucle principale
while execution:

    clock.tick(affichage.get_ips())  #Frequence d'affichage ecran

    if affichage.menu == Menu.AUCUN:
        partie.rafraichir()
    affichage.rafraichir_ecran(partie)

    execution = ecoute_evenements(pygame.event.get())

pygame.quit()
