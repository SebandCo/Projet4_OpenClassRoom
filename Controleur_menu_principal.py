from Vue_menu_principal import *
from Controleur_valeur_menu import *
from Controleur_menu_joueur import *
from Controleur_menu_tournoi import *

def ctrl_menu_principal():
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_principal = 0
    
    # Affiche la vue du menu principal
    reponse_utilisateur = vue_menu_principal()
    
    # Nombre de menu possible
    menu_max_principal = reponse_utilisateur[1]
    reponse_menu_principal = reponse_utilisateur[0]

    while reponse_utilisateur_menu_principal != menu_max_principal:
        # Controle la réponse de l'utilisateur
        reponse_utilisateur_menu_principal = ctrl_valeur_menu(menu_max_principal, reponse_menu_principal)

        if reponse_utilisateur_menu_principal == 1:
            ctrl_menu_joueur()
            # Relance le menu principale
            reponse_utilisateur = vue_menu_principal()
            reponse_menu_principal = reponse_utilisateur[0]
        elif reponse_utilisateur_menu_principal == 2:
            ctrl_menu_tournoi()
        elif reponse_utilisateur_menu_principal == 3:
            print("Vous avez choisi le menu 3")

    print("\n A une prochaine fois\n")