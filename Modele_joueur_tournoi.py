from Modele_joueur import *

class JoueurTournoi(Joueur):
    def __init__(self,
                couleur = "",
                paires = "",
                points = "",
                ordre = ""):
        self.couleur = couleur
        self.paires = paires
        self.points = points
        self.ordre = ordre