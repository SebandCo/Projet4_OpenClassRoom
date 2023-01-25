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
        
        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)
        reponse_menu = int(reponse_menu)
        if reponse_menu != menu_max_joueur:
            if reponse_menu == 1:
                reponse_menu = "nom"
            elif reponse_menu == 2:
                reponse_menu = "prenom"
            elif reponse_menu == 3:
                reponse_menu = "naissance"
            elif reponse_menu == 4:
                reponse_menu = "sexe"
            elif reponse_menu == 5:
                reponse_menu = "classement"
            mot_recherche = vue_menu_mot_recherche_joueur()

        resultat_recherche = recherche_joueur_bdd(reponse_menu, mot_recherche)
        vue_menu_resultat_recherche_joueur(resultat_recherche)

        
