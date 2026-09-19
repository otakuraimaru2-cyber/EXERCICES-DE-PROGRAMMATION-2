
def afficher_etat(pv_h, pv_b):
 print(f"\n💙 Héros : {pv_h} PV | 👹 Boss Golem : {max(0, pv_b)} PV")

print("⚔️ ======================================== ⚔️")
print(" DUEL ÉPIQUE : HÉROS vs GOLEM DE PIERRE ")
print("⚔️ ======================================== ⚔️")

pv_heros = 60
pv_boss = 80

sorts = ["Coup d'épée (18 dgts)", "Éclair magique (25 dgts)", "Potion de soin (+20 PV)" ,"attaque ultime(40 dgts)"]
tour = 0
while pv_heros > 0 and pv_boss > 0:
 tour += 1

 print(f"\n--- TOUR {tour} ---")

 afficher_etat(pv_heros, pv_boss)
 
 print("\nActions disponibles :")

 for idx, s in enumerate(sorts, start=1):
  print(f" {idx}. {s}")
 
 choix = input("\nTon action (1-4) : ").strip()
 
 
 if choix == "1":
  degats = 18
  pv_boss -= degats
  print(f"🗡️ Coup d'épée précis ! Tu infliges {degats} dégâts au Boss !")

 elif choix == "2":
  degats = 25
  pv_boss -= degats
  print(f"⚡ Éclair magique foudroyant ! Tu infliges {degats} dégâts au Boss !")

 elif choix == "3":
  soin = 20
  pv_heros += soin
  print(f"🧪 Tu bois une potion magique et récupères +{soin} PV !")
  
 elif choix == "4" :
    import random
    chance = random.randint(0,100)
    if chance < 50 :
     degats = 40
     pv_boss -= degats
     print(f" bravo tu as reussie a utiliser ton attaque ultime ⚔ ! Tu infliges {degats} dégâts au Boss !")
    
    else :
        print("❌ Action manquée !")

 else:
  print("❌ Action manquée ! Tu hésites et perds ton tour !")
 
 
 if pv_boss > 0:
  degats_boss = random.randint(0,50)
  pv_heros -= degats_boss
  print(f"💥 Le Golem frappe le sol et t'inflige {degats_boss} dégâts !")


print("\n" + "=" * 45)

if pv_boss <= 0:
 print("🏆 VICTOIRE LÉGENDAIRE !")
 print("Le Golem de Pierre s'effondre en morceaux ! Tu gagnes 500 XP !")

else:
 print("💀 DÉFAITE...")
 print("Tes points de vie sont tombés à 0. Recommence pour prendre ta revanche !")

print("=" * 45)