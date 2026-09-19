
print("🕹️ --- GRAND QUIZ DE CULTURE GEEK & JEUX VIDÉO ---")
print("Réponds aux 5 questions pour tester tes connaissances !")
print("-" * 50)
score = 0

q1 = input("1. Quel est le héros vêtu de vert dans Zelda (ce n'est pas Zelda !) ? ").lower()

if q1 == "link":

 print("✅ Bonne réponse ! C'est bien Link ! (+1 point)")
 score += 1

else:

 print("❌ Raté ! C'était Link (Zelda est la princesse) !")


q2 = input("2. Quel studio a créé le jeu Minecraft (Mojang / Epic / Nintendo) ? ").lower()

if q2 == "mojang":

 print("✅ Excellent ! Mojang a créé Minecraft en 2009 ! (+1 point)")
 score += 1

else:
 print("❌ Faux ! C'était le studio Mojang !")



q3 = input("3. Dans Pokémon, quel est le type élémentaire de Pikachu ? ").lower()

if q3 == "electrik" or q3 == "electrique" or q3 == "electricite":

 print("✅ Parfait ! Pikachu est de type Électrik ! (+1 point)")
 score += 1

else:
 print("❌ Dommage ! Pikachu est de type Électrik !")


q4 = input("3. Dans genshin impact quel est le nom commun des joueur dans l'istoire  ? ").lower()


if q4 == "le voyageur":

 print("✅ Parfait ! c'est le voyageur ! (+1 point)")
 score += 1

else:
 print("❌ Dommage ! c'etait le voyageur !")


q5 = input("3. dans fortnite comment s'apelle le hero  ? ").lower()


if q4 == "jonesy":

 print("✅ Parfait ! le hero de fortnite s'appelle jonesy ! (+1 point)")
 score += 1

else:
 print("❌ Dommage ! c'etait jonesy !")


print("=" * 45)

print(f"🎯 BILAN FINAL DU QUIZ : {score} / 5 points")

if score == 5:
 print("🏆 RANG : MAÎTRE ABSOLU DU GAMING ! Un score parfait !")


elif score == 4:
 print("🌟 RANG : JOUEUR PLATINE !NIVEAU INTERNATIONAL ")


elif score == 3:
 print("👍 RANG :JOUEUR OR  ! UN GRAN JOUEUR AU NIVEAU NATIONAL !")


elif score == 2:
 print("👍 RANG : JOUEUR ARGENT ! tu maitrise parfaitement tes bases, continue !")


elif score == 1:
 print("👍 RANG : JOUEUR BRONZE ! De bonnes bases, continue !")


else:
 print("📚 RANG : DÉBUTANT ! Rejoue pour améliorer ton score !")


print("=" * 4)