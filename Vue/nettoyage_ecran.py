import os


# Permet de nettoyer l'écran pour afficher un écran noir
def nettoyage_ecran():

    if os.name == "nt":
        # Permet de nettoyer l'écran sous Windows
        os.system("cls")
    else:
        # Permet de nettoyer l'écran sous Mac ou Linux
        os.system("clear")
