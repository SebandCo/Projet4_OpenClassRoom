from Vue_nettoyage_ecran import *

def vue_menu_revoir_reprendre_tournoi_accueil(tournoi_existant):
    # Permet de nettoyer l'écran
    nettoyage_ecran()
    # Logo de démarrage
    print(
        "==================================================\n"
        "           Logiciel de tournois d'Echec\n"
        "           Revoir ou Reprendre un tournoi\n"
        "==================================================\n\n")

    # Menu de selection pour l'utilisateur
    print("Voici la liste des tournois en mémoire :")
    compteur = 1
    for tournoi in tournoi_existant:
        vue_menu_revoir_reprendre_affichage_tournoi(compteur,tournoi)
        compteur += 1

    print(f"{compteur} : retour au menu principal" )
    
    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir votre choix : ")
    
    menu_max = compteur
    return (reponse_menu,menu_max)

def vue_menu_revoir_reprendre_affichage_tournoi(compteur,tournoi):
    
    # Réponse si le tournoi est toujours en cours
    if tournoi['status'] == "En cours":
        print(compteur, ":\t",
            f"{tournoi['nom']} qui a commencé à {tournoi['lieu']} le {tournoi['date']}\n",
            f"\t Il oppose {tournoi['nbr_joueur']} joueurs en {tournoi['nbr_tour']} tours\n"
            f"\t C'est un tournoi {tournoi['ctrl_temps']}\n"
            f"\t le tournoi est toujours en cours\n")

    # Réponse si le tournoi est terminé
    else:
        print(compteur, ":\t",
            f"{tournoi['nom']} qui a eu lieu à {tournoi['lieu']} le {tournoi['date']}\n",
            f"\t Il a opposé {tournoi['nbr_joueur']} joueurs en {tournoi['nbr_tour']} tours\n"
            f"\t C'est un tournoi {tournoi['ctrl_temps']}\n"
            f"\t le tournoi est à présent terminé\n")
            
    if len(tournoi['description']) != 0:
        print("\tVoici une description du tournoi :\n"
            f"\t {tournoi['description']}\n")
    
    return