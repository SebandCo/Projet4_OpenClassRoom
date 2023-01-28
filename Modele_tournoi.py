# -*- coding: utf-8 -*-
# Module pour l'importation de la base de donnée
from tinydb import TinyDB, where
from datetime import datetime
from Controleur_valeur_menu import *

class Tournoi:
    def __init__(self,
                nom,
                lieu,
                date,
                nbr_tour,
                tournee,
                joueurs,
                ctrl_temps,
                description):
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
        print("\nLe tournoi a t'il lieu aujourd'hui le ", self.date,"?") 
        date_tournoi = input("Si oui, merci de valider. Sinon mettre la nouvelle date :")
        if len(date_tournoi) != 0 :
            self.date = date_tournoi
        return self.date
    
    # Méthode pour demander le nom du tournoi
    # Renvoie le nom saisie par l'utilisateur ou le nom prédifini
    def generate_nom(self):
        self.nom = "Tournoi du",self.date
        print("\nUn nom possible du tournoi est : Tournoi du ",self.date)
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
        self.nbr_tour = 4
        print ("\nEst ce que le tournoi va se dérouler en ", self.nbr_tour,"tour ?")
        print ("Si le tournoi se déroule en",self.nbr_tour,"tours, merci de valider. Sinon mettre le nombre de tour :")
        nbr_tour_tournoi = input()
        if len(nbr_tour_tournoi) != 0:
            ctrl_valeur_utilisateur(nbr_tour_tournoi)
            self.nbr_tour = nbr_tour_tournoi
        return self.nbr_tour

    def generate_tournee(self):
        pass

    def generate_joueurs(self):
        pass

    def generate_ctrl_temps(self):
        pass

    def generate_description(self):
        self.description = input("\nSouhaitez vous rajouter une description : ")
        return self.description