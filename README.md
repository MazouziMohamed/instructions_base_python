# Instructions de Base en Python
Ce dépôt rassemble les solutions de **12 exercices pratiques** axés sur l'apprentissage des **instructions de base** en Python.

---

## Concepts couverts

- **Entrées / Sorties**
- **Types de données & Conversion (Casting)**
- **Opérations Arithmétiques**
- **Modules standards**
- **Logique & Algorithmes**

---

## Liste des Exercices

1. **Données Personnelles :** Lecture et affichage d'informations de base.
2. **Calcul d'Âge :** Détermination de l'âge à partir de l'année de naissance.
3. **Propriétés du Rectangle :** Calcul du périmètre et de la surface.
4. **Puissance :** Évaluation de la puissance $X^Y$.
5. **Opérations Élémentaires :** Calcul de la somme, différence, produit et quotient.
6. **Moyenne :** Calcul de la somme et de la moyenne de 5 notes.
7. **Volume d'une Sphère :** Application de la formule géométrique $V = \frac{4}{3}\pi r^3$.
8. **Échange de Variables :** Permutation de deux valeurs (`A, B = B, A`).
9. **Conversion Temporelle :** Transformation d'une durée en secondes vers heures, minutes et secondes.
10. **Distance Euclidienne :** Calcul de la distance entre deux points dans un plan 2D.
11. **Circuits Électriques :** Calcul de la résistance équivalente en série et en parallèle.
12. **Analyse Numérique :** Décomposition, somme des chiffres et inversion d'un nombre à trois chiffres.

---

## 📚 Résumé Pratique & Exemples

### 1. Entrées et Sorties (Input / Output)
* **`input()`** : Permet de récupérer la saisie de l'utilisateur.
  * *Exemple :* `nom = input("Entrez votre nom : ")`
* **`print()`** : Permet d'afficher un résultat à l'écran.
  * *Exemple :* `print("Bonjour")`
* **`f-string`** : Méthode propre pour intégrer des variables dans un texte.
  * *Exemple :* `print(f"Bonjour {nom}, tu as {age} ans.")`

### 2. Conversion des Types (Type Casting)
* **`int()`** : Convertit une valeur en nombre entier.
  * *Exemple :* `age = int(input("Votre âge : "))`
* **`float()`** : Convertit une valeur en nombre réel (décimal).
  * *Exemple :* `prix = float(input("Le prix : "))`
* **`str()`** : Convertit une valeur en chaîne de caractères (texte).
  * *Exemple :* `texte_age = str(25)`

### 3. Opérations Arithmétiques et Mathématiques
* **Opérations de base (`+`, `-`, `*`)** :
  * *Exemple :* `somme = 5 + 3`
* **Puissance (`**`)** :
  * *Exemple :* `carre = 4 ** 2` (donne 16)
* **Division et Reste (`/`, `//`, `%`)** :
  * Division classique `/` : `5 / 2` (donne `2.5`)
  * Division entière `//` : `5 // 2` (donne `2`)
  * Reste (Modulo) `%` : `5 % 2` (donne `1`)
* **Le module `math` (`pi`, `sqrt`)** :
  * *Exemple :* 
    ```python
    from math import pi, sqrt
    surface = pi * (r ** 2)
    racine = sqrt(16)  # donne 4.0
    ```

### 4. Astuces et Techniques Pythoniques (Pythonic Tricks)
* **Permutation rapide (Tuple Unpacking)** : Échanger deux variables instantanément.
  * *Exemple :* `A, B = B, A`
* **Utilisation d'une variable temporaire (`temporaire`)** : Garder la valeur d'origine intacte lors des calculs en chaîne.
  * *Exemple :* 
    ```python
    temp = 385
    unite = temp % 10
    temp //= 10
    ```

---

## Guide d'Exécution

### Prérequis
Python 3.10 ou une version supérieure.

### Installation et Lancement

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/MazouziMohamed/instructions_base_python_niveau1.git
