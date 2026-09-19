
TRESORS_DISPONIBLES = [
 "Épée de Diamant (Légendaire 🌟)",
 "Bouclier d'Or (Épique 🛡️)",
 "Arc des Tempêtes (Rare 🏹)",
 "Armure de Dragon (Légendaire 🐉)",
 "Bague de Vitesse (Rare 💍)",
 "Potion de Force Suprême (Commun 🧪)"
]
def afficher_menu(jetons_restants):
 print(f"\n--- MENU DE LA BOUTIQUE (Jetons restants : {jetons_restants} 🪙) ---")
 print("1. Ouvrir un coffre mystère (Coût : 1 jeton)")
 print("2. Voir mon inventaire de butin")
 print("3. Voir la liste de tous les trésors du jeu")
 print("4. Quitter la boutique")


def afficher_inventaire(inventaire):
 print("\n" + "=" * 45)
 print(f"🎒 INVENTAIRE DU HÉROS ({len(inventaire)} objet(s) collecté(s)) :")
 if len(inventaire) == 0:
  print(" (Ton inventaire est vide pour le moment)")

 else:
  for idx, item in enumerate(inventaire, start=1):
   print(f" {idx}. {item}")
   print("=" * 45)

print("🎁 ======================================== 🎁")
print(" BOUTIQUE DES COFFRES MYSTÈRES v1.0 ")
print("🎁 ======================================== 🎁")
import random
mon_inventaire = []
jetons = random.randint(1,5)
compteur_tirage = 0

while True:
 afficher_menu(jetons)
 choix = input("\nTon choix (1-4) : ").strip()
 
 if choix == "1":
   if jetons > 0:
     jetons -= 1

     tresor_gagne = TRESORS_DISPONIBLES[compteur_tirage %
len(TRESORS_DISPONIBLES)]
     compteur_tirage += 1
 
     print("\n✨ Ouvertuuuuure du coffre en cours...")
     print(f"🎉 FÉLICITATIONS ! Tu obtiens : [ {tresor_gagne} ] !")
     mon_inventaire.append(tresor_gagne)
     print("-> L'objet a été rangé dans ton inventaire !")
   else:
      print("\n❌ Tu n'as plus de jetons ! Reviens demain pour en récupérer !")
 
 elif choix == "2":
   afficher_inventaire(mon_inventaire)
 
 elif choix == "3":
  print("\n📜 LISTE DES OBJETS DU JEU :")
  for t in TRESORS_DISPONIBLES:
   print(f" • {t}")
 
 elif choix == "4":
  print("\n👋 Merci d'avoir visité la Boutique des Coffres Mystères ! Bon jeu !")
  break

 else:
  print("❌ Choix invalide ! Tape 1, 2, 3 ou 4.")