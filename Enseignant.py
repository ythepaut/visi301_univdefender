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
            self.portee = 120
            self.cadance = 1
            self.degats = 40
            self.sprite = os.path.join("ressources", "img", "enseignant.png")
        elif matiere == Matiere.MATHS:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 180
            self.cadance = 0.9
            self.degats = 25
            self.sprite = os.path.join("ressources", "img", "enseignant_math.png")
        elif matiere == Matiere.INFO:
            self.prix = enseignantutils.get_prix(matiere)
            self.portee = 200
            self.cadance = 1.3
            self.degats = 35
            self.sprite = os.path.join("ressources", "img", "enseignant_info.png")


    def tirer(self):
        """Procedure : Fait tirer la tour sur une cible"""

        cible = cible_ideale(self, self.partie.etudiants)
        if cible is not None:
            mtn = pygame.time.get_ticks()                           #
            if mtn - self.dernier_tir >= self.cadance * 1000:       #Delai entre les tirs
                self.dernier_tir = mtn                              #
                cible.degats(self.matiere, self.degats)


    def evoluer(self):
        """Procedure : Augmente le tier de l'enseignant."""
        self.tier += 1
        self.prix *= int(self.tier * 0.5)
        self.portee *= int(self.tier * 0.5)
        self.cadance -= int(self.tier * 0.1)
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
