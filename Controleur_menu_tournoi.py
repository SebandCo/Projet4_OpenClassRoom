from Vue_menu_nouveau_tournoi import *
from Modele_tournoi import *
from Modele_joueur_tournoi import *


def ctrl_menu_tournoi():
    vue_menu_nouveau_tournoi()
    nouveau_tournoi = Tournoi()
    nouveau_tournoi.creation_tournoi()
    vue_recap_menu_nouveau_tournoi(nouveau_tournoi)
    # Boucle pour le rajout des joueurs au tournoi
    compteur = 1
    while compteur != nouveau_tournoi.nbr_joueur:
        
        reponse_utilisateur_creation_joueur = 0

        reponse_utilisateur = vue_menu_nouveau_tournoi_creation_joueur(nouveau_tournoi,compteur)
        menu_max = reponse_utilisateur[1]
        reponse_menu = reponse_utilisateur[0]    

        while reponse_utilisateur_creation_joueur != menu_max:
            reponse_utilisateur_creation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)

            if reponse_utilisateur_creation_joueur == 1 :
                nouveau_joueur = JoueurTournoi()
                nouveau_joueur.creation_joueur()
                nouveau_joueur.ajout_joueur_bdd()
            
            elif reponse_utilisateur_creation_joueur == 2 :
                pass
        
        
        compteur += 1


    input("Tournoi crée")
