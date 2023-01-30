# -*- coding: utf-8 -*-
# Module pour l'importation de la base de donnée
from tinydb import TinyDB, where
from datetime import datetime
from Controleur_valeur_menu import *

class Tournoi:
    def __init__(self,
                nom = "",
                lieu = "",
                date = "",
                nbr_tour = 4,
                tournee = "",
                joueurs = "",
                ctrl_temps = "",
                description = ""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_tour = nbr_tour
        self.tournee = tournee
        self.joueurs = joueurs
        self.ctrl_temps = ctrl_temps
        self.description = description
    
    # Méthode pour compiler l'ensemble des étapes de création d'un tournoi
    # Renvoi un objet tournoi crée
    def creation_tournoi(self):
        self.date = self.generate_date()
        self.nom = self.generate_nom()
        self.lieu = self.generate_lieu()        
        self.nbr_tour = self.generate_nbr_tour()
        self.tournee = self.generate_tournee()
        self.joueurs = self.generate_joueurs()
        self.ctrl_temps = self.generate_ctrl_temps()
        self.description = self.generate_description()
    
    # Méthode pour demander la date du tournoi
    # Renvoie par défaut la date du jour
    def generate_date(self):
        self.date = (datetime.today().strftime("%d-%m-%Y"))
        print("\nLe tournoi a t'il lieu aujourd'hui le ",self.date,"?") 
        date_tournoi = input("Si oui, merci de valider. Sinon mettre la nouvelle date :")
        if len(date_tournoi) != 0 :
            self.date = date_tournoi
        return self.date
    
    # Méthode pour demander le nom du tournoi
    # Renvoie le nom saisie par l'utilisateur ou le nom prédifini
    def generate_nom(self):
        self.nom = (f"Tournoi du {self.date}")
        print(f"\nUn nom possible du tournoi est : {self.nom}")
        nom_tournoi = input("Si le nom vous satisfait, merci de valider. Sinon mettre le nouveau nom :")
        if len(nom_tournoi) != 0:
            self.nom = nom_tournoi
        return self.nom    
    
    # Méthode pour demande le lieu du tournoi
    # Renvoie le lieu saisie par l'utilisateur
    def generate_lieu(self):
        self.lieu = input("\nMerci de saisir le lieu du tournoi : ")
        return self.lieu
        
    def generate_nbr_tour(self):
        print (f"\nEst ce que le tournoi va se dérouler en {self.nbr_tour} tour ?")
        nbr_tour_tournoi = input(f"Si il se déroule en {self.nbr_tour} tours, merci de valider. Sinon mettre le nombre de tour :")
        if len(nbr_tour_tournoi) != 0:
            ctrl_valeur_utilisateur(nbr_tour_tournoi)
            self.nbr_tour = nbr_tour_tournoi
        return self.nbr_tour

    def generate_tournee(self):
        pass

    def generate_joueurs(self):
        pass

    def generate_ctrl_temps(self):
        menu_max=3
        print( "Quel type de tournoi allez vous faire? :"
        "1 - Un Blitz"
        "2 - Un Bullet"
        "3 - Un coup rapide")
        reponse_temps = input ("Quel est votre choix? 1, 2 ou 3 :")
        self.ctrl_temps = ctrl_valeur_menu(menu_max, reponse_temps)
        if self.ctrl_temps == 1:
            self.ctrl_temps = "Blitz"
        elif self.ctrl_temps == 2:
            self.ctrl_temps = "Bullet"
        else:
            self.ctrl_temps = "coup rapide"
        return self.ctrl_temps

    def generate_description(self):
        self.description = input("\nSouhaitez vous rajouter une description : ")
        return self.description