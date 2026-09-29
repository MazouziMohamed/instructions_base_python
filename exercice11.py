# L'énoncé de l'exercice
'''Ecrire un programme qui affiche la résistance équivalente à trois
résistances R1, R2, R3 : si les résistances sont branchées en série.
si les résistances sont branchées en parallèle. '''
# la solution corrigée de l'exercice
R1 = float(input('Veuillez entrer la valeur de la première résistance : '))
R2 = float(input('Veuillez entrer la valeur de la deuxième résistance : '))
R3 = float(input('Veuillez entrer la valeur de la troisième résistance : '))
resistance_equivalente_serie = R1 + R2 + R3
resistance_equivalente_parallele = (R1 * R2 * R3) / (R2*R3 + R1*R3 + R1*R2)
print(f"La résistance équivalente si les résistances sont branchées en série est : {resistance_equivalente_serie}")
print(f"La résistance équivalente si les résistances sont branchées en parallèle est : {resistance_equivalente_parallele}")
