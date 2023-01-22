from Vue_menu_recherche_joueur import *
from Controleur_valeur_menu import *
from Modele_recherche_joueur import *

def ctrl_menu_recherche_joueur():
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Nombre de menu possible
    menu_max_joueur = 6
    
    while reponse_utilisateur_menu_joueur != menu_max_joueur:
        reponse_menu = vue_menu_recherche_joueur()
        
        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu[0])
        reponse_menu[0] = int(reponse_menu[0])
        if reponse_menu[0] == 1:
            reponse_menu[0] = "nom"
        elif reponse_menu[0] == 2:
            reponse_menu[0] = "prenom"
        elif reponse_menu[0] == 3:
            reponse_menu[0] = "naissance"
        elif reponse_menu[0] == 4:
            reponse_menu[0] = "sexe"
        elif reponse_menu[0] == 5:
            reponse_menu[0] = "classement"
        
        resultat_recherche = recherche_joueur_bdd(reponse_menu[0], reponse_menu[1])
        vue_menu_resultat_recherche_joueur(resultat_recherche)

        
