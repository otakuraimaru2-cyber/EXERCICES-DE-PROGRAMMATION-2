
sac = ["Épée en bois", "Bouclier", "Potion de soin", "Torche", "Corde"]

print("🎒 --- INVENTAIRE DU SAC À DOS RPG ---")

print(f"Nombre d'objets dans le sac : {len(sac)}")

print(f"• Premier objet équipé : {sac[0]}")

print(f"• Dernier objet rangé : {sac[-1]}")

print("\n⚡ ÉVÉNEMENT : Tu trouves un forgeron magique !")

sac[0] = "Épée légendaire de feu"
sac[3] = " Lanterne magique"

print("L'épée en bois est transformée en Épée légendaire de feu et la torche en  Lanterne magique !\n")

print("CONTENU ACTUEL DU SAC À DOS :")

for i in range(len(sac)):

 print(f"{i + 1}. {sac[i]}")
