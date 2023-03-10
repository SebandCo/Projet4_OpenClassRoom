from Vue.nettoyage_ecran import nettoyage_ecran
"""
    Liste de Vue affichée à l'utilisateur lors de la création d'un tournoi
    Comprend aussi les vues de déroulement du tournoi
"""


# Permet d'afficher le menu général de la création d'un tournoi
def vue_menu_nouveau_tournoi():
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Nouveau Tournoi\n"
        "==================================================\n\n")

    # Menu d'initialisation pour l'utilisateur
    print("Commençons par initialiser le tournoi\n")


# Permet d'afficher un récapitulatif du tournoi créé
def vue_recap_menu_nouveau_tournoi(tournoi):
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Nouveau Tournoi\n"
        "==================================================\n\n")
    print(f"Le tournoi suivant a été crée :\n"
          f"{tournoi.nom}\n"
          f"\tIl a lieu à {tournoi.lieu} le {tournoi.date}\n"
          f"\tCa sera un {tournoi.ctrl_temps}\n"
          f"\tIl se déroulera en {tournoi.nbr_tour} tours\n"
          f"\tIl y aura {tournoi.nbr_joueur} joueurs dans ce tournoi\n")
    if len(tournoi.description) != 0:
        print(f"\tVoici la description donnée par le créateur :\n"
              f"{tournoi.description}\n")
    input("Passons maintenant à la création des joueurs")


# Permet d'afficher le choix de type de partie
def vue_choix_type_partie():
    print("\nQuel type de tournoi allez vous faire?"
          "\n1 - Un Blitz"
          "\n2 - Un Bullet"
          "\n3 - Un Coup rapide")

    # Récupération du choix de l'utilisateur
    reponse_temps = input("Quel est votre choix? 1, 2 ou 3 : ")
    return reponse_temps


# Permet d'afficher le menu joueur lors de la création d'un tournoi
def vue_menu_nouveau_tournoi_creation_joueur(tournoi, compteur):
    nettoyage_ecran()
    menu_max = 2

    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"               {tournoi.nom}\n"
        f"           Rajout des {tournoi.nbr_joueur} joueurs\n"
        f"                 Joueur {compteur}/{tournoi.nbr_joueur}\n"
        "==================================================\n\n")

    print("Que souhaitez vous faire?\n"
          "1 --> Création d'un nouveau joueur\n"
          "2 --> Recherche d'un joueur existant\n")
    reponse_menu = input("Merci de saisir le numéro de menu : ")

    return (reponse_menu, menu_max)


# Permet d'afficher la liste des duels de la manche en cours
def vue_tournoi_liste_duel(tournoi):
    nettoyage_ecran()
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"               {tournoi.nom}\n"
        f"                 Round {tournoi.tour_actif}/{tournoi.nbr_tour}\n"
        "==================================================\n\n")
    numero_paire = 1
    while numero_paire <= tournoi.nbr_joueur/2:
        adversaires = tournoi.affichage_adversaire(numero_paire)
        if tournoi.tour_actif == 1:
            print(f"Le duel {numero_paire} opposera :\n"
                  f"\t{adversaires[0].nom} {adversaires[0].prenom} {adversaires[0].classement}eme au classement\n"
                  f"\t{adversaires[0].nom} {adversaires[0].prenom} prendra les {adversaires[0].couleur}\n"
                  f"avec\n"
                  f"\t{adversaires[1].nom} {adversaires[1].prenom} {adversaires[1].classement}eme au classement\n"
                  f"\t{adversaires[1].nom} {adversaires[1].prenom} prendra les {adversaires[1].couleur}\n\n")
        else:
            print(f"Le duel {numero_paire} opposera :\n"
                  f"\t{adversaires[0].nom} {adversaires[0].prenom} avec {format(adversaires[0].points,'.1f')}"
                  f"points ({adversaires[0].classement}eme)\n"
                  f"\t{adversaires[0].nom} {adversaires[0].prenom} prendra les {adversaires[0].couleur}\n"
                  f"avec\n"
                  f"\t{adversaires[1].nom} {adversaires[1].prenom} avec {format(adversaires[1].points,'.1f')}"
                  f"points ({adversaires[1].classement}eme)\n"
                  f"\t{adversaires[1].nom} {adversaires[1].prenom} prendra les {adversaires[1].couleur}\n\n")
        numero_paire += 1

    input("Appuyer sur Entrée pour continuer")


# Permet de récupérer le résultat de chaque duel de la manche en cours
def vue_tournoi_recuperation_score(numero_de_paires, joueur1, joueur2, tournoi):
    nettoyage_ecran()
    menu_max = 3
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"               {tournoi.nom}\n"
        f"                 Round {tournoi.tour_actif}/{tournoi.nbr_tour}\n"
        "==================================================\n\n")

    print(f"Merci d'indiquer le vainqueur du duel {numero_de_paires}:\n"
          f"1 :\t {tournoi.joueurs[joueur1].nom} {tournoi.joueurs[joueur1].prenom}\n"
          f"2 :\t {tournoi.joueurs[joueur2].nom} {tournoi.joueurs[joueur2].prenom}\n"
          f"3 :\t match nul")

    reponse_menu = input("Merci de saisir votre choix : ")

    return (reponse_menu, menu_max)


# Permet d'afficher le resultat final du tournoi
def vue_tournoi_resultat(tournoi):
    nettoyage_ecran()
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"               {tournoi.nom}\n"
        f"                 Resultat finaux\n"
        "==================================================\n\n")
    classement = 1
    print("Le tournoi est à présent terminé\n"
          "Voici le classement final\n\n")
    while classement <= tournoi.nbr_joueur:
        for participant in tournoi.joueurs:
            if tournoi.joueurs[participant].ordre == classement:
                if classement == 1:
                    print(f"Le vainqueur du tournoi est :\n"
                          f"{tournoi.joueurs[participant].prenom} {tournoi.joueurs[participant].nom}"
                          f" avec {format(tournoi.joueurs[participant].points,'.1f')} points\n\n"
                          f"voici la suite du classement\n")
                else:
                    print(f"{classement}eme\t{tournoi.joueurs[participant].prenom} {tournoi.joueurs[participant].nom}"
                          f" avec {format(tournoi.joueurs[participant].points,'.1f')} points\n")

                classement += 1

    input("Appuyer sur Entrée pour continuer")


# Permet d'afficher les resultats à la fin de chaque duel
def vue_tournoi_resultat_intermediaire(tournoi):
    nettoyage_ecran()
    menu_max = 2
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"               {tournoi.nom}\n"
        f"         Résultat : Round {(tournoi.tour_actif)-1}/{tournoi.nbr_tour}\n"
        "==================================================\n\n")
    classement = 1
    print(f"Voici le resultat du Round {(tournoi.tour_actif)-1}/{tournoi.nbr_tour}\n")
    while classement <= tournoi.nbr_joueur:
        for participant in tournoi.joueurs:
            if tournoi.joueurs[participant].ordre == classement:
                print(f"{classement}eme\t{tournoi.joueurs[participant].prenom} {tournoi.joueurs[participant].nom}"
                      f" avec {format(tournoi.joueurs[participant].points,'.1f')} points\n")
                classement += 1

    print("Que voulez vous faire ?\n"
          "1 :\tContinuer le tournoi\n"
          "2 :\tMettre le tournoi en pause\n")

    reponse_menu = input("Merci de saisir votre choix : ")
    return (reponse_menu, menu_max)
