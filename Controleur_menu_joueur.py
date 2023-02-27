from Vue_menu_joueur import vue_menu_joueur
from Controleur_valeur_menu import ctrl_valeur_menu
from Controleur_menu_recherche_joueur import ctrl_menu_recherche_joueur
from Modele_joueur import Joueur


def ctrl_menu_joueur():
    # Indique que nous accedons au menu joueur via le menu général et non le menu Tournoi
    menu_tournoi = False
    # Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Affichage de la vue menu joueur
    reponse_utilisateur = vue_menu_joueur()

    menu_max_joueur = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_joueur != menu_max_joueur:

        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)

        # Choix 1 : Recherche d'un joueur
        if reponse_utilisateur_menu_joueur == 1:
            # Affiche la fonction de recherche de joueur
            ctrl_menu_recherche_joueur(menu_tournoi)
            # Relance le menu principale
            reponse_utilisateur = vue_menu_joueur()
            reponse_menu = reponse_utilisateur[0]
        # Choix 2 : Création d'un joueur
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

    # Choix 3 : Retour au menu principal
    return
