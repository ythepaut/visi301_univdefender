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

        enseignantutils = EnseignantUtils()
        if matiere == Matiere.HISTOIRE:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 160
            self.cadence = 1
            self.degats = 40
            self.sprite = os.path.join("ressources", "img", "enseignant_histoire.png")
        elif matiere == Matiere.MATHS:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 200
            self.cadence = 0.9
            self.degats = 25
            self.sprite = os.path.join("ressources", "img", "enseignant_math.png")
        elif matiere == Matiere.INFO:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 150
            self.cadence = 0.5
            self.degats = 10
            self.sprite = os.path.join("ressources", "img", "enseignant_info.png")
        elif matiere == Matiere.SPORT:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 300
            self.cadence = 3
            self.degats = 50
            self.sprite = os.path.join("ressources", "img", "enseignant.png")


    def tirer(self):
        """Procedure : Fait tirer la tour sur une cible"""

        cible = cible_ideale(self, self.partie.etudiants)
        if cible is not None:
            mtn = pygame.time.get_ticks()                           #
            if mtn - self.dernier_tir >= self.cadence * 1000:       #Delai entre les tirs
                self.dernier_tir = mtn                              #
                cible.degats(self.matiere, self.degats)


    def evoluer(self):
        """Procedure : Augmente le tier de l'enseignant."""
        self.tier += 1
        self.prix *= int(self.tier * 0.5)
        self.portee += int(self.tier *5)
        self.cadence -= int(self.tier * 0.05)
        self.degats += int(self.tier * 5)


class EnseignantUtils:
    """Classe EnseignantUtils : Fonctions utiles."""

    def get_prix(self, matiere):
        """Fonction qui retourne le prix d'un enseignant en fonction de sa matiere.
        :param enums.Matiere: Matiere
        :return: Entier : Prix."""
        resultat = -1
        if matiere == Matiere.HISTOIRE:
            resultat = 50
        elif matiere == Matiere.MATHS:
            resultat = 100
        elif matiere == Matiere.INFO:
            resultat = 75
        elif matiere == Matiere.SPORT:
            resultat = 80
        return resultat


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
