from Vue_menu_recherche_joueur import *
from Controleur_valeur_menu import *
from Modele_recherche_joueur import *

def ctrl_menu_recherche_joueur():
    menu_max = 6
    reponse_utilisateur_menu_joueur=0
    
    while reponse_utilisateur_menu_joueur != menu_max :

        reponse_menu = vue_menu_recherche_joueur()
                
        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max, reponse_menu)
        
        if reponse_utilisateur_menu_joueur != menu_max:
            if reponse_utilisateur_menu_joueur == 1:
                reponse_utilisateur_menu_joueur = "nom"
            elif reponse_utilisateur_menu_joueur == 2:
                reponse_utilisateur_menu_joueur = "prenom"
            elif reponse_utilisateur_menu_joueur == 3:
                reponse_utilisateur_menu_joueur = "naissance"
            elif reponse_utilisateur_menu_joueur == 4:
                reponse_utilisateur_menu_joueur = "sexe"
            elif reponse_utilisateur_menu_joueur == 5:
                reponse_utilisateur_menu_joueur = "classement"
            mot_recherche = vue_menu_mot_recherche_joueur(reponse_utilisateur_menu_joueur)

            resultat_recherche = recherche_joueur_bdd(reponse_utilisateur_menu_joueur, mot_recherche)
            vue_menu_resultat_recherche_joueur(resultat_recherche)

            if len(resultat_recherche) != 0:
                retour_tampon=ctrl_menu_recherche_choix_joueur(resultat_recherche)
                if retour_tampon == "retour_generale":
                    return
                elif retour_tampon == "retour_menu":
                    pass

def ctrl_menu_recherche_choix_joueur(resultat_recherche):

    menu_max = 3
    reponse_utilisateur_orientation_joueur=0

    reponse_menu = vue_menu_choix_resultat_recherche_joueur()
    

    while reponse_utilisateur_orientation_joueur != menu_max:

        reponse_utilisateur_orientation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)
    
        if reponse_utilisateur_orientation_joueur != menu_max:
            retour_tampon = "retour_menu"
            if reponse_utilisateur_orientation_joueur == 1:
                reponse_choix_joueur = input("Quel numéro de joueur voulez vous modifier ? :")
                nbr_max_joueur = len(resultat_recherche)
                reponse_choix_joueur = ctrl_valeur_menu(nbr_max_joueur,reponse_choix_joueur)
                compteur = 0
                for joueur in resultat_recherche:
                    compteur += 1
                    if compteur == reponse_choix_joueur:
                        joueur_selectionne = joueur
                print (f"Vous avez choisi le joueur : {joueur_selectionne}")
                input("tt")
                return retour_tampon
            elif reponse_utilisateur_orientation_joueur == 2:
                return retour_tampon
            elif reponse_utilisateur_orientation_joueur == 3:
                retour_tampon = "retour_generale"
    
    return retour_tampon
        
