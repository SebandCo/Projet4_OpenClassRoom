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
        self.point = self.generate_points(points)
        self.ordre = ordre

    def generate_points(self,points):
        if points == "":
            inverse_classement = (10**(len(str(self.classement)))-self.classement)
            nombre_division = (len(str(self.classement))*2)
            self.points = inverse_classement / (10**nombre_division)
        else:
            self.points = points       
        return