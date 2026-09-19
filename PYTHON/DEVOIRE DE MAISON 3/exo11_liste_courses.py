
panier = []

print("🛒 --- CRÉATEUR DE LISTE DE SHOPPING ---\n")

while True:
 article = input("Article à ajouter (ou 'fin' pour terminer) : ").strip()
 
 if article.lower() == "fin":
  break

 elif article != "":
  panier.append(article)
  print(f"-> '{article}' ajouté au panier !\n")

 elif article in panier :
  print("article deja dans le panier")

print("\n" + "=" * 40)

print(f"RÉCAPITULATIF DE TON PANIER ({len(panier)} articles) :")

for idx, item in enumerate(panier, start=1):

 print(f"{idx}. {item}")

print("========================================")