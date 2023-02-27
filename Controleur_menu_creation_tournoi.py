from Vue_menu_nouveau_tournoi import vue_menu_nouveau_tournoi
from Vue_menu_nouveau_tournoi import vue_recap_menu_nouveau_tournoi
from Vue_menu_nouveau_tournoi import vue_menu_nouveau_tournoi_creation_joueur
from Modele_tournoi import Tournoi
from Modele_joueur_tournoi import JoueurTournoi, Joueur
from Controleur_menu_recherche_joueur import ctrl_valeur_menu
from Controleur_menu_recherche_joueur import ctrl_menu_recherche_joueur
from Controleur_menu_deroulement_tournoi import deroulement_tournoi


def ctrl_menu_tournoi():
    # Création du tournoi
    nouveau_tournoi = ctrl_creation_du_tournoi()
    # Rajout des joueurs au tournoi
    ctrl_rajout_des_joueurs(nouveau_tournoi)
    nouveau_tournoi.ajout_tournoi_bdd()

    input("Tournoi crée\nAppuyer sur Entrée pour continuer")

    deroulement_tournoi(nouveau_tournoi)


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

        reponse_utilisateur = vue_menu_nouveau_tournoi_creation_joueur(nouveau_tournoi, compteur)
        menu_max = reponse_utilisateur[1]
        reponse_menu = reponse_utilisateur[0]

        reponse_utilisateur_creation_joueur = ctrl_valeur_menu(menu_max, reponse_menu)

        # Choix 1 : Création d'un nouveau joueur
        if reponse_utilisateur_creation_joueur == 1:
            nouveau_joueur = Joueur()
            nouveau_joueur.creation_joueur()
            nouveau_joueur.ajout_joueur_bdd()
            nouveau_joueur_tournoi = JoueurTournoi(nouveau_joueur)
            nouveau_tournoi.joueurs[compteur] = nouveau_joueur_tournoi
            # Permet de passer au joueur suivant
            compteur += 1
        # Choix 2 : Recherche d'un joueur
        elif reponse_utilisateur_creation_joueur == 2:
            # Indique que nous accedons au menu joueur via le menu tournoi
            menu_tournoi = True
            nouveau_joueur = ctrl_menu_recherche_joueur(menu_tournoi)
            # Si le joueur a bien été selectionné
            if nouveau_joueur:
                # Transforme la réponse Json(dictionnaire) en objet
                nouveau_joueur = Joueur(
                                        nouveau_joueur["nom"],
                                        nouveau_joueur["prenom"],
                                        nouveau_joueur["naissance"],
                                        nouveau_joueur["sexe"],
                                        nouveau_joueur["classement"],
                                        nouveau_joueur["position"])
                nouveau_joueur_tournoi = JoueurTournoi(nouveau_joueur)
                nouveau_tournoi.joueurs[compteur] = nouveau_joueur_tournoi
                input("Appuyer sur Entrée pour continuer")
                # Passe au joueur suivant
                compteur += 1

    return
