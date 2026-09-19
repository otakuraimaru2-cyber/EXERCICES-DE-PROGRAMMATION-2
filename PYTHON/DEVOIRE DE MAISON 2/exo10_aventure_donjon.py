
print("🏰 --- L'ÉPOPÉE DU DONJON MAUDIT ---")

print("Une aventure interactive dont tu es le seul maître !")

(" " + "=" * 55)


pseudo = input("Nom de ton héros / héroïne : ")

classe = input("Choisis ta classe (Guerrier / Mage / Voleur ...) : ").lower()

print(f"Bienvenue, noble {pseudo} le {classe.capitalize()} !")

print("Tu pénètres dans une crypte antique. Trois chemins s'offrent à toi :")

print(" [1] La Porte de Cristal bleu (scellée par une énigme)")

print(" [2] L'Antre du Dragon rouge (chaleur étouffante)")

print(" [3] Le Pont Suspendu (au-dessus d'un gouffre sans fond)")

choix_porte = int(input("Quel chemin oses-tu emprunter (1, 2 ou 3) ? "))

print(" " + "=" * 45)


if choix_porte == 1:

 print("Une statue de pierre géante s'anime et résonne :")
 print("« Voyageur, résous ce calcul mental : Combien vaut 8 multiplié par 7 ? »")
 reponse_enigme = int(input("Ta réponse : "))

 
 if reponse_enigme == 56:

    print("✨ ÉCLATANT ! La porte s'ouvre sur une salle pleine de diamants !")
    print(f"🏆 VICTOIRE MAJESTUEUSE : {pseudo} repart riche et célèbre !")

  
 else:

  print("⚡ ERREUR ! Une trappe s'ouvre sous tes pieds... Tu glisses dehors !")
  print("🚪 Défaite : Tu es expulsé du donjon, sain et sauf mais les mains vides.")


elif choix_porte == 2:

 print("Un immense Dragon Écarlate dort sur une montagne de pièces d'or.")
 action = input("Que fais-tu (attaquer / discret / fuir) ? ").lower()

 
 if action == "discret" and (classe == "voleur" or classe == "mage"):

    print(f"🤫 Grâce à ton agilité de {classe}, tu dérobes 1000 pièces d'or sans bruit !")
    print("🏆 VICTOIRE FURTIVE : Un véritable coup de maître !")


 elif action == "attaquer" and classe == "guerrier":

  print(f"⚔️ Avec ta force herculéenne, tu terrasses le monstre dans un duel héroïque !")
  print(f"🏆 VICTOIRE LÉGENDAIRE : {pseudo} devient le Protecteur du Royaume !")


 elif action == "fuir":

  print("🏃 Prudent, tu fais demi-tour à pas de loup. Mieux vaut vivre pour rejouer !")


 else:
  print("🔥 Mauvais choix ! Le dragon se réveille et souffle une vague de feu !")
  print("💀 DÉFAITE : Tu t'enfuis en courant avec tes vêtements roussis !")


elif choix_porte == 3:

 print("Le pont de corde oscille dangereusement au-dessus du vide.")
 decision = input("Avances-tu en 'courant' ou à 'taton' ? ").lower()

 
 if decision == "taton":

  print("🌉 Pas à pas, tu atteins l'autre rive et découvres le Graal d'Émeraude !")
  print("🏆 VICTOIRE : La patience est la plus grande des vertus !")


 else:

  print("💥 Une planche craque ! Tu t'accroches in extremis à une liane et remontes.")
  print("🚪 Fin de partie : Tu as sauvé ta peau de justesse !")

else:

 print("❌ Choix invalide ! Pris de panique, tu fais demi-tour et quittes le donjon.")


print("=" * 45)

print(f"Merci d'avoir joué, {pseudo} ! Relance le script pour explorer d'autres destins !")