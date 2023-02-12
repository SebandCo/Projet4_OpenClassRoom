from Vue_nettoyage_ecran import *
from Controleur_bdd_json import *
from pprint import pprint
from numpy import *

def vue_menu_recherche_joueur():

    nettoyage_ecran()
    menu_max = 6

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

    return (reponse_menu,menu_max)

def vue_menu_mot_recherche_joueur(mot_recherche):
    print("\nVous avez choisi la recherche par :", mot_recherche.capitalize())
    mot_recherche = input("Merci de saisir le critère de recherche : ")
    return  mot_recherche

def vue_menu_resultat_recherche_joueur(resultat_recherche):
    if len(resultat_recherche) == 0:
        print("Aucun joueur n'a été trouvé")
        # Pause pour permettre à l'utilisateur de lire le resultat
        input("\n Appuyer sur ""Entrée"" pour continuer")
    else:
        print("Voici le resultat :\n")
        compteur = 0
        for joueur in resultat_recherche:
            compteur += 1
            vue_menu_affichage_joueur_recherche_joueur(joueur,compteur)

def vue_menu_affichage_joueur_recherche_joueur(joueur,compteur):
    print (compteur, ":\t",
            joueur["nom"], joueur["prenom"],"(",joueur["sexe"],")\n",
            "\t Né(e) le : ", joueur["naissance"],"\n"
            "\t",joueur["classement"],"eme au classement\n")
        
def vue_menu_choix_resultat_recherche_joueur_simple():
    # Menu de selection pour l'utilisateur
    menu_max = 3    
    print("Que souhaitez vous faire :")
    print(
        "1 --> Modifier un joueur(NOK)\n"
        "2 --> Faire une nouvelle recherche\n"
        "3 --> Revenir au menu précedent\n")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro choisi : ")
    
    return (reponse_menu, menu_max)

def vue_menu_choix_resultat_recherche_joueur_tournoi():
    # Menu de selection pour l'utilisateur
    menu_max = 4    
    print("Que souhaitez vous faire :")
    print(
        "1 --> Selectionner un joueur\n"
        "2 --> Modifier un joueur(NOK)\n"
        "3 --> Faire une nouvelle recherche\n")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro choisi : ")

    return (reponse_menu, menu_max)

def vue_menu_modif_joueur(joueur):
    print(f"\nVous avez choisi le joueur :\n"
            f"\t{joueur.nom} {joueur.prenom}({joueur.sexe})\n"
            f"\tNé(e) le : {joueur.naissance}\n"
            f"\t{joueur.classement}eme au classement\n")
    
    print(f"Le nom du joueur est {joueur.nom}")
    reponse = modif_joueur_bdd(joueur.position,"nom")
    if reponse:
        joueur.nom=reponse

    print(f"Le prénom du joueur est {joueur.prenom}")
    reponse = modif_joueur_bdd(joueur.position,"prenom")
    if reponse:
        joueur.prenom=reponse

    print(f"La date de naissance du joueur est {joueur.naissance}")
    reponse = modif_joueur_bdd(joueur.position,"naissance")
    if reponse:
        joueur.naissance=reponse

    print(f"Le sexe du joueur est {joueur.sexe}")
    reponse = modif_joueur_bdd(joueur.position,"sexe")
    if reponse:
        joueur.sexe=reponse

    print(f"Le classement du joueur est {joueur.classement}")
    reponse = modif_joueur_bdd(joueur.position,"classement")
    if reponse:
        joueur.classement=reponse

    print(f"\nVoici les nouvelles informations du joueur :\n",
            f"\t{joueur.nom} {joueur.prenom}({joueur.sexe})\n"
            f"\tNé(e) le : {joueur.naissance}\n"
            f"\t{joueur.classement}eme au classement\n")
    input("Appuyer sur ""Entrée"" pour continuer")
    
    return joueur
   