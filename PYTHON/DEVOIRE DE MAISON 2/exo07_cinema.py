
TARIF_PLEIN = 11.50

TARIF_REDUIT = 6.00

print("🎬 --- BILLETTERIE CINÉMA MÉGA-STAR ---")

print("-" * 45)

age = int(input("Quel est ton âge ? "))

reponse_pass = input("As-tu un pass jeune ou une carte abonné (oui/non) ? ").lower()

a_un_pass = (reponse_pass == "oui")

seance = input("Quelle séance souhaites-tu (matinée ou soirée) ? ").lower()

print(" " + "=" * 40)

if seance == "matinée":

 print("🎟️ TARIF MATINÉE APPLIQUÉ : 5.00 €.")

elif seance == "soirée":

 if age < 18 or a_un_pass:

  economie = TARIF_PLEIN - TARIF_REDUIT

  print("🎉 TARIF RÉDUIT ACCORDÉ !")

  if age < 18 and a_un_pass:
   print(f"Motif : Tu as {age} ans (< 18) ET tu possèdes un pass jeune.")


  elif age < 18:
   print(f"Motif : Moins de 18 ans ({age} ans).")


  else:

   print("Motif : Titulaire du pass jeune officiel.")

  print(f"Prix de ton billet : {TARIF_REDUIT:.2f} € (au lieu de {TARIF_PLEIN:.2f} €).")
  print(f"Économie réalisée : {economie:.2f} € !")


 else:

  print("🎟️ PLEIN TARIF APPLIQUÉ.")
  print(f"Prix de ton billet : {TARIF_PLEIN:.2f} €.")
  print("Conseil : Souscris au pass jeune pour payer seulement 6.00 € la prochaine fois !")

print("=" * 40)