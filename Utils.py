import pygame

class Utils:
    """Classe Utils : Contient plusieurs fonction utiles..."""

    def __init__(self):
        pass

    ticks = 0

    def update_ticks(self):
        self.ticks += 10
        pygame.time.delay(10)

    def sleep(self, delai, tick_init):
        """Fonction qui retourne si doit attendre pour executer une prochaine action.
        :param delai: Entier : Nombre de ms a attendre.
        :param tick_init: Entier : Nombre de ticks au debut de l'attente.
        :return: booleen."""
        
        return tick_init + delai > self.ticks
