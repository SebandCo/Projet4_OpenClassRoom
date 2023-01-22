from Vue_menu_joueur import *
from Controleur_valeur_menu import *

def ctrl_menu_joueur():
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Nombre de menu possible
    menu_max_joueur = 3
    
    while reponse_utilisateur_menu_joueur != menu_max_joueur:
        reponse_menu = menu_joueur

        reponse_utilisateur_menu_joueur = valeur_menu(menu_max_joueur, reponse_menu)

        if reponse_utilisateur_menu_joueur == 1:
            # Affiche la fonction de recherche de joueur
            menu_recherche_joueur()
            menu_joueur()
        elif reponse_utilisateur_menu_joueur == 2:
            # Creation d'un retour à la ligne pour aérer la présentation
            print()
            # Appel de l'objet joueur pour la création
            nouveau_joueur = Joueur()
        
            print("Le joueur", nouveau_joueur.nom, nouveau_joueur.prenom, "a bien été rajouté à la base de donnée")
            input("Appuyer sur ""Entrée"" pour continuer")
            menu_joueur()