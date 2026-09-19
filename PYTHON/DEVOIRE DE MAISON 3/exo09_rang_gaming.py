
def determiner_rang(score):

 if score >= 2000:
  return "🏆 Rang Maître Suprême"

 elif score >= 1500:
  return "💎 Rang Diamant"

 elif score >= 1000:
  return "🥇 Rang Or"

 elif score >= 500:
  return "🥈 Rang Argent"

 else:
  return "🥉 Rang Bronze"

print("🎮 --- SYSTÈME DE CLASSEMENT E-SPORT ---")

print("VOICIE LE BAREMME")

for score in [250, 800, 1200, 1900, 2500] :

    RANG  = determiner_rang(score)
    print(RANG)

score_joueur = int(input("\nQuel est ton score de saison ? "))

rang_obtenu = determiner_rang(score_joueur)

print("\n" + "=" * 40)

print(f"Score enregistré : {score_joueur} points")

print(f"Statut officiel : {rang_obtenu}")

print("========================================")