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

def recap_menu_nouveau_tournoi(tournoi):
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "             Menu Nouveau Tournoi\n"
        "==================================================\n\n")
    print(f"Le tournoi suivant a été crée : \n"
        f"{tournoi.nom}\n"
        f"\tIl a lieu a {tournoi.lieu} le {tournoi.date}\n"
        f"\tCa sera un {tournoi.ctrl_temps}"
        f"\tIl se déroule en {tournoi.nbr_tour} tours")