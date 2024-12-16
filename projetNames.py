#un programme simple rédiger par Walid El Guelloly(moi) en tant que je suis un debutant dans la programmation notamment en language python
import time

def afficher_texte_lentement(texte, delai=0.05):
    for char in texte:
        print(char, end="", flush=True)
        time.sleep(delai)  
    print()  
texte = """Bienvenu(e) !
Ce programme est capable d'afficher différents noms d'utilisateurs et leurs âges sous forme de liste, comme on l'appelle en Python. 
De plus, il existe certaines fonctionnalités telles que : 
- Afficher le minumum des âges  
- Afficher le maximum des âges
- Afficher l'âge moyen"""
afficher_texte_lentement(texte, 0.05)
print("\033[1;34m----------------------\033[0m")
import time
def afficher_texte_lentement(texte, delai=0.1):
    for char in texte:
        print(char, end="", flush=True)
        time.sleep(delai)  
    print() 

list1 = []
ages = []
while True:
    import itertools
    for N in itertools.count() :
        afficher_texte_lentement(f"• Entrer le nom complet numero {N+1} : ", 0.05)
        NomComplet = input().capitalize() 
        
        afficher_texte_lentement(f"• Entrer l'âge de \033[32m{NomComplet}\033[0m : ", 0.05)
        Age = int(input())  
        ages.append(Age)

        afficher_texte_lentement("• Si vous souhaitez quitter, tapez 'fin' sinon, tapez entrer ↩ : ", 0.02)
        quit = input().lower() 

        ans = "ans"
        list1.append((NomComplet, f"{Age} {ans}"))

        if quit == "fin":
            afficher_texte_lentement("Fin de la saisie.", 0.05)

            print("\033[1;34m----------------------\033[0m")

            print(f"Votre liste finale est : {list1}",)

            print("\033[1;34m----------------------\033[0m")

            break
    if quit == "fin":
        break
#fonction de lage min
def minAge(ages):
    return min(ages)
if ages:
    Min = minAge(ages)
print("L'âge minimum est : ",Min, "ans")
#fonction de lage max
def maxAge(ages):
    return max(ages)
if ages:
    Max = maxAge(ages)
print("L'âge maximun est : ",Max, "ans")
#fonction de moyenne age
def moyenneAge(ages) :
    Totalages = sum(ages)
    moyenne = Totalages / len(ages)
    return moyenne
print(f"Le moyenne des âges est : {moyenneAge(ages):.2f}")