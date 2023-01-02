# -*- coding: utf-8 -*-
#Module pour l'importation de la base de donnée
from tinydb import TinyDB, Query
from pprint import pprint

class joueur:
    def __init__ (self):
        # Succession de question auprès de l'utilisateur pour l'implementation du nouveau joueur
        self.nom = input("Merci de saisir le nom du joueur : ")
        self.prenom = input("Merci de saisir le prénom du joueur : ")
        self.naissance = input("Merci de saisir la date de naissance de " + self.prenom + " " + self.nom + " : ")
        self.sexe = input(self.prenom + " " + self.nom + " est-ce un Homme, une Femme ou Indeterminée ? (Saisir H, F ou I) : ")
        # Vérification pour savoir si l'utilisateur à mis H, F ou I et rien d'autre
        test_sexe = 0
        while test_sexe == 0:
            if self.sexe in {"H", "F", "I"}:
                #Si réponse correct on passe à la suite
                test_sexe = 1
            else:
                #Si réponse différente alors demande de précision
                self.sexe = input("Merci de saisir H, F ou I : ")
        self.classement = input("Merci de saisir le classement de " + self.prenom + " " + self.nom + " : ")
        # Vérification pour savoir si le nombre rentré est un entier positif
        test_classement = 0
        while test_classement == 0:
            try:
                # Vérifie si le classement est un entier
                int(self.classement) 
                self.classement=int(self.classement)# Met le string en integer
                # Vérifie que self.classement est positif
                if 0 <= self.classement:
                    test_classement=1 # Valide le controle pour sortir de la boucle
                else:
                    # Si reponse_menu n'est pas compris entre 1 et 4
                    self.classement=input("Merci de rentrer un nombre entier positif : ")
            except:
                # Si reponse_menu n'est pas un entier
                self.classement=input("Merci de rentrer un nombre entier positif : """)
        
        
    def rajout_joueur_bdd (self):
        #Implémentation de la base de donnée suivant les valeurs de l'initialisation
        joueurs_bdd = TinyDB("joueurs_bdd.json")
        joueur_aj = joueurs_bdd.table("joueur_aj")
        joueur_aj.insert({"nom" : self.nom, 
                       "prenom" : self.prenom,
                       "naissance" : self.naissance,
                       "sexe" : self.sexe,
                       "classement" : self.classement})

