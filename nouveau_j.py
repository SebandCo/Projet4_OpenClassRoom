# -*- coding: utf-8 -*-
class joueur:
    def __init__ (self):
        self.nom = input("Merci de saisir le nom du joueur : ")
        self.prenom = input("Merci de saisir le prénom du joueur : ")
        self.naissance = input("Merci de saisir la date de naissance de " + self.prenom + " " + self.nom + " : ")
        self.sexe = input(self.prenom + " " + self.nom + " est-ce un Homme, une Femme ou Indeterminée ? (Saisir H, F ou I) : ")
        test_sexe = 0
        while test_sexe == 0:
            if self.sexe in {"H", "F", "I"}:
                test_sexe = 1
            else:
                self.sexe = input("Merci de saisir H, F ou I : ")
        self.classement = input("Merci de saisir le classement de " + self.prenom + " " + self.nom + " : ")
        