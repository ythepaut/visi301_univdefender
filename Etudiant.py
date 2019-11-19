"""Module Etudiant"""

import os
from enums.Filiere import Filiere
from enums.Matiere import Matiere
from enums.EvenementsAleatoires import EvenementsAleatoires

class Etudiant:
    """Classe Etudiant : Ennemis du jeu."""

    def __init__(self, coords, partie, tier, filiere):
        """Constructeur classe Etudiant

        :param coords: Coordonnées initiales de l'etudiant [x,y].
        :param partie: Partie à laquelle appartient l'etudiant
        :param tier: Entier representant le niveau de l'etudiant.
        :param filiere: (Enum) Filire de l'etudiant.
        """
        self.coords = coords
        self.point_passage = 0
        self.partie = partie
        self.sprite = [os.path.join("ressources", "img", "etudiant1_1.png"), os.path.join("ressources", "img", "etudiant1_2.png")]
        self.vie_max = 100 * (1+ partie.vague/20)
        self.vitesse = 1
        self.recompense = 5 * (1+ partie.vague/50)

        self.filiere = filiere

        if tier == 2:
            self.sprite = [os.path.join("ressources", "img", "etudiant2_1.png"), os.path.join("ressources", "img", "etudiant2_2.png")]
            self.vie_max = self.vie_max * 1.6 * (1+ partie.vague/10)
            self.vitesse = self.vitesse * 1
            self.recompense = self.recompense * 1.2 * (1+ partie.vague/10)
        elif tier == 3:
            self.sprite = [os.path.join("ressources", "img", "etudiant3_1.png"), os.path.join("ressources", "img", "etudiant3_2.png")]
            self.vie_max = self.vie_max * 2 * (1+ partie.vague/10)
            self.vitesse = self.vitesse * 1.2
            self.recompense = self.recompense * 1.5 * (1+ partie.vague/10)
        self.vie = self.vie_max


    def avancer(self):
        """Procedure : Fait avancer l'etudiant sur le chemin de la carte."""

        if self.point_passage >= len(self.partie.carte.chemin) - 1: #Dernier point passage atteint ?

            self.partie.retirer_etudiant(self)
            self.partie.perdre_vie()

        else:

            prochain_point_passage = self.partie.carte.chemin[self.point_passage + 1]

            dir_x = prochain_point_passage[0] - self.coords[0]
            dir_y = prochain_point_passage[1] - self.coords[1]

            if abs(dir_x) + abs(dir_y) <= 1:    #Point de passage atteint ?
                self.point_passage += 1


            d_x = max(-1, min(1, dir_x))
            d_y = max(-1, min(1, dir_y))

            vitesse_totale = self.vitesse
            if self.partie.evenement == EvenementsAleatoires.RETOUR_VACANCES:
                vitesse_totale = self.vitesse * 1.2

            self.coords = [self.coords[0] + d_x * vitesse_totale, self.coords[1] + d_y * vitesse_totale]


    def degats(self, matiere, vie):
        """Procedure qui fait dimunuer la vie de l'Etudiants (et c'est cruel)"""

        multiplicateur = 1 #Modifie les degats en fonction de la filiere de l'etudiant et de la matiere de l'enseignant.

        if matiere == Matiere.INFO:
            if self.filiere == Filiere.MIST:
                multiplicateur = 0.3
            elif self.filiere == Filiere.MPC:
                multiplicateur = 1.3
            elif self.filiere == Filiere.STAPS:
                multiplicateur = 1.8
        elif matiere == Matiere.MATHS:
            if self.filiere == Filiere.MIST:
                multiplicateur = 1.6
            elif self.filiere == Filiere.MPC:
                multiplicateur = 0.6
            elif self.filiere == Filiere.STAPS:
                multiplicateur = 1.2

        #Gestion evenements aléatoires
        if self.partie.evenement == EvenementsAleatoires.PARTIEL:
            multiplicateur -= 0.2
        elif self.partie.evenement == EvenementsAleatoires.VENDREDI_MATIN:
            multiplicateur += 0.2


        self.vie -= int(vie * multiplicateur)

        #Etudiant décédé ?
        if self.vie < 0:
            self.partie.retirer_etudiant(self)
            self.partie.argent += self.recompense
