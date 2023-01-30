from Vue_menu_joueur import *
from Controleur_valeur_menu import *
from Controleur_menu_recherche_joueur import *
from Modele_joueur import *


def ctrl_menu_joueur():
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Nombre de menu possible
    menu_max_joueur = 3
    
    while reponse_utilisateur_menu_joueur != menu_max_joueur:
        reponse_menu = vue_menu_joueur()

        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)

        if reponse_utilisateur_menu_joueur == 1:
            # Affiche la fonction de recherche de joueur
            ctrl_menu_recherche_joueur()
        elif reponse_utilisateur_menu_joueur == 2:
            # Creation d'un retour à la ligne pour aérer la présentation
            print()
            # Appel de l'objet joueur pour la création
            nouveau_joueur = Joueur()
            nouveau_joueur.creation_joueur()
            nouveau_joueur.ajout_joueur_bdd()
        
            print("Le joueur", nouveau_joueur.nom, nouveau_joueur.prenom, "a bien été rajouté à la base de donnée")
            input("Appuyer sur ""Entrée"" pour continuer")