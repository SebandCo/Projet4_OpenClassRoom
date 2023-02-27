
from Vue_nettoyage_ecran import nettoyage_ecran


def vue_menu_principal():
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    menu_max = 5
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Que souhaitez vous faire?")
    print(
        "1 --> Gestion des joueurs\n"
        "2 --> Création d'un nouveau tournoi\n"
        "3 --> Revoir/Reprendre un tournoi\n"
        "4 --> Afficher les rapports (NOK)\n"
        "5 --> Sortir du programme\n")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro de menu : ")

    return (reponse_menu, menu_max)
