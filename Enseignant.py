"""Module Enseignant (Tours)"""

import os
import pygame

from enums.Matiere import Matiere

class Enseignant:
    """Classe Enseignant : Defenses."""


    def __init__(self, coords, partie, tier, matiere):
        """Constructeur classe Enseignant

        :param coords: Coordonnées de l'enseignant [x,y].
        :param partie: Partie à laquelle appartient l'enseignant
        :param tier: Entier representant le eniveau de l'enseignant
        :param matiere: Matiere de l'enseignant
        """
        self.coords = coords
        self.partie = partie
        self.dernier_tir = 0
        self.sprite = os.path.join("ressources", "img", "enseignant.png")
        self.tier = tier
        self.matiere = matiere

        self.afficher_tirs = True

        enseignantutils = EnseignantUtils()
        if matiere == Matiere.HISTOIRE:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = enseignantutils.get_portee(matiere)
            self.cadence = enseignantutils.get_cadence(matiere)
            self.degats = enseignantutils.get_degat(matiere)
            self.sprite = os.path.join("ressources", "img", "enseignant_histoire.png")
        elif matiere == Matiere.MATHS:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = enseignantutils.get_portee(matiere)
            self.cadence = enseignantutils.get_cadence(matiere)
            self.degats = enseignantutils.get_degat(matiere)
            self.sprite = os.path.join("ressources", "img", "enseignant_math.png")
        elif matiere == Matiere.INFO:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = enseignantutils.get_portee(matiere)
            self.cadence = enseignantutils.get_cadence(matiere)
            self.degats = enseignantutils.get_degat(matiere)
            self.sprite = os.path.join("ressources", "img", "enseignant_info.png")
        elif matiere == Matiere.SPORT:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = enseignantutils.get_portee(matiere)
            self.cadence = enseignantutils.get_cadence(matiere)
            self.degats = enseignantutils.get_degat(matiere)
            self.sprite = os.path.join("ressources", "img", "enseignant_sport.png")


    def tirer(self):
        """Procedure : Fait tirer la tour sur une cible"""

        cible = cible_ideale(self, self.partie.etudiants)
        if cible is not None:
            mtn = pygame.time.get_ticks()                           #
            if mtn - self.dernier_tir >= self.cadence * 1000:       #Delai entre les tirs
                self.dernier_tir = mtn                              #
                cible.degats(self.matiere, self.degats)

                if self.afficher_tirs:
                    pygame.draw.line(self.partie.get_affichage().fenetre, (255, 0, 0), (self.coords[0], self.coords[1]), (cible.coords[0], cible.coords[1]))
                    #self.partie.get_affichage().tir(self.coords[0], self.coords[1], cible.coords[0], cible.coords[1])


    def evoluer(self):
        """Procedure : Augmente le tier de l'enseignant."""
        self.tier += 1
        self.prix *= int(self.tier * 0.5)
        matiere = self.matiere
        if matiere == Matiere.HISTOIRE:
            self.portee += int(5)
            self.cadence -= int(0.05)
            self.degats += int(5)
        elif matiere == Matiere.MATHS:
            self.portee += int(self.tier *5)
            self.cadence -= int(0.05)
            self.degats += int(10)
        elif matiere == Matiere.INFO:
            self.portee += int(5)
            self.cadence -= int(self.tier * 0.05)
            self.degats += int(5)
        elif matiere == Matiere.SPORT:
            self.portee += int(10)
            self.degats += int(10)
    #Fonction pour l'affichage des caractéristiques du prochain tier   
    def get_prix_evol(self):
        """Fonction qui retourne le cout de l'évolution' d'un enseignant
        :return: Entier : prix."""
        prix = int(self.prix)
        prix += prix*0.5
        return prix
    
    def get_degat_evol(self):
        """Fonction qui retourne les degats après l'évolution' d'un enseignant 
        :return: Entier : degats."""
        degats= int(self.degats)
        if self.matiere == Matiere.HISTOIRE:
            degats += 5
        elif self.matiere == Matiere.MATHS:
            degats += 10
        elif self.matiere == Matiere.INFO:
            self.degats += 5
        elif self.matiere == Matiere.SPORT:
            degats += 10
        return degats
    
    def get_porte_evol(self):
        """Fonction qui retourne la portée après l'évolution' d'un enseignant 
        :return: Entier : portee."""
        portee= int(self.portee)
        return portee
        
            
    
class EnseignantUtils:
    """Classe EnseignantUtils : Fonctions utiles."""

    def get_prix(self, matiere):
        """Fonction qui retourne le prix d'un enseignant en fonction de sa matiere.
        :param enums.Matiere: Matiere
        :return: Entier : Prix."""
        prix = -1
        if matiere == Matiere.HISTOIRE:
            prix = 50
        elif matiere == Matiere.MATHS:
            prix = 100
        elif matiere == Matiere.INFO:
            prix = 75
        elif matiere == Matiere.SPORT:
            prix = 80
        return prix
    
    def get_cadence(self, matiere):
        """Fonction qui retourne la cadence de tir d'un enseignant en fonction de sa matiere.
        :param enums.Matiere: Matiere
        :return: Entier : Cadence."""
        cadence = -1
        if matiere == Matiere.HISTOIRE:
            cadence = 1.0
        elif matiere == Matiere.MATHS:
            cadence = 0.9
        elif matiere == Matiere.INFO:
            cadence = 0.5
        elif matiere == Matiere.SPORT:
            cadence = 3.0
        return cadence
    
    def get_degat(self, matiere):
        """Fonction qui retourne les degats d'un enseignant en fonction de sa matiere.
        :param enums.Matiere: Matiere
        :return: Entier : degat."""
        degat = -1
        if matiere == Matiere.HISTOIRE:
            degat = 20
        elif matiere == Matiere.MATHS:
            degat = 25
        elif matiere == Matiere.INFO:
            degat = 5
        elif matiere == Matiere.SPORT:
            degat = 50
        return degat
    
    def get_portee(self, matiere):
        """Fonction qui retourne la portée d'un enseignant en fonction de sa matiere.
        :param enums.Matiere: Matiere
        :return: Entier : portee."""
        portee = -1
        if matiere == Matiere.HISTOIRE:
            portee = 150
        elif matiere == Matiere.MATHS:
            portee = 160
        elif matiere == Matiere.INFO:
            portee = 100
        elif matiere == Matiere.SPORT:
            portee = 200
        return portee


def cible_ideale(enseignant, cibles):
    """Fonction qui retourne l'etudiant a attaquer en fonction de sa distance avec la tour et la ligne d'arrivée

    :param enseignant: Enseignant referant
    :param cibles: Liste d'Etudiants

    :return: Etudiant
    """

    resultat = None

    if len(cibles) != 0:


        i = 0
        trouvee = False

        while not trouvee and i < len(cibles):
            cible = cibles[i]
            distance = ((cible.coords[0] - enseignant.coords[0])**2 + (cible.coords[1] - enseignant.coords[1])**2)**0.5
            if distance < enseignant.portee:
                trouvee = True
                resultat = cible
            else:
                i += 1

    return resultat
