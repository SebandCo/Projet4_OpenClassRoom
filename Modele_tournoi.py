# -*- coding: utf-8 -*-
# Module pour la récuperation de la date du jour
from datetime import datetime
# Module pour naviguer dans les fichiers
from Controleur_valeur_menu import *
from Vue_menu_nouveau_tournoi import *
from Controleur_bdd_json import *

class Tournoi:
    def __init__(self,
                nom = "",
                lieu = "",
                date = "",
                nbr_tour = 4,
                tour_actif = 1,
                tournee = "",
                nbr_joueur = 8,
                joueurs = "",
                ctrl_temps = "",
                description = "",
                status = "En cours"):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_tour = nbr_tour
        self.tour_actif = tour_actif
        self.tournee = tournee
        self.nbr_joueur = nbr_joueur
        self.joueurs = joueurs
        self.ctrl_temps = ctrl_temps
        self.description = description
        self.status = status
    
    # Méthode pour compiler l'ensemble des étapes de création d'un tournoi
    # Renvoi un objet tournoi crée
    def creation_tournoi(self):
        self.date = self.generate_date()
        self.nom = self.generate_nom()
        self.lieu = self.generate_lieu()        
        self.nbr_tour = self.generate_nbr_tour()
        self.tournee = self.generate_tournee()
        self.nbr_joueur = self.generate_nbr_joueur()
        self.joueurs = self.generate_joueurs()
        self.ctrl_temps = self.generate_ctrl_temps()
        self.description = self.generate_description()
    
    # Méthode pour demander la date du tournoi
    # Renvoie le texte saisie par l'utilisateur ou par défaut la date du jour
    def generate_date(self):
        # Par défaut met la date du jour
        self.date = (datetime.today().strftime("%d-%m-%Y"))
        print("\nLe tournoi a t'il lieu aujourd'hui le ",self.date,"?") 
        date_tournoi = input("Si oui, merci de valider. Sinon mettre la nouvelle date : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(date_tournoi) != 0 :
            self.date = date_tournoi
        return self.date
    
    # Méthode pour demander le nom du tournoi
    # Renvoie le nom saisie par l'utilisateur ou par défaut "Tournoi du date du jour"
    def generate_nom(self):
        # Par défaut met "Tournoi du" suivi de la date du jour
        self.nom = (f"Tournoi du {self.date}")
        print(f"\nUn nom possible du tournoi est : {self.nom}")
        nom_tournoi = input("Si le nom vous satisfait, merci de valider. Sinon mettre le nouveau nom : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(nom_tournoi) != 0:
            self.nom = nom_tournoi
        return self.nom    
    
    # Méthode pour demander le lieu du tournoi
    # Renvoie le lieu saisie par l'utilisateur
    def generate_lieu(self):
        self.lieu = input("\nMerci de saisir le lieu du tournoi : ")
        return self.lieu

    # Méthode pour demander le nombre de tour du tournoi
    # Renvoie le nombre saisie par l'utilisateur ou la valeur de l'__init__ par défaut
    def generate_nbr_tour(self):
        print (f"\nEst ce que le tournoi va se dérouler en {self.nbr_tour} tour ?")
        nbr_tour_tournoi = input(f"Si il se déroule en {self.nbr_tour} tours, merci de valider. Sinon mettre le nombre de tour : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(nbr_tour_tournoi) != 0:
            nbr_tour_tournoi = ctrl_valeur_utilisateur(nbr_tour_tournoi)
            self.nbr_tour = nbr_tour_tournoi
        return self.nbr_tour

    # Méthode pour demander le nombre de joueur
    # Renvoie le nombre pair saisie par l'utilisateur ou la valeur de l'__init__ par défaut
    def generate_nbr_joueur(self):
        nbr_joueur = input("\nMerci de dire combien de joueur participerons au tournoi : ")
        controle = False
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        while controle is False:
            # A condition que la saisie utilisateur soit un nombre
            if nbr_joueur != self.nbr_joueur:
                nbr_joueur = ctrl_valeur_utilisateur(nbr_joueur)
                # Et a condition que le nombre soit positif (divisible par 0)
                if (nbr_joueur % 2) == 0:
                   self.nbr_joueur = nbr_joueur
                   controle = True
                else:
                    nbr_joueur = input("Merci de rentrer un nombre de joueur pair : ")
        return self.nbr_joueur
    
    # Méthode pour demander la tournée ????
    def generate_tournee(self):
        pass

    # Méthode pour demander les joueurs participants au tournoi
    def generate_joueurs(self):
        self.joueurs = {}
        return self.joueurs

    # Méthode pour demander le type de jeu
    # Renvoie le type saisie par l'utilisateur
    def generate_ctrl_temps(self):
        menu_max=3
        # Demande à l'utilisateur le nom du tournoi
        reponse_temps = vue_choix_type_partie()
        self.ctrl_temps = ctrl_valeur_menu(menu_max, reponse_temps)
        # Suivant la réponse de l'utilisateur affecte le type de partie
        if self.ctrl_temps == 1:
            self.ctrl_temps = "Blitz"
        elif self.ctrl_temps == 2:
            self.ctrl_temps = "Bullet"
        else:
            self.ctrl_temps = "Coup rapide"
        return self.ctrl_temps

    # Méthode pour demander la description du tournoi
    # Renvoie le texte saisie par l'utilisateur
    def generate_description(self):
        self.description = input("\nSouhaitez vous rajouter une description : ")
        return self.description
    
    # Méthode pour ajouter un tournoi dans la base de donnée json
    # Ne renvoi rien, mais rajoute le tournoi à la base de donnée json
    def ajout_tournoi_bdd(self):
        bdd_tournoi = initialisation_bdd_tournoi()
        #Transforme les objets JoueurTournoi en dictionnaire pour  mettre en json
        dico_global_joueurs={}
        dico_joueur={}
        for joueur in self.joueurs:
            dico_joueur={}
            dico_joueur["nom"] = self.joueurs[joueur].nom
            dico_joueur["prenom"] = self.joueurs[joueur].prenom
            dico_joueur["sexe"] = self.joueurs[joueur].sexe
            dico_joueur["naissance"] = self.joueurs[joueur].naissance
            dico_joueur["classement"] = self.joueurs[joueur].classement
            dico_joueur["position"] = self.joueurs[joueur].position
            dico_joueur["couleur"] = self.joueurs[joueur].couleur
            dico_joueur["ordre"] = self.joueurs[joueur].ordre
            dico_joueur["paires"] = self.joueurs[joueur].paires
            dico_joueur["points"] = self.joueurs[joueur].points
            dico_global_joueurs[joueur]=dico_joueur

        bdd_tournoi.insert({"nom" : self.nom,
                          "lieu" : self.lieu,
                          "date" : self.date,
                          "nbr_tour" : self.nbr_tour,
                          "tour_actif" : self.tour_actif,
                          "tournee" : self.tournee,
                          "nbr_joueur" :self.nbr_joueur,
                          "joueurs" : dico_global_joueurs,
                          "ctrl_temps" : self.ctrl_temps,
                          "description" : self.description,
                          "status" : self.status})

    # Méthode pour créer l'ordre des duels du premier tour
    # Affilie à la classe joueur l'ordre des duels
    def ordre_premier_tour(self):
        liste_croissant = []
        #Classe la liste des valeurs de classement par ordre croissant
        for participant in self.joueurs:
            liste_croissant.append(self.joueurs[participant].classement)
            liste_croissant.sort()
        
        #Donne l'ordre au participant
        #Balaie la liste des joueurs
        for participant in self.joueurs:
            ordre = 1
            #Balaie la liste des nombres
            for nombre in liste_croissant:
                #Si un nombre est identique au classement. C'est le bon joueur
                if nombre == self.joueurs[participant].classement:
                    #En cas de classement identique, affilie au premier joueur sans ordre
                    if self.joueurs[participant].ordre == "":
                        self.joueurs[participant].ordre = ordre
                        ordre += 1
        return
    
    # Méthode pour lancer le premier tour
    def creation_premier_tour(self):
        self.ordre_premier_tour()
        self.creation_paire()
    
    def creation_paire(self):
        numero_de_paires = 1
        for participant in self.joueurs:
            #Vérifie que nous sommes bien dans la première moitié
            if participant <= (self.nbr_joueur)/2:
                self.joueurs[participant].paires = numero_de_paires
                #Permet de prendre l'adversaire opposé
                adversaire = ((self.nbr_joueur)/2) + participant
                self.joueurs[adversaire].paires = numero_de_paires
            numero_de_paires += 1
    
    def affichage_adversaire(self,numero_paire):
        joueur1 = ""
        joueur2 = ""
        for participant in self.joueurs:
            if self.joueurs[participant].paires == numero_paire:
                if joueur1 == "":
                    joueur1 = self.joueurs[participant] 
                else:
                    joueur2 = self.joueurs[participant]
        return (joueur1, joueur2)
