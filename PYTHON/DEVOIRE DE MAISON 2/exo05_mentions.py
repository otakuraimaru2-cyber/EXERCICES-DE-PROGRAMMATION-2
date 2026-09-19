
print("🎓 --- CALCULATEUR DE MENTION OFFICIELLE ---")

print("-" * 45)

note = float(input("Entre ta note d'examen (sur 20) : "))

print(" " + "=" * 40)

if note < 0 or note > 20:

 print("❌ ERREUR : La note doit être comprise entre 0 et 20 !")


elif note == 20.0:

    print(f"Note obtenue : {note:.2f} / 20")
    print("🏆 RÉSULTAT : Mention Exellent !")
    print("Félicitations, tu as atteint la perfection absolut !")


elif note >= 16.0:

 print(f"Note obtenue : {note:.2f} / 20")
 print("🏅 RÉSULTAT : Mention Très Bien !")
 print("Félicitations exceptionnelles du jury !")


elif note >= 14.0:

 print(f"Note obtenue : {note:.2f} / 20")
 print("🌟 RÉSULTAT : Mention Bien !")
 print("Très bon travail, continue sur cette lancée !")


elif note >= 12.0:

 print(f"Note obtenue : {note:.2f} / 20")
 print("👍 RÉSULTAT : Mention Assez Bien !")
 print("Travail satisfaisant et régulier.")


elif note >= 10.0:

 print(f"Note obtenue : {note:.2f} / 20")
 print("🎯 RÉSULTAT : Admis (Mention Passable) !")
 print("Examen réussi, l'objectif est atteint !")


else:

 print(f"Note obtenue : {note:.2f} / 20")
 print("📚 RÉSULTAT : Non admis (Insuffisant).")
 print("Ne te décourage pas, persévère dans tes révisions !")

print("=" * 40)