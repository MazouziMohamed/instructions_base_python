# L'énoncé de l'exercice
'''Ecrire un programme qui demande à l'utilisateur de taper la largeur et la
longueur d'un rectangle et qui en affiche le périmètre et la surface.'''
# la solution corrigée de l'exercice
largeur_rectangle = float(input('Veuillez entrer la largeur du rectangle : '))
longueur_rectangle = float(input('Veuillez entrer la longueur du rectangle : '))
surface_rectangle = largeur_rectangle * longueur_rectangle
perimetre_rectangle = 2 * (largeur_rectangle + longueur_rectangle)
print(f"La surface du rectangle est : {surface_rectangle}")
print(f"Le périmètre du rectangle est : {perimetre_rectangle}")
