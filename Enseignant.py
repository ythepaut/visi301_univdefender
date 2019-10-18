class Enseignant:
    """Classe Enseignant : Defenses."""


    def __init__(self, coords, partie):
        """Constructeur classe Enseignant
        :param coords: Coordonnées de l'enseignant [x,y].
        :param partie: Partie à laquelle appartient l'enseignant"""
        self.coords = coords
        self.partie = partie


    def tirer(self):
        """Procedure : Fait tirer la tour sur une cible"""
        #cible = cible_ideale(self.partie.etudiants)
        #print(cible)



    def cible_ideale(self, cibles):

        if len(cibles) != 0:

            resultat = cibles[0]
            distance = ((resultat.coords[0] - self.coords[0])**2 + (resultat.coords[1] - self.coords[1])**2)**0.5

            for cible in cibles:
                resultat = cible

        return resultat