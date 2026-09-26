# L'énoncé de l'exercice
'''Ecrire un programme opérations qui calcule la somme, le produit, la
différence et la division de deux nombre réels.'''
# la solution corrigée de l'exercice
premier_reel = float(input('Veuillez entrer le premier réel : '))
deuxieme_reel = float(input('Veuillez entrer le deuxième réel : '))
print(premier_reel, '+', deuxieme_reel, '=', premier_reel + deuxieme_reel)
print(premier_reel, '-', deuxieme_reel, '=', premier_reel - deuxieme_reel)
print(premier_reel, '*', deuxieme_reel, '=', premier_reel * deuxieme_reel)
# Attention : La division par zéro est impossible
print(premier_reel, '/', deuxieme_reel, '=', premier_reel / deuxieme_reel)