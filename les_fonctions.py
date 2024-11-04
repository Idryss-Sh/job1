# Job 1
def My_prints_hello(): # Crée une fonction qui imprime "Hello World"
    print ("Hello World")

# Job 2
def My_print_name(Name): # Crée une fonction qui imprime "
    print (Name)
My_print_name("Alice") # Appelle la fonction pour imprimer "Alice"
My_print_name("Bob")
My_print_name("Charlie")
My_print_name("Diane")

# Job 3
def add(num1, num2): # Crée une fonction qui additionne deux nombres
    somme = num1 + num2 # Calcul la somme
    print(f"La somme de {num1} et {num2} est {somme}") # Imprime la somme
add(3, 5) # Appelle la fonction pour additionner 3 et 5
add(10, 20)
add(7, 8)
add(15, 25)

# Job 4
def GetHello(): # Crée une fonction qui renvoie "Hello World"
    return "Hello la Plateforme"
message = GetHello() # Appelle la fonction pour stocker le résultat dans la variable "message"
print(message) # Imprime le résultat

# Job 5
def calcule(num1, operator, num2): # Crée une fonction qui additionne deux nombres et renvoie la somme
    if operator == "+": # Vérifie si l'opérateur est "+"
        return num1 + num2 # Retourne la somme
    elif operator == "-": # Vérifie si l'opérateur est "-"
        return num1 - num2 # Retourne la différence
    elif operator == "*": # Vérifie si l'opérateur est "*"
        return num1 * num2 # Retourne le produit
    elif operator == "/": # Vérifie si l'opérateur est "/"
        return num1 / num2 # Retourne
    elif operator == "%": # Vérifie si l'opérateur est
        return num1 % num2 # Retourne
    else:
            return "Opérateur invalide"
print(calcule(10, "+", 5)) # Affiche 15
print(calcule(10, "-", 5)) # Affiche 5
print(calcule(10, "*", 5)) # Affiche 50
print(calcule(10, "/", 5)) # Affiche 2.0
print(calcule(10, "%", 5)) # Affiche 0
print(calcule(10, "^", 5)) # Affiche "Opérateur invalide"

# Job 6
def verifier_positive(nombre): # Crée une fonction qui vérifie si un nombre est positif
    if nombre > 0: # Vérifie si le nombre est supérieur à zéro
        print(f"{nombre} est positif") # Imprime "nombre est positif"
    elif nombre < 0: # Vérifie si le nombre est inférieur à zéro
        print(f"{nombre} est négatif") # Imprime "nombre est négatif"
verifier_positive(10) # Appelle la fonction pour vérifier si 10 est positif
verifier_positive(-5)
verifier_positive(0)
verifier_positive(7)
verifier_positive(-12)

# Job 7
def identifier_developpeur(language):
    if language == "JavaScript":
        print("tu es développeur web")
    elif language == "Python":
        print("tu es développeur IA")
    elif language == "Java":
        print("tu es développeur logiciel")
    elif language == "reactjs":
        print("tu es développeur mobile")
    else:
        print("un jour, je serais le meilleur développeur")

identifier_developpeur("JavaScript")
identifier_developpeur("Python")
identifier_developpeur("Java")
identifier_developpeur("reactjs")

# Job 8
def affichier_produits(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Type ou saison invalide")
affichier_produits("fruit", "hivert") # Appel de la fonction
affichier_produits("fruit", "été")
affichier_produits("légume", "hivert")
affichier_produits("légume", "été")
affichier_produits("fruit", "printemps") # Exemple invalide

# Job 9
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Exemple d'appels de la fonction avec différents paramètres
print(moyenne(15, 18, 20))  # Affiche 17.666666666666668
print(moyenne(10, 12, 14))  # Affiche 12.0
print(moyenne(7, 8, 9))     # Affiche 8.0

# Job 10
def verifier_parite(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        print("Veuillez entrer un nombre entier positif.")
        return
    if nombre % 2 == 0:
        print(f"{nombre} est un nombre pair.")
    else:
        print(f"{nombre} est un nombre impair.")
verifier_parite(10)
verifier_parite(7)
verifier_parite(0)
verifier_parite(-3)
verifier_parite(14.5)

# Job 11
def time_to_text(minutes):
    heures = minutes // 60
    minutes_restants = minutes % 60
    print(f"{heures} heures et {minutes_restants} minutes")
time_to_text(125)
time_to_text(90)
time_to_text(45)
time_to_text(180)

# Job 12
def inverser_string(chaine):
    return chaine[::-1]

print(inverser_string("nikana"))  # Affiche "anakin"
print(inverser_string("Bonjour"))  # Affiche "roujonB"
print(inverser_string("Python"))  # Affiche "nohtyP"
print(inverser_string("Hello World"))  # Affiche "dlroW olleH"