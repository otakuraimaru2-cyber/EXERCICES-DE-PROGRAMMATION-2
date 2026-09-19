
MDP = "python2026"

MDP_par_defaut = "admin"

print("🔒 --- SYSTÈME DE SÉCURITÉ DU BUNKER ---")

print("-" * 45)

saisie_utilisateur = input("Entre le mot de passe d'accès : ").lower()

print(" " + "=" * 40)


if saisie_utilisateur == MDP or saisie_utilisateur == MDP_par_defaut:

 print("🟢 ACCÈS CONFIRMÉ : Porte blindée déverrouillée !")

 print("Bienvenue dans le centre de contrôle secret 🛡️.")
else:
 print("🔴 ALERTE INTRUSION : Mot de passe incorrect !")

 print("Le protocole d'autodéfense a été activé 🚨.")
 
print("=" * 40)