
from Vue_nettoyage_ecran import *

def vue_menu_rapport():
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    menu_max = 8
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Edition de Rapport\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Quel rapport souhaitez vous éditer?")
    print(
        "Coté joueurs\n"
        "\t1 --> Liste des joueurs par ordre alphabétique\n"
        "\t2 --> Liste des joueurs par ordre de classement\n"
        "Coté tournoi\n"
        "\t3 --> Liste de l'ensemble des tournois\n"
        "Coté tournoi spécifique\n"
        "\t4 --> Liste des joueurs par ordre alphabétique\n"
        "\t5 --> Liste des joueurs par ordre de classement\n"
        "\t6 --> Liste des tours d'un tournoi\n"
        "\t7 --> Liste des matchs d'un tournoi\n"
        "8 --> Revenir au menu précédent")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro de menu : ")
    
    return (reponse_menu,menu_max)