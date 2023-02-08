from Vue_menu_joueur import *
from Controleur_valeur_menu import *
from Controleur_menu_recherche_joueur import *
from Modele_joueur import *


def ctrl_menu_joueur():
    # Indique que nous accedons au menu joueur via le menu général et non le menu Tournoi
    menu_tournoi = False
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Affichage de la vue menu joueur
    reponse_utilisateur = vue_menu_joueur()

    menu_max_joueur = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_joueur != menu_max_joueur:
        

        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)

        if reponse_utilisateur_menu_joueur == 1:
            # Affiche la fonction de recherche de joueur
            ctrl_menu_recherche_joueur(menu_tournoi)
            # Relance le menu principale
            reponse_utilisateur = vue_menu_joueur()
            reponse_menu = reponse_utilisateur[0]
        elif reponse_utilisateur_menu_joueur == 2:
            # Creation d'un retour à la ligne pour aérer la présentation
            print()
            # Appel de l'objet joueur pour la création
            nouveau_joueur = Joueur()
            nouveau_joueur.creation_joueur()
            nouveau_joueur.ajout_joueur_bdd()
        
            print("Le joueur", nouveau_joueur.nom, nouveau_joueur.prenom, "a bien été rajouté à la base de donnée")
            input("Appuyer sur ""Entrée"" pour continuer")
            return
    return