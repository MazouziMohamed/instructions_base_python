# L'énoncé de l'exercice
'''Ecrire un programme qui demande le nom et l'âge d'un étudiant à l'université
et afficher "Bonjour ..., tu as ... ans et bienvenue à l'université" en remplaçant
les ... par, respectivement le nom et l'âge.'''
# la solution corrigée de l'exercice
nom_etudiant = input("Veuillez entrer votre nom : ")
age_etudiant = int(input("Veuillez entrer votre âge : "))
print("Bonjour " + nom_etudiant + ", tu as", age_etudiant, "ans et bienvenue à l'université.")