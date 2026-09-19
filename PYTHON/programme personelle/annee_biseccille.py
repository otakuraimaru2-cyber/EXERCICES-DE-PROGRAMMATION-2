

continuer = "oui"

while continuer == "oui" :
 année = int(input("tapez une année "))

 if année > 2026 :

   if (année % 4 == 0 and année % 100 > 0)or ((année % 100 == 0) and (année % 400 == 0)):
     print("l'année sera bisecsile")

   else :
     print("cette année ne sera  pas bisecsile")

   if année > 1930 and ((année + 2 or année - 2) % 4 == 0) :
     print( " mais cette année il y aura  la coupe du monde")

 elif année == 2026 :
  print("l'année n'est bisecsile et il y as une coupe du monde")
 
 else :
  if (année % 4 == 0 and année % 100 > 0)or ((année % 100 == 0) and (année % 400 == 0)):
   print("l'année etait bisecsile")

  else :
    print("cette année n'est pas bisecsile")

  if année > 1930 and ((année + 2 or année - 2) % 4 == 0) :
    print( " mais cette année il y a eu la coupe du monde")

 continuer = input("vouler vous continuer ? : ").lower()


