# L'énoncé de l'exercice
'''Écrire un programme qui demande un temps T (entier) exprimé en secondes,
et qui le convertit en heures, minutes, secondes.'''
# la solution corrigée de l'exercice
temps_secondes = int(input('Veuillez entrer un nombre entier de secondes : '))
temporaire = temps_secondes
heures = temporaire // 3600
temporaire %= 3600
minutes = temporaire // 60
temporaire %= 60
secondes = temporaire
print(temps_secondes, 'secondes =', heures, 'heures', minutes, 'minutes', secondes, 'secondes')