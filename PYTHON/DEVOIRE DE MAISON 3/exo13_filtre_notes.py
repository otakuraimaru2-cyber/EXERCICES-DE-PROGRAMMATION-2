
def filtrer_notes(notes, seuil):
 
 bonnes_notes = []
 for note in notes:
   if note >= seuil:
     bonnes_notes.append(note)
 return bonnes_notes

toutes_les_notes = [15, 12, 18, 9, 14, 16, 11, 20]

SEUIL_HONNEUR = 14.0


selection = filtrer_notes(toutes_les_notes, SEUIL_HONNEUR)
moyenne_bonne_note = sum(selection) / len(selection)

print("🎓 --- SÉLECTEUR DE NOTES POUR LE TABLEAU D'HONNEUR ---")

print(f"Toutes les notes de la classe : {toutes_les_notes}")

print(f"Seuil de sélection : >= {SEUIL_HONNEUR} / 20\n")

print("=" * 40)

print(f"Notes qualifiées pour le Tableau d'Honneur ({len(selection)} notes) :")

for n in selection:
 print(f"\n• {n} / 20")

print(f"\nla moyenne des bonne note est : {moyenne_bonne_note}")

print("========================================")