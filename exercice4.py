# L'énoncé de l'exercice
'''Ecrire un programme qui demande à l'utilisateur de saisir deux réels X et Y,
et qui affiche la puissance X^Y.'''
# la solution corrigée de l'exercice
base = float(input('Veuillez entrer la base : '))
exposant = float(input('Veuillez entrer l\'exposant : '))
print(f"{base} à la puissance {exposant} est égale à {base ** exposant}")
