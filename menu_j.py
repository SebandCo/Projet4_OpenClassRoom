# -*- coding: utf-8 -*-
from menu_g import *
from nouveau_j import *
import os

def menu_joueur():
    # Permet de nettoyer l'écran
    os.system("cls")
    # Logo de démarrage
    print("\
    ==================================================\n\
        Logiciel de tournois d'Echec - Menu Joueur\n\
    ==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Que souhaitez vous faire?")
    print("\
    1 --> Recherche d'un joueur\n\
    2 --> Création d'un nouveau joueur\n\
    3 --> Retour au menu principal")

    # Récupération du choix de l'utilisateur
    reponse_menu=input("Merci de saisir le numéro de menu : ")
    # Initialisation du controle de valeur de reponse_menu
    reponse_correct=0

    while reponse_correct==0:# Tant que le controle n'est pas valide
        try:
            # VÃ©rifie si reponse_menu est un entier
            int(reponse_menu) 
            reponse_menu=int(reponse_menu)# Met le string en integer
            # VÃ©rifie que reponse_menu est compris entre 1 et 4
            if 1<=reponse_menu<=3:
                reponse_correct=1 # Valide le controle pour sortir de la boucle
                reponse_menu=int(reponse_menu)# Met le string en integer
            else:
                # Si reponse_menu n'est pas compris entre 1 et 4
                reponse_menu=input("Merci de choisir un menu existant : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_menu=input("Merci de choisir un menu existant : ")

    # Redirection en fonction du choix de l'utilisateur
    if reponse_menu==1:
        print ("Vous avez choisi le menu 1")
    elif reponse_menu==2:
        print ()
        nouveau_joueur=joueur()
    elif reponse_menu==3:
       menu_accueil()
