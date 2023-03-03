from Vue.menu_principal import vue_menu_principal
from Controleur.valeur_menu import ctrl_valeur_menu
from Controleur.menu_creation_tournoi import ctrl_menu_tournoi
from Controleur.menu_tournoi_existant import ctrl_reprise_tournoi_existant
from Controleur.menu_rapport import ctrl_menu_rapport
from Controleur.menu_joueur import ctrl_menu_joueur


# Permet de lancer le menu principal et la redirection en fonction des réponses
def ctrl_menu_principal():
    # Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_principal = 0

    # Affiche la vue du menu principal
    reponse_utilisateur = vue_menu_principal()

    # Nombre de menu possible
    menu_max_principal = reponse_utilisateur[1]
    reponse_menu_principal = reponse_utilisateur[0]

    while reponse_utilisateur_menu_principal != menu_max_principal:
        # Controle la réponse de l'utilisateur
        reponse_utilisateur_menu_principal = ctrl_valeur_menu(menu_max_principal, reponse_menu_principal)

        # Choix 1 : Menu Joueur
        if reponse_utilisateur_menu_principal == 1:
            ctrl_menu_joueur()

        # Choix 2 : Création d'un nouveau tournoi
        elif reponse_utilisateur_menu_principal == 2:
            ctrl_menu_tournoi()

        # Choix 3 : Visualisation ou reprise d'un tournoi existant
        elif reponse_utilisateur_menu_principal == 3:
            ctrl_reprise_tournoi_existant()

        # Choix 4 : Affichage des rapports
        elif reponse_utilisateur_menu_principal == 4:
            ctrl_menu_rapport()

        # Choix 5 : Sortir du programme
        elif reponse_utilisateur_menu_principal == 5:
            break

        # Relance le menu principale
        reponse_utilisateur = vue_menu_principal()
        reponse_menu_principal = reponse_utilisateur[0]
    print("\n A une prochaine fois\n")
