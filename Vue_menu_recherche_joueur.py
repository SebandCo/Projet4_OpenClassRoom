import os
from pprint import pprint
from numpy import *

def vue_menu_recherche_joueur():
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
    return reponse_menu

def vue_menu_mot_recherche_joueur():
    mot_recherche = input("Merci de saisir votre recherche : ")
    return  mot_recherche

def vue_menu_resultat_recherche_joueur(resultat_recherche):
    if len(resultat_recherche) == 0:
        print("Aucun joueur n'a été trouvé")
        # Pause pour permettre à l'utilisateur de lire le resultat
        input("\n Appuyer sur ""Entrée"" pour continuer")
    elif len(resultat_recherche) == 1:
        joueur_test=resultat_recherche[0]
        print(" 1: \t",joueur_test["nom"],joueur_test["prenom"],"\n",
            "\t", joueur_test["classement"], "eme au classement")
        input("\n Appuyer sur ""Entrée"" pour continuer")
    else:
        print("Des joueurs ont été trouvé :", resultat_recherche)
        # Pause pour permettre à l'utilisateur de lire le resultat
        input("\n Appuyer sur ""Entrée"" pour continuer")