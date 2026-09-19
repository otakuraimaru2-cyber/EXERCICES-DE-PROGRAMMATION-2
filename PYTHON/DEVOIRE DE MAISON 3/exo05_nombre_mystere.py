import random


NOMBRE_SECRET = random.randint(1, 1000)

coups = 0

trouve = False

print("🎲 --- JEU DU NOMBRE MYSTÈRE  ---")

print("Devine le nombre secret choisi par l'ordinateur !\n")

while not trouve:

 proposition = int(input("Entre ta proposition : "))

 coups += 1

 
 if proposition < NOMBRE_SECRET:
   print("C'est plus GRAND ! ⬆️\n")

 elif proposition > NOMBRE_SECRET:
   print("C'est plus PETIT ! ⬇️\n")

 else:
    if coups == 1:
        print(f"🎉 BINGO ! Tu as trouvé le nombre secret {NOMBRE_SECRET} en {coups} coup(s), tu es un devin ? 🏆 !")
    elif coups <=4:
        print(f"🎉 BINGO ! Tu as trouvé le nombre secret {NOMBRE_SECRET} en {coups} coup(s), tu es un génie 🏆 !")
    elif coups <= 7:
        print(f"🎉 BINGO ! Tu as trouvé le nombre secret {NOMBRE_SECRET} en {coups} coup(s), tu es très fort !")
    elif coups <= 10:
        print(f"🎉 BINGO ! Tu as trouvé le nombre secret {NOMBRE_SECRET} en {coups} coup(s), bien joué !")
    elif coups > 10:
        print(f"🎉 BINGO ! Tu as trouvé le nombre secret {NOMBRE_SECRET} en {coups} coup(s), pas mal !")
    trouve = True