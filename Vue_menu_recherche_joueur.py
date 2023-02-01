from Vue_nettoyage_ecran import *
from pprint import pprint
from numpy import *

def vue_menu_recherche_joueur():
    nettoyage_ecran()
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

    return reponse_menu

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
            print (compteur, ":\t",
                    joueur["nom"], joueur["prenom"],
                    "(",joueur["sexe"],")",
                    "\n",
                    "\t Né(e) le : ", joueur["naissance"],
                    "\n"
                    "\t",joueur["classement"],"eme au classement"
                    "\n")
        
def vue_menu_choix_resultat_recherche_joueur():
    # Menu de selection pour l'utilisateur
    print("Que souhaitez vous faire :")
    print(
        "1 --> Modifier un joueur(NOK)\n"
        "2 --> Faire une nouvelle recherche\n"
        "3 --> Revenir au menu précedent\n")

    # Récupération du choix de l'utilisateur
    reponse_menu = input("Merci de saisir le numéro choisi : ")
    
    return reponse_menu
