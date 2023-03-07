"""
    Procédure de controle des valeurs utilisateurs par rapport à l'attendu
    Comprend
    - Un controle pour vérifier que la valeur est compris entre 1 et une variable
    - Un controle pour vérifier que la valeur est positive
    - Un controle pour vérifier que la valeur est H, F ou I
"""


# Permet de controler si la réponse utilisateur correspond à un menu existant
def ctrl_valeur_menu(menu_max, reponse_menu):
    reponse_correct = False

    # Tant que le controle n'est pas valide
    while reponse_correct is False:
        try:
            # Vérifie si reponse_menu est un entier
            int(reponse_menu)
            # Met le string en integer
            reponse_menu = int(reponse_menu)
            # Vérifie que reponse_menu est compris entre 1 et le menu max
            if 1 <= reponse_menu <= menu_max:
                # Valide le controle pour sortir de la boucle
                reponse_correct = True
            else:
                # Si reponse_menu n'est pas compris entre 1 et le menu max
                reponse_menu = input("Merci de choisir un menu existant : ")
        except (ValueError):
            # Si reponse_menu n'est pas un entier
            reponse_menu = input("Merci de choisir un menu existant : ")
    return int(reponse_menu)


# Permet de controler si la réponse utilisateur est un nombre positif non nul
def ctrl_valeur_utilisateur(reponse_utilisateur):
    reponse_correct = False

    # Tant que le controle n'est pas valide
    while reponse_correct is False:
        try:
            # Vérifie si reponse_utilisateur est un entier
            int(reponse_utilisateur)
            # Met le string en integer
            reponse_utilisateur = int(reponse_utilisateur)
            # Vérifie que reponse_utilisateur est positif
            if 1 <= reponse_utilisateur:
                # Valide le controle pour sortir de la boucle
                reponse_correct = True
            else:
                # Si reponse_utilisateur n'est pas valide
                reponse_utilisateur = input("Merci de choisir un nombre positif non nul : ")
        except (ValueError):
            # Si reponse_utilisateur n'est pas un entier
            reponse_utilisateur = input("Merci de choisir un nombre positif non nul : ")

    return int(reponse_utilisateur)


# Permet de controler si la réponse utilisateur est H, F ou I
def ctrl_valeur_sexe(reponse):
    reponse_correct = False
    # Tant que le controle n'est pas valide
    while reponse_correct is False:
        if reponse in {"H", "F", "I"}:
            reponse_correct = True
        # Si la réponse utilisateur est différente de H, F ou I
        else:
            reponse = input("Merci de saisir H, F ou I : ")

    return reponse
