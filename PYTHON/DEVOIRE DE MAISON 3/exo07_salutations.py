
def saluer_joueur(pseudo, langue):

 langue = langue.lower()

 if langue == "fr":
    print(f"Bonjour {pseudo}, bienvenue dans l'arène 🇫🇷 !")

 elif langue == "en":
    print(f"Welcome {pseudo}, get ready to battle 🇬🇧 !")

 elif langue == "es":
    print(f"¡Hola {pseudo}, bienvenido a la arena 🇪🇸 !")

 elif langue == "jp" :
     print(f"Welcome {pseudo}, get ready to battle  !")

 else :
    print(f"Welcome {pseudo}, get ready to battle 🌐 !")
   
 

  
print("🌍 --- TEST DE LA FONCTION DE SALUTATIONS MULTILINGUE ---\n")


saluer_joueur("Leo", "fr")

saluer_joueur("ShadowKnight", "en")

saluer_joueur("Carlos", "es")

saluer_joueur("ayase", "jp")

saluer_joueur("PixelBot", "it")

