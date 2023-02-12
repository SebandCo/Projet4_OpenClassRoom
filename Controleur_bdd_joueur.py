from tinydb import TinyDB, where, Query
from Controleur_valeur_menu import *

def recherche_joueur_bdd(categorie_recherche, mot_recherche):
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    #Regarde si le joueur avec le classement en argument existe
    joueur_trouve=joueur_aj.search(where(categorie_recherche) == mot_recherche)
    #Si la réponse est vide, ne retourne rien
    return (joueur_trouve)

def modif_joueur_bdd(position,categorie_recherche):
    Joueur = Query()
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    valeur_modif = input("Si vous voulez modifier, merci de saisir la nouvelle valeur, sinon valider simplement : ")
    if valeur_modif:
        if categorie_recherche == "classement" :
            valeur_modif = ctrl_valeur_utilisateur(valeur_modif)
        joueur_aj.update({categorie_recherche:valeur_modif}, Joueur.position == position)
        return valeur_modif
    return
