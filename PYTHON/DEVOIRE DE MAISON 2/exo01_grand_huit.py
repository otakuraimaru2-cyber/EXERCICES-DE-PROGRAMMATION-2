
print(" 🎢 --- ENTRÉE DU GRAND HUIT GALACTIQUE 🎢 ---")
print("-" * 45)

prenom = input("Comment t'appelles-tu ? ")

taille_cm = int(input("Quelle est ta taille en cm ? "))

age = int(input("Quel âge as-tu ? "))

AGE_MINIMALE = 10

TAILLE_MINIMALE = 140

print(" " + "=" * 40)

print(" ")

if taille_cm >= TAILLE_MINIMALE and age >= AGE_MINIMALE:

 print(f"✅ ACCÈS AUTORISÉ pour {prenom} !")

 print(f"Tu mesures {taille_cm} cm (minimum requis : {TAILLE_MINIMALE} cm) et tu as {age} ans (minimum requis : {AGE_MINIMALE} ans).")

 print("Installe-toi au premier rang et prépare-toi au grand saut 🚀 !")
 
else:
 cm_manquants = TAILLE_MINIMALE - taille_cm

 age_manquant = AGE_MINIMALE - age

 print(f"⛔ ACCÈS REFUSÉ pour {prenom}.")

 if taille_cm < TAILLE_MINIMALE and age < AGE_MINIMALE:

  print(f"Tu mesures {taille_cm} cm et tu as {age} ans. Il te manque encore {cm_manquants} cm et {age_manquant} ans pour monter.")

  print(f"Reviens dans {age_manquant} ans et quand tu auras grandi de {cm_manquants} cm, tu pourras retenter ta chance !")

 elif taille_cm < TAILLE_MINIMALE:

  print(f"Tu mesures {taille_cm} cm. Il te manque encore {cm_manquants} cm pour monter.")

  print(f"Reviens très bientôt quand tu auras grandi de {cm_manquants} cm !")
 
 else:
    print(f"Tu as {age} ans. Il te manque encore {age_manquant} ans pour monter.")
    
    print(f"Reviens dans {age_manquant} ans et tu pourras retenter ta chance !")