from Vue_nettoyage_ecran import *

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

def vue_recap_menu_nouveau_tournoi(tournoi):
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Nouveau Tournoi\n"
        "==================================================\n\n")
    print(f"Le tournoi suivant a été crée : \n"
        f"{tournoi.nom}\n"
        f"\tIl a lieu à {tournoi.lieu} le {tournoi.date}\n"
        f"\tCa sera un {tournoi.ctrl_temps}\n"
        f"\tIl se déroulera en {tournoi.nbr_tour} tours\n"
        f"\tIl y aura {tournoi.nbr_joueur} joueurs dans ce tournoi\n")
    if len(tournoi.description) != 0:
        print(f"\tVoici la description donnée par le créateur\n{tournoi.description}\n")
    input("Passons maintenant à la création des joueurs")

def vue_choix_type_partie():
    print("\nQuel type de tournoi allez vous faire?"
        "\n1 - Un Blitz"
        "\n2 - Un Bullet"
        "\n3 - Un Coup rapide")
    
    # Récupération du choix de l'utilisateur
    reponse_temps = input ("Quel est votre choix? 1, 2 ou 3 :")
    return reponse_temps

def vue_menu_nouveau_tournoi_creation_joueur(tournoi):
    nettoyage_ecran()
    menu_max = 2
    
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        f"                   {tournoi.nom}\n"
        f"          Rajout des {tournoi.nbr_joueur} joueurs\n"
        "==================================================\n\n")
    print("Que souhaitez vous faire?")
    print(
        "1 --> Recherche d'un joueur\n"
        "2 --> Création d'un nouveau joueur\n")
    reponse_menu = input("Merci de saisir le numéro de menu : ")
    
    return (reponse_menu, menu_max)