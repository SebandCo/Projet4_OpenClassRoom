from Vue.nettoyage_ecran import nettoyage_ecran


# Permet d'afficher le menu général des joueurs
def vue_menu_joueur():
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    menu_max = 3
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
    return (reponse_menu, menu_max)
