from Vue_menu_nouveau_tournoi import *
from Modele_tournoi import *
from Modele_joueur_tournoi import *
from Controleur_menu_recherche_joueur import *


def ctrl_menu_tournoi():
    
    nouveau_tournoi = ctrl_creation_du_tournoi()
    
    ctrl_rajout_des_joueurs(nouveau_tournoi)  

    input("Tournoi crée")

    nouveau_tournoi.creation_premier_tour()

    # Début du tournoi





def ctrl_creation_du_tournoi():
    # Création du tournoi
    vue_menu_nouveau_tournoi()
    nouveau_tournoi = Tournoi()
    nouveau_tournoi.creation_tournoi()
    vue_recap_menu_nouveau_tournoi(nouveau_tournoi)
    return nouveau_tournoi

def ctrl_rajout_des_joueurs(nouveau_tournoi):
    # Boucle pour le rajout des joueurs au tournoi
    compteur = 1
    while compteur != nouveau_tournoi.nbr_joueur+1:
        # Tant qu'un nouveau joueur n'a pas été crée la boucle continu
        # while nouveau_tournoi.joueurs[compteur] != "":
        reponse_utilisateur_creation_joueur = 0

        reponse_utilisateur = vue_menu_nouveau_tournoi_creation_joueur(nouveau_tournoi,compteur)
        menu_max = reponse_utilisateur[1]
        reponse_menu = reponse_utilisateur[0]    

        reponse_utilisateur_creation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)

        if reponse_utilisateur_creation_joueur == 1 :
            nouveau_joueur = JoueurTournoi()
            nouveau_joueur.creation_joueur()
            nouveau_joueur.ajout_joueur_bdd()
            nouveau_tournoi.joueurs[compteur] = nouveau_joueur    
        elif reponse_utilisateur_creation_joueur == 2 :
            # Indique que nous accedons au menu joueur via le menu tournoi
            menu_tournoi = True
            nouveau_joueur = JoueurTournoi()
            nouveau_joueur = ctrl_menu_recherche_joueur(menu_tournoi)
            nouveau_tournoi.joueurs[compteur] = nouveau_joueur

        # Si le joueur a été crée, passe au suivant
        if compteur in nouveau_tournoi.joueurs:
            compteur += 1