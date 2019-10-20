import os

class Etudiant:
    """Classe Etudiant : Ennemis du jeu."""

    def __init__(self, coords, partie, tier):
        """Constructeur classe Etudiant

        :param coords: Coordonnées initiales de l'etudiant [x,y].
        :param partie: Partie à laquelle appartient l'etudiant
        """
        self.coords = coords
        self.point_passage = 0
        self.partie = partie
        self.sprite = os.path.join("ressources", "img", "etudiant1.png")
        self.vie_max = 100 * (1+ partie.vague/20)
        self.vitesse = 1
        self.recompense = 5 * (1+ partie.vague/20)

        if tier == 2:
            self.sprite = os.path.join("ressources", "img", "etudiant2.png")
            self.vie_max = self.vie_max * 1.5 * (1+ partie.vague/10)
            self.vitesse = self.vitesse * 1.2
            self.recompense = self.recompense * 1.2 * (1+ partie.vague/10)
        elif tier == 3:
            os.path.join("ressources", "img", "etudiant3.png")
            self.vie_max = self.vie_max * 1.8 * (1+ partie.vague/10)
            self.vitesse = self.vitesse * 1.5
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


            dx = max(-1, min(1, dir_x))
            dy = max(-1, min(1, dir_y))

            self.coords = [self.coords[0] + dx*self.vitesse, self.coords[1] + dy*self.vitesse]


    def degats(self, vie):
        """Procedure qui fait dimunuer la vie de l'Etudiants (et c'est cruel)"""

        self.vie -= vie
        if self.vie < 0:
            self.partie.retirer_etudiant(self)
            self.partie.argent += self.recompense
