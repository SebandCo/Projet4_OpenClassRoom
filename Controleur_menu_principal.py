from Vue_menu_principal import *
from Controleur_valeur_menu import *
from Controleur_menu_joueur import *

def ctrl_menu_principal():
    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_principal = 0
    # Nombre de menu possible
    menu_max_principal = 4

    while reponse_utilisateur_menu_principal != menu_max_principal:
        # Affiche la vue du menu principal
        reponse_menu_principal = vue_menu_principal()
        # Controle la réponse de l'utilisateur
        reponse_utilisateur_menu_principal = ctrl_valeur_menu(menu_max_principal, reponse_menu_principal)

        if reponse_utilisateur_menu_principal == 1:
            ctrl_menu_joueur()
        elif reponse_utilisateur_menu_principal == 2:
            print("Vous avez choisi le menu 2")
        elif reponse_utilisateur_menu_principal == 3:
            print("Vous avez choisi le menu 3")

    print("\n A une prochaine fois\n")