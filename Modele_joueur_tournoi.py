from Modele_joueur import *

class JoueurTournoi(Joueur):
    def __init__(self,
                joueur_base,
                couleur = "",
                paires = "",
                points = "",
                ordre = ""):
        Joueur.__init__(self,
                        joueur_base.nom,
                        joueur_base.prenom,
                        joueur_base.naissance,
                        joueur_base.sexe,
                        joueur_base.classement,
                        joueur_base.position)
        self.couleur = couleur
        self.paires = paires
        self.points = points
        self.ordre = ordre