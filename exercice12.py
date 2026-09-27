# L'énoncé de l'exercice
'''Écrire un programme Python qui demande à l'utilisateur de saisir un nombre entier composé exactement de 3 chiffres (par exemple : 385).
Le programme doit effectuer les traitements suivants :
Décomposition : Extraire le chiffre des centaines, des dizaines et des unités en utilisant uniquement des opérations mathématiques (// et %).
Calcul : Calculer la somme de ces trois chiffres.
Inversion (Casting) : Reconstituer le nombre inversé sous forme de chaîne de caractères (str), puis le convertir en un nombre entier (int).. '''
# la solution corrigée de l'exercice
nombre_entier = int(input('Veuillez entrer un nombre entier composé exactement de 3 chiffres : '))
# Décomposition
temporaire = nombre_entier
chiffre_unites = temporaire % 10
temporaire //= 10
chiffre_dizaines = temporaire % 10
temporaire //= 10
chiffre_centaines = temporaire
# la somme de ces trois chiffres
somme_chiffres = chiffre_unites + chiffre_dizaines + chiffre_centaines
# Inversion (Casting)
temporaire = str(chiffre_unites) + str(chiffre_dizaines) + str(chiffre_centaines)
temporaire = int(temporaire)
# Affichage
print('La somme de ces trois chiffres est :', somme_chiffres)
print("L'inverse de", nombre_entier, "est :", temporaire)
print('Le type du nombre inversé est :', type(temporaire))