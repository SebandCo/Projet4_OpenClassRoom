from Modele_joueur import *

class JoueurTournoi(Joueur):
    def __init__(self,
                nom = "",
                prenom = "",
                naissance = "",
                sexe = "",
                classement = 0,
                position = 0,
                couleur = "",
                paires = "",
                points = "",
                ordre = ""):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.sexe = sexe
        self.classement = classement
        self.position = position
        self.couleur = couleur
        self.paires = paires
        self.points = points
        self.ordre = ordre