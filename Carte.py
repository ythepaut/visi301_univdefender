"""Module Carte"""

class Carte:
    """Classe Carte : Definit un niveau."""

    def __init__(self, chemin, arriere_plan):
        """Constructeur classe Carte

        :param chemin: Liste des coordonnées des points de passage.
        :param arriere_plan: Chemin d'acces de l'image d'arriere plan.
        """

        #Attributs
        self.chemin = chemin
        self.arriere_plan = arriere_plan
