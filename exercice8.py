# L'énoncé de l'exercice
'''Ecrire un programme qui demande à l'utilisateur de saisir 2 entiers A et B,
qui échange le contenu des variables A et B puis qui affiche A et B.'''
# la solution corrigée de l'exercice
A = int(input('Veuillez entrer la valeur de A : '))
B = int(input('Veuillez entrer la valeur de B : '))
print('Avant la permutation : A =', A, 'et B =', B)
A, B = B, A
print('Après la permutation : A =', A, 'et B =', B)