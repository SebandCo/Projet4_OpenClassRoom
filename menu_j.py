# -*- coding: utf-8 -*-
from menu_g import *
from class_joueur import *
from menu_recherche_j import *
from recherche_j import *
import os


def menu_joueur():
    # Permet de nettoyer l'écran
    os.system("cls")
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "                  Menu Joueur\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Que souhaitez vous faire?")
    print(
        "1 --> Recherche d'un joueur\n"
        "2 --> Création d'un nouveau joueur\n"
        "3 --> Retour au menu principal")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro de menu : ")
    # Initialisation du controle de valeur de reponse_menu
    reponse_correct = 0

    # Tant que le controle n'est pas valide
    while reponse_correct == 0:
        try:
            # Vérifie si reponse_menu est un entier
            int(reponse_menu)
            # Met le string en integer
            reponse_menu = int(reponse_menu)
            # Vérifie que reponse_menu est compris entre 1 et 3
            if 1 <= reponse_menu <= 3:
                # Valide le controle pour sortir de la boucle
                reponse_correct = 1
            else:
                # Si reponse_menu n'est pas compris entre 1 et 3
                reponse_menu = input("Merci de choisir un menu existant : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_menu = input("Merci de choisir un menu existant : ")

    # Redirection en fonction du choix de l'utilisateur

    if reponse_menu == 1:
        # Affiche la fonction de recherche de joueur
        menu_recherche_joueur()
        menu_joueur()
    elif reponse_menu == 2:
        # Creation d'un retour à la ligne pour aérer la présentation
        print()
        # Appel de l'objet joueur pour la création
        nouveau_joueur = Joueur()
        
        print("Le joueur", nouveau_joueur.nom, nouveau_joueur.prenom, "a bien été rajouté à la base de donnée")
        input("Appuyer sur ""Entrée"" pour continuer")
        menu_joueur()
    elif reponse_menu == 3:
        return
