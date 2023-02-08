from Vue_menu_recherche_joueur import *
from Controleur_valeur_menu import *
from Modele_recherche_joueur import *

def ctrl_menu_recherche_joueur(menu_tournoi):
    
    reponse_utilisateur_menu_joueur = False

    reponse_utilisateur = vue_menu_recherche_joueur()
    
    menu_max = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_joueur != menu_max:      
        # Permet de relancer une recherche si le programme n'est pas sur le premier tour
        if reponse_utilisateur_menu_joueur != False:
            reponse_utilisateur = vue_menu_recherche_joueur()
            reponse_menu = reponse_utilisateur[0]

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
                if menu_tournoi == False :
                    retour_tampon = ctrl_menu_recherche_choix_joueur_simple(resultat_recherche)
                    if retour_tampon == "retour_generale":
                        return
                    elif retour_tampon == "retour_menu":
                        pass
                else:
                    joueur_selectionne = ctrl_menu_recherche_choix_joueur_tournoi(resultat_recherche)
                    return joueur_selectionne
    return
def ctrl_menu_recherche_choix_joueur_tournoi(resultat_recherche):
    reponse_utilisateur_orientation_joueur = 0

    reponse_utilisateur = vue_menu_choix_resultat_recherche_joueur_tournoi()
    
    menu_max = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]    

    while reponse_utilisateur_orientation_joueur != menu_max:
        reponse_utilisateur_orientation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)
    
        if reponse_utilisateur_orientation_joueur != menu_max:
            if reponse_utilisateur_orientation_joueur == 1 or reponse_utilisateur_orientation_joueur == 2:
                reponse_choix_joueur = input("Quel numéro de joueur voulez vous selectionner ? : ")
                nbr_max_joueur = len(resultat_recherche)
                reponse_choix_joueur = ctrl_valeur_menu(nbr_max_joueur,reponse_choix_joueur)
                compteur = 0
                for joueur in resultat_recherche:
                    compteur += 1
                    if compteur == reponse_choix_joueur:
                        joueur_selectionne = joueur
                        nombre_trouve = compteur
                print ("Vous avez choisi le joueur : ")
                vue_menu_affichage_joueur_recherche_joueur(joueur_selectionne, nombre_trouve)
                input()
                if reponse_utilisateur_orientation_joueur == 1:
                    return joueur_selectionne
                elif reponse_utilisateur_orientation_joueur == 2:
                    input("Joueur à modifier")
                    return joueur_selectionne
            elif reponse_utilisateur_orientation_joueur == 3:
                return 

def ctrl_menu_recherche_choix_joueur_simple(resultat_recherche):

    reponse_utilisateur_orientation_joueur = 0

    reponse_utilisateur = vue_menu_choix_resultat_recherche_joueur_simple()
    
    menu_max = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]    

    while reponse_utilisateur_orientation_joueur != menu_max:
        reponse_utilisateur_orientation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)
    
        if reponse_utilisateur_orientation_joueur != menu_max:
            if reponse_utilisateur_orientation_joueur == 1:
                reponse_choix_joueur = input("Quel numéro de joueur voulez vous modifier ? :")
                nbr_max_joueur = len(resultat_recherche)
                reponse_choix_joueur = ctrl_valeur_menu(nbr_max_joueur,reponse_choix_joueur)
                compteur = 0
                for joueur in resultat_recherche:
                    compteur += 1
                    if compteur == reponse_choix_joueur:
                        joueur_selectionne = joueur
                input (f"Vous avez choisi le joueur : {joueur_selectionne}")
                return ("retour_menu")
            elif reponse_utilisateur_orientation_joueur == 2:
                return ("retour_menu")
            elif reponse_utilisateur_orientation_joueur == 3:
                return ("retour_generale")
    
    return ("retour_generale")

