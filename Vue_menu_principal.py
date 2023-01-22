import os


def vue_menu_principal():
    # Permet de nettoyer l'écran
    os.system("cls")
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Que souhaitez vous faire?")
    print(
        "1 --> Gestion des joueurs\n"
        "2 --> Création d'un nouveau tournoi (NOK)\n"
        "3 --> Revoir un tournoi (NOK)\n"
        "4 --> Sortir du programme")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro de menu : ")
    return reponse_menu