# -*- coding: utf-8 -*-
# Module pour l'importation de la base de donnée
from Controleur_bdd_json import recherche_bdd_position
from Controleur_bdd_json import initialisation_bdd_joueur
from Controleur_valeur_menu import ctrl_valeur_sexe


class Joueur:
    def __init__(self,
                 nom="",
                 prenom="",
                 naissance="",
                 sexe="",
                 classement=0,
                 position=0):
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
        self.naissance = self.generate_naissance()
        self.sexe = self.generate_sexe()
        self.classement = self.generate_classement()
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
        reponse_utilisateur = input(f"{self.prenom} {self.nom} est-ce un Homme, une Femme ou Indeterminée ?"
                                    f"(Saisir H, F ou I) : ")
        reponse = ctrl_valeur_sexe(reponse_utilisateur)
        self.sexe = reponse
        return self.sexe

    # Méthode pour demander à l'utilisateur le classement du joueur (controle avec une autre méthode)
    # Renvoie le classement saisie par l'utilisateur
    def generate_classement(self):
        self.classement = input("Merci de saisir le classement de " + self.prenom + " " + self.nom + " : ")
        controle_reponse = False
        while controle_reponse is False:
            controle_reponse = self.controle_reponse_classement()
        return self.classement

    # Méthode pour trouver un numéro de position non utilisé dans la base de donnée json
    # Renvoie le premier numéro de position non utilisé
    def generate_position(self):
        bdd_joueur = initialisation_bdd_joueur()
        self.position = recherche_bdd_position(bdd_joueur)
        return self.position

    # Méthode pour ajouter un joueur dans la base de donnée json
    # Ne renvoi rien, mais rajoute l'utilisateur à la base de donnée json
    def ajout_joueur_bdd(self):
        bdd_joueur = initialisation_bdd_joueur()
        bdd_joueur.insert({"nom": self.nom,
                           "prenom": self.prenom,
                           "naissance": self.naissance,
                           "sexe": self.sexe,
                           "classement": self.classement,
                           "position": self.position})

    # Méthode pour controler que la réponse de l'utilisateur est bien conforme (entier positif)
    # Renvoi True ou False après le controle
    def controle_reponse_classement(self):
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
        except (ValueError):
            self.classement = input("Merci de rentrer un nombre entier positif : ")
            controle_reponse = False
            return controle_reponse
