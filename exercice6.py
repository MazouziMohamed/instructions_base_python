# L'énoncé de l'exercice
'''Ecrire un programme qui demande à l'utilisateur de taper 5 notes et qui
affiche leur somme et leur moyenne.'''
# la solution corrigée de l'exercice
note1 = float(input('Veuillez entrer la première note : '))
note2 = float(input('Veuillez entrer la deuxième note : '))
note3 = float(input('Veuillez entrer la troisième note : '))
note4 = float(input('Veuillez entrer la quatrième note : '))
note5 = float(input('Veuillez entrer la cinquième note : '))
somme_notes = note1 + note2 + note3 + note4 + note5
moyenne_notes = somme_notes / 5
print('La somme des notes est :', somme_notes)
print('La moyenne des notes est :', moyenne_notes)