# -*- coding: utf-8 -*-
# Module pour l'importation de la base de donnée
from tinydb import TinyDB, where

class Joueur:
    def __init__(self, nom="", prenom="", naissance="", sexe="", classement=0, position=0):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.sexe = sexe
        self.classement = classement
        self.position = position

    # Méthode pour compiler l'ensemble des étapes de création d'un joueur
    # Renvoi un objet joueur crée
    def creation_joueur(self):
        self.nom = self.generate_nom()
        self.prenom = self.generate_prenom()
        self.naissance = self.generate_naissance(self.nom, self.prenom)
        self.sexe = self.generate_sexe(self.nom, self.prenom)
        self.classement = self.generate_classement(self.nom, self.prenom)
        self.position = self.generate_position()

    # Méthode pour demander à l'utilisateur le nom du joueur
    # Renvoie le nom saisie par l'utilisateur
    def generate_nom(self):
        self.nom = input("Merci de saisir le nom du joueur : ")
        return self.nom
    
    # Méthode pour demander à l'utilisateur le prénom du joueur
    # Renvoie le prenom saisie par l'utilisateur
    def generate_prenom(self):
        self.prenom = input("Merci de saisir le prénom du joueur : ")
        return self.prenom

    # Méthode pour demander à l'utilisateur la date de naissance du joueur (pas de controle)
    # Renvoie la date de naissance saisie par l'utilisateur
    def generate_naissance(self):
        self.naissance = input("Merci de saisir la date de naissance de " + self.prenom + " " + self.nom + " : ")
        return self.naissance

    # Méthode pour demander à l'utilisateur le genre du joueur (controle avec une autre méthode)
    # Renvoie le genre saisie par l'utilisateur
    def generate_sexe(self):
        self.sexe = input(self.prenom + " " + self.nom + " est-ce un Homme, une Femme ou Indeterminée ? (Saisir H, F ou I) : ")
        controle_reponse = False
        while controle_reponse == False:
            controle_reponse = self.controle_reponse_sexe(self.sexe)
        return self.sexe
    
    # Méthode pour demander à l'utilisateur le classement du joueur (controle avec une autre méthode)
    # Renvoie le classement saisie par l'utilisateur
    def generate_classement(self, nom, prenom):
        self.classement = input("Merci de saisir le classement de " + self.prenom + " " + self.nom + " : ")
        controle_reponse = False
        while controle_reponse == False:
            controle_reponse = self.controle_reponse_classement(self.classement)
        return self.classement
    
    # Méthode qui donne un numéro unique au joueur (controle avec une autre méthode)
    # Renvoi un numéro unique suivant la base json (invisible pour l'utilisateur)
    def generate_position(self):
        self.position = self.recherche_position_joueur_bdd()
        return self.position  

    # Méthode pour trouver un numéro de position non utilisé dans la base de donnée json
    # Renvoie le premier numéro de position non utilisé
    def recherche_position_joueur_bdd(self, position=0):
        joueurs_bdd = TinyDB("joueurs_bdd.json")
        joueur_aj = joueurs_bdd.table("joueur_aj")
        joueur_existant = True
        # Tant qu'il y a un joueur à la position sélectionnée, on itére la boucle
        while joueur_existant == True:
            position += 1
            joueur_trouve=joueur_aj.search(where("position") == position)
            # Si la chaine de caractère trouvé est vide, c'est que la place est libre
            if len(joueur_trouve) == 0:
                joueur_existant = False
                position
                return position

    # Méthode pour ajouter un joueur dans la base de donnée json
    # Ne renvoi rien, mais rajoute l'utilisateur à la base de donnée json
    def ajout_joueur_bdd(self, nom, prenom, naissance, sexe, classement, position):
        joueurs_bdd = TinyDB("joueurs_bdd.json")
        joueur_aj = joueurs_bdd.table("joueur_aj")
        joueur_aj.insert({"nom": self.nom,
                          "prenom": self.prenom,
                          "naissance": self.naissance,
                          "sexe": self.sexe,
                          "classement": self.classement,
                          "position": self.position})

    # Méthode pour controler que la réponse de l'utilisateur est bien conforme (H, F ou I)
    # Renvoi True ou False après le controle
    def controle_reponse_sexe(self, sexe):
        # Si la réponse utilisateur est H, F ou I
        if self.sexe in {"H", "F", "I"}:
            controle_reponse = True
            return controle_reponse
        # Si la réponse utilisateur est différente de H, F ou I
        else:
            self.sexe = input("Merci de saisir H, F ou I : ")
            controle_reponse = False
            return controle_reponse

    # Méthode pour controler que la réponse de l'utilisateur est bien conforme (entier positif)
    # Renvoi True ou False après le controle
    def controle_reponse_classement(self, classement):
        # Si la réponse utilisateur est un nombre
        try:
            # Met le string en integer
            self.classement = int(self.classement)
            # Si la réponse utilisateur est positive ou nul
            if 0 > self.classement:
                self.classement = input("Merci de rentrer un nombre entier positif : ")
                controle_reponse = False
                return controle_reponse
            # Si la réponse utlisateur est négative
            else:
                controle_reponse = True
                return controle_reponse
        # Si la réponse utilisateur n'est pas un nombre
        except:
            self.classement = input("Merci de rentrer un nombre entier positif : ")
            controle_reponse = False
            return controle_reponse