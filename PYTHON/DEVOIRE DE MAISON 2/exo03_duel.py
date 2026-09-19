
print("🎮 --- ARBITRE OFFICIEL DE DUEL GAMING ---")

print("-" * 45)

joueur1 = input("Pseudo du Joueur 1 : ")

score1 = int(input(f"Score de {joueur1} : "))

joueur2 = input("Pseudo du Joueur 2 : ")

score2 = int(input(f"Score de {joueur2} : "))

print(" " + "=" * 40)

if score1 > score2:
 ecart = score1 - score2
 print(f"🏆 VICTOIRE DE {joueur1.upper()} !")

 print(f"Score final : {score1} à {score2}.")

 if ecart >= 100:

  print(f"{joueur1} a demoli {joueur2} avec une avance de {ecart} points !")
 else:
    print(f"{joueur1} s'impose avec une avance de {ecart} points !")


elif score2 > score1:

 ecart = score2 - score1

 print(f"🏆 VICTOIRE DE {joueur2.upper()} !")

 print(f"Score final : {score2} à {score1}.")

 if ecart >= 100:
  print(f"{joueur2} a demoli {joueur1} avec une avance de {ecart} point !")
 else:
  print(f"{joueur2} s'impose avec une avance de {ecart} points !")
else:
 print("🤝 MATCH NUL ÉPIQUE !")

 print(f"Les deux joueurs terminent à égalité parfaite avec {score1} points chacun !")

print("=" * 40)