from tinydb import TinyDB, where

def recherche_joueur_bdd(categorie_recherche, mot_recherche):
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    #Regarde si le joueur avec le classement en argument existe
    joueur_trouve=joueur_aj.search(where(categorie_recherche) == mot_recherche)
    #Si la réponse est vide, ne retourne rien
    return (joueur_trouve)