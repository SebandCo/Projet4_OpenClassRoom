from Vue_menu_nouveau_tournoi import *
from Modele_tournoi import *


def deroulement_tournoi(tournoi):
    
    while tournoi.tour_actif <= tournoi.nbr_tour:
        if tournoi.tour_actif == 1:
            tournoi.creation_premier_tour()
        else:
            tournoi.creation_tour()
        vue_tournoi_liste_duel(tournoi)
        tournoi.recuperation_resultat()
        tournoi.tour_actif += 1
        tournoi.ordre_tour()
        
        #Initialisation de la réponse utilisateur
        reponse_utilisateur_deroulement_tournoi = 0
    
        # Affiche la vue du menu principal
        reponse_utilisateur = vue_tournoi_resultat_intermediaire(tournoi)
    
        # Nombre de menu possible
        menu_max_principal = reponse_utilisateur[1]
        reponse_menu_principal = reponse_utilisateur[0]

        while reponse_utilisateur_deroulement_tournoi!= menu_max_principal:
            # Controle la réponse de l'utilisateur
            reponse_utilisateur_deroulement_tournoi = ctrl_valeur_menu(menu_max_principal, reponse_menu_principal)

            # Choix 1 : Continuer le tournoi
            if reponse_utilisateur_deroulement_tournoi == 1:
                break
            
            # Choix 2 : Arrêt du tournoi
            elif reponse_utilisateur_deroulement_tournoi == 2:
                return

    vue_tournoi_resultat(tournoi)