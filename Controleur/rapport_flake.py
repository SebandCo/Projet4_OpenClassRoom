import os


# Permet de générer un rapport flake8
def rapport_flake8():
    print("\n")
    os.system("flake8 "
              # Au format HTML
              "--format=html "
              # Dans le dossier flake-report
              "--htmldir=flake8_rapport "
              # Avec une longueur de ligne maximal à 119
              "--max-line-length 119")
    input("\n Le rapport est disponible dans le dossier flake8_rapport du programme")
