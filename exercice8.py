# L'énoncé de l'exercice
'''Ecrire un programme qui demande à l'utilisateur de saisir 2 réels A et B,
qui échange le contenu des variables A et B puis qui affiche A et B.'''
# la solution corrigée de l'exercice
A = float(input('Veuillez entrer la valeur de A : '))
B = float(input('Veuillez entrer la valeur de B : '))
print(f"Avant la permutation : A = {A} et B = {B}")
A, B = B, A
print(f"Après la permutation : A = {A} et B = {B}")
