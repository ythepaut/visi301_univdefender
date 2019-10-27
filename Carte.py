"""Module Carte"""

class Carte:
    """Classe Carte : Definit un niveau."""

    def __init__(self, chemin, emplacements, arriere_plan):
        """Constructeur classe Carte

        :param chemin: Liste des coordonnées des points de passage.
        :param emplacements: Liste des coordonnées des points d'apparition des tours.
        :param arriere_plan: Chemin d'acces de l'image d'arriere plan.
        """

        #Attributs
        self.chemin = chemin
        self.emplacements = emplacements
        self.arriere_plan = arriere_plan

        #Dico des emplacements utilisés
        self.dico_emplacements = {}
        for i in range(len(self.emplacements)):
            self.dico_emplacements[i] = False


    def est_emplacement_utilise(self, coords):
        """Fonction qui retourne si un emplacement d'enseignant est utilisé ou non.

        :param coords: Coordonnées du point d'apparition.

        :return: booleen vrai si utilisé.
        """

        resultat = True

        for i in range(len(self.emplacements)):
            if self.emplacements[i] == coords:
                resultat = self.dico_emplacements[i]

        return resultat

    def utiliser_emplacement(self, coords):
        """Procedure qui modifie le statut de l'emplacement.
        :param coords: Coordonnées de l'emplacement à utiliser.
        """

        for i in range(len(self.emplacements)):
            if self.emplacements[i] == coords:
                self.dico_emplacements[i] = True

    def emplacement_le_plus_proche(self, coords):
        """Fonction qui retourne les coordonnées de l'emplacement le plus proche à moins de 30px.

        :param coords: Coordonnées de reference

        :return: Coordonnées de l'emplacement ou None si aucun emplacement disponible.
        """

        resultat = self.emplacements[0]
        meilleur_distance = int(distance(coords, self.emplacements[0]))

        for emplacement in self.emplacements:
            distance_courante = distance(emplacement, coords)
            if distance_courante < meilleur_distance:
                meilleur_distance = distance_courante
                resultat = emplacement

        if distance(resultat, coords) >= 30:
            resultat = None

        return resultat


def distance(a, b):
    """Fonction qui retourne la distance entre deux points

    :param a: Point a (x_a, y_a)
    :param b: Point b (x_b, y_b)

    :return: float
    """
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
