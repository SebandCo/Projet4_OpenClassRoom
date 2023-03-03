from Vue.nettoyage_ecran import nettoyage_ecran


# Permet d'afficher le menu général des rapport
def vue_menu_rapport():
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    menu_max = 9
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
        "\n8 --> Rapport flake8\n\n"
        "9 --> Revenir au menu précédent\n")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro de menu : ")

    return (reponse_menu, menu_max)


# Permet d'afficher le détail des tours d'un tournoi
def vue_rapport_tours(tournoi):
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"        Rapport du tournoi {tournoi.nom}\n"
        "==================================================\n\n")

    print(f"Le tournoi a {tournoi.tour_actif-1} tours déjà réalisés\n"
          f"Voici le détail des tours\n\n")

    compteur_round = 1
    compteur_match = 1
    for round in tournoi.round_global:
        print(f"Round {compteur_round}:")
        for matchs in round:
            print(f"\tMatchs {compteur_match} :\n"
                  f"\t\t{tournoi.joueurs[int(matchs[0])].nom} {tournoi.joueurs[int(matchs[0])].prenom}"
                  f" contre "
                  f"{tournoi.joueurs[int(matchs[-1])].nom} {tournoi.joueurs[int(matchs[-1])].prenom}\n")
            compteur_match += 1
        compteur_round += 1
    input("Appuyer sur Entrée pour continuer")
    return
