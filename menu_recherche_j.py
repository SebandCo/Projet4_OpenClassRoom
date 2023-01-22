# -*- coding: utf-8 -*-
from recherche_j import *
import os


def menu_recherche_joueur():
    # Permet de nettoyer l'écran
    os.system("cls")
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Recherche de Joueur\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Comment souhaitez vous rechercher votre joueur?")
    print(
        "1 --> Par Nom\n"
        "2 --> Par Prénom\n"
        "3 --> Par Date de Naissance\n"
        "4 --> Par Sexe\n"
        "5 --> Par Numéro de Classement\n"
        "6 --> Annuler la recherche")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro choisi : ")
    # Initialisation du controle de valeur de reponse_menu
    reponse_correct = 0

    while reponse_correct == 0:  # Tant que le controle n'est pas valide
        try:
            # Vérifie si reponse_menu est un entier
            int(reponse_menu)
            # Met le string en integer
            reponse_menu = int(reponse_menu)
            # Vérifie que reponse_menu est compris entre 1 et 6
            if 1 <= reponse_menu <= 6:
                # Valide le controle pour sortir de la boucle
                reponse_correct = 1
            else:
                # Si reponse_menu n'est pas compris entre 1 et 6
                reponse_menu = input("Merci de choisir un menu existant : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_menu = input("Merci de choisir un menu existant : ")

    # Si la réponse est 6, on reviens au menu précédent
    if reponse_menu == 6:
        return
    # Sinon on lance la recherche
    else:
        mot_recherche = input("Merci de saisir votre recherche : ")
        if reponse_menu == 1:
            reponse_recherche = "nom"
        elif reponse_menu == 2:
            reponse_recherche = "prenom"
        elif reponse_menu == 3:
            reponse_recherche = "naissance"
        elif reponse_menu == 4:
            reponse_recherche = "sexe"
        elif reponse_menu == 5:
            reponse_recherche = "classement"
            # Boucle try, pour vérifier que classement est un nombre
            try:
                # Si c'est un nombre alors transforme mot_recherche en integer
                mot_recherche = int(mot_recherche)
            except:
                # Sinon ne fait rien
                mot_recherche = mot_recherche


    joueur_existant = recherche_joueur(reponse_recherche, mot_recherche)

    if len(joueur_existant) == 0:
        print("Aucun joueur n'a été trouvé")
        # Pause pour permettre à l'utilisateur de lire le resultat
        input("\n Appuyer sur ""Entrée"" pour continuer")
        menu_recherche_joueur()
    else:
        print("Un joueur a été trouvé :", joueur_existant)
        # Pause pour permettre à l'utilisateur de lire le resultat
        input("\n Appuyer sur ""Entrée"" pour continuer")
        menu_recherche_joueur()
