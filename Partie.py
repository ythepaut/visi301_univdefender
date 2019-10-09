from enums.Statut import Statut
import pygame

from Etudiant import Etudiant
from Utils import Utils

class Partie:
    """Classe Partie : Gestion de la partie."""


    def __init__(self, carte):
        """Constructeur classe Partie
        :param carte: Carte sur laquelle la partie se joue."""
        #Attributs
        self.carte = carte
        self.etudiants = []
        self.statut = Statut.ENTRE_VAGUE
        self.timer = 10
        self.vague = 0


    def ajouter_etudiant(self, etudiant):
        """Procedure : Ajouter un etudiant dans la partie
        :param etudiant: Etudiant à ajouter."""
        self.etudiants += [etudiant]
        print("etu")

    def retirer_etudiant(self, etudiant):
        """Procedure : Retirer un etudiant de la partie
        :param etudiant: Etudiant à retirer."""
        self.etudiants.remove(etudiant)
        del etudiant



    def rafraichir(self):
        """Procedure : Fait avancer le jeu (Temps entre-vague, faire avancer les etudiant, faire tirer les profs...)"""

        if len(self.etudiants) > 0:

            for etudiant in self.etudiants:
                etudiant.avancer()


        else:

            if self.statut == Statut.VAGUE: #Fin de vague
                self.statut = Statut.ENTRE_VAGUE
                self.timer = 10
                print("Fin de la vague.")
            elif self.statut == Statut.ENTRE_VAGUE and self.timer > 0:
                self.timer -= 1
                print("Nouvelle vague dans ", self.timer)

                ticks = Utils.ticks
                while Utils.sleep(Utils, 1000, ticks):
                    Utils.update_ticks(Utils)

            elif self.statut == Statut.ENTRE_VAGUE and self.timer <= 0:
                self.statut = Statut.VAGUE
                print("Nouvelle vague !")

                nouvelle_vague(self)


def nouvelle_vague(self):
    """Procedure qui lance une nouvelle vague d'ennemis"""

    self.vague += 1

    effectifs = vague_etudiant(self.vague)
    
    for i in range(0, effectifs[0]): #Apparition etudiants 1 standart
        etudiant = Etudiant(self.carte.chemin[0], self)
        self.ajouter_etudiant(etudiant)

        ticks = Utils.ticks
        while Utils.sleep(Utils, 500, ticks):
            Utils.update_ticks(Utils)

    for i in range(0, effectifs[0]): #Apparition etudiants 2 moyen TODO
        etudiant = Etudiant(self.carte.chemin[0], self)
        self.ajouter_etudiant(etudiant)

        ticks = Utils.ticks
        while Utils.sleep(Utils, 500, ticks):
            Utils.update_ticks(Utils)


    for i in range(0, effectifs[0]): #Apparition etudiants 1 fort TODO
        etudiant = Etudiant(self.carte.chemin[0], self)
        self.ajouter_etudiant(etudiant)

        ticks = Utils.ticks
        while Utils.sleep(Utils, 500, ticks):
            Utils.update_ticks(Utils)


def vague_etudiant(vague):
    """Fonction qui retourne le nombre d'etudiant a faire apparaitre dans la prochaine vague.
    :param vague: Entier : Numero de vague.
    :return: Tableau d'entiers : Nombre d'etudiants par type."""

    #5v mod 20  etudiant standart
    #v - 1      etudiant moyen
    #v div 20   etudiant fort
    resultat = [(vague * 5) % 20, vague - 1, vague // 20]

    return resultat