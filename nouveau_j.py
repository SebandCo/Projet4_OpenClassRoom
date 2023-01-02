# -*- coding: utf-8 -*-
#Module pour l'importation de la base de donnée
from tinydb import TinyDB, where
from pprint import pprint
from recherche_j import *

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
        test_classement1 = False
        while test_classement1 == False:
            try:
                # Vérifie si le classement est un entier
                int(self.classement) 
                self.classement=int(self.classement)# Met le string en integer
                # Vérifie que self.classement est positif
                if 0 > self.classement:
                    self.classement=input("Merci de rentrer un nombre entier positif : ")
                else:
                    test_classement1 = True
                    # Si self.classement n'est pas positif
            except:
                # Si self.classement n'est pas un entier
                self.classement=input("Merci de rentrer un nombre entier positif : """)
        
        # Vérification pour savoir si un joueur avec le même classement existe
        joueur_existant = recherche_joueur(self.classement)
        
        #Si joueur_existant est vide alors il n'y a pas de doublon
        if len(joueur_existant) == 0:
            return
        #Sinon joueur_existant n'est pas vide, il y a donc un doublon
        else:             
            print("Un joueur existe déjà avec le classement", self.classement,". Voulez vous le remplacer ?")
            #On demande à l'utilisateur quoi faire
            reponse_classement=input("Si oui, saisir ""O"". Sinon saisir ""N"" et recommencer : ")
            test_classement2 = False
            while test_classement2 == False:
                if reponse_classement == "O":
                    #Si l'utilisateur valide, le programme continue et remplace le joueur existant
                    self.doublon = True
                    test_classement2 = True
                elif reponse_classement == "N":
                    #Si l'utilisateur valide le programme continue mais ne rajoute pas le joueur
                    self.doublon = False
                    test_classement2 = True
                else:
                    reponse_classement=input("Merci de saisir ""O"" pour remplacer ou ""N"" pour recommencer : ")
  
    def rajout_joueur_bdd (self):
        #Implémentation de la base de donnée suivant les valeurs de l'initialisation
        joueurs_bdd = TinyDB("joueurs_bdd.json")
        joueur_aj = joueurs_bdd.table("joueur_aj")
        joueur_aj.insert({"nom" : self.nom, 
                       "prenom" : self.prenom,
                       "naissance" : self.naissance,
                       "sexe" : self.sexe,
                       "classement" : self.classement})
    
    def mise_a_jour_joueur_bdd (self):
        joueurs_bdd = TinyDB("joueurs_bdd.json")
        joueur_aj = joueurs_bdd.table("joueur_aj")
        joueur_aj.update({"nom" : self.nom, 
                       "prenom" : self.prenom,
                       "naissance" : self.naissance,
                       "sexe" : self.sexe},
                       where("classement") == self.classement)

