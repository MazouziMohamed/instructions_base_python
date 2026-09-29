# L'énoncé de l'exercice
'''Ecrire un programme qui calcule et affiche la distance entre deux points
A et B du plan dont les coordonnées (X_A, Y_A) et (X_B, Y_B) sont entrées
au clavier comme des réels'''
# la solution corrigée de l'exercice
from math import sqrt
XA = float(input("Veuillez entrer L'abscisse du point A : "))
YA = float(input("Veuillez entrer L'ordonnée du point A : "))
XB = float(input("Veuillez entrer L'abscisse du point B : "))
YB = float(input("Veuillez entrer L'ordonnée du point B : "))
AB = sqrt((YB - YA)**2 + (XB - XA)**2)
print(f"La distance entre A et B est : {AB}")
