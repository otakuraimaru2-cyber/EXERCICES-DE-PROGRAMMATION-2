
AGE_REQUIS = 15

SCORE_REQUIS = 1000


print("🎟️ --- CONTRÔLE D'ACCÈS AU SALON VIP ESPORT ---")

print("-" * 50)

pseudo = input("Pseudo du joueur : ")

age = int(input("Quel est ton âge ? "))

score = int(input("Quel est ton score compétitif ? "))

MDP_SECRET = input("Mot de passe secret (si tu en as un) : ")

print(" " + "=" * 45)

if age >= (AGE_REQUIS and score >= SCORE_REQUIS) or MDP_SECRET == "OTAKU":

 print(f"👑 ACCÈS VIP ACCORDÉ pour {pseudo} !")
 print(f"Critères validés : {age} ans (>= {AGE_REQUIS}) et {score} pts (>= {SCORE_REQUIS}).")
 print("Bienvenue dans le carré des champions 🏆 !")


elif age < AGE_REQUIS and score < SCORE_REQUIS:

 print(f"⛔ ACCÈS REFUSÉ pour {pseudo}.")
 print(f"Motif : Âge insuffisant ({age}/{AGE_REQUIS} ans) ET score insuffisant ({score}/{SCORE_REQUIS} pts).")


elif age < AGE_REQUIS:

 print(f"⛔ ACCÈS REFUSÉ pour {pseudo}.")
 print(f"Motif : Ton score est bon ({score} pts), mais tu dois avoir au moins {AGE_REQUIS} ans.")

else:

 pts_manquants = SCORE_REQUIS - score
 print(f"⛔ ACCÈS REFUSÉ pour {pseudo}.")
 print(f"Motif : Ton âge est bon ({age} ans), mais il te manque encore {pts_manquants} pts au classement.")

print("=" * 45)