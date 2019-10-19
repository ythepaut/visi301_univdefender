import pygame

class Enseignant:
    """Classe Enseignant : Defenses."""


    def __init__(self, coords, partie):
        """Constructeur classe Enseignant
        :param coords: Coordonnées de l'enseignant [x,y].
        :param partie: Partie à laquelle appartient l'enseignant"""
        self.coords = coords
        self.partie = partie
        self.portee = 100
        self.cadance = 0.7
        self.dernier_tir = 0


    def tirer(self):
        """Procedure : Fait tirer la tour sur une cible"""

        mtn = pygame.time.get_ticks()                           #
        if mtn - self.dernier_tir >= self.cadance * 1000:       #Delai entre les tirs
            self.dernier_tir = mtn                              #

            cible = cible_ideale(self, self.partie.etudiants)
            if cible != None:
                cible.degats(35)




def cible_ideale(enseignant, cibles):
    """Fonction qui retourne l'etudiant a attaquer en fonction de sa distance avec la tour et la ligne d'arrivée
    :param enseignant: Enseignant referant
    :param cibles: Liste d'Etudiants
    :return: Etudiant"""

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
