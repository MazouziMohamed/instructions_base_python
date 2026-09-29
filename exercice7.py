# L'énoncé de l'exercice
'''Écrire un programme qui demande à l'utilisateur de taper
le rayon d'une sphère, puis calcule et affiche son volume.'''
# la solution corrigée de l'exercice
from math import pi
rayon_sphere = float(input('Veuillez entrer le rayon de la sphère : '))
volume_sphere = (4 * pi * (rayon_sphere ** 3)) / 3
print(f"Le volume de la sphère est : {volume_sphere}")
