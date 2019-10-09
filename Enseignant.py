class Enseignant:
    """Classe Enseignant : Defenses."""


    def __init__(self, coords, partie):
        """Constructeur classe Enseignant
        :param coords: Coordonnées de l'enseignant [x,y].
        :param partie: Partie à laquelle appartient l'enseignant"""
        self.coords = coords
        self.partie = partie
