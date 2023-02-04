
def ctrl_valeur_menu(menu_max, reponse_menu):
    reponse_correct = 0

    # Tant que le controle n'est pas valide
    while reponse_correct == 0:
        try:
            # Vérifie si reponse_menu est un entier
            int(reponse_menu)
            # Met le string en integer
            reponse_menu = int(reponse_menu)
            # Vérifie que reponse_menu est compris entre 1 et 3
            if 1 <= reponse_menu <= menu_max:
                # Valide le controle pour sortir de la boucle
                reponse_correct = 1
            else:
                # Si reponse_menu n'est pas compris entre 1 et 3
                reponse_menu = input("Merci de choisir un menu existant : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_menu = input("Merci de choisir un menu existant : ")
    return int(reponse_menu)

def ctrl_valeur_utilisateur(reponse_utilisateur):
    reponse_correct = False

    # Tant que le controle n'est pas valide
    while reponse_correct is False:
        try:
            # Vérifie si reponse_utilisateur est un entier
            int(reponse_utilisateur)
            # Met le string en integer
            reponse_utilisateur = int(reponse_utilisateur)
            # Vérifie que reponse_menu est positif
            if 1 <= reponse_utilisateur:
                # Valide le controle pour sortir de la boucle
                reponse_correct = True
            else:
                # Si reponse_menu n'est pas compris entre 1 et 3
                reponse_utilisateur = input("Merci de choisir un nombre positif non nul : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_utilisateur = input("Merci de choisir un nombre positif non nul : ")

    return int(reponse_utilisateur)