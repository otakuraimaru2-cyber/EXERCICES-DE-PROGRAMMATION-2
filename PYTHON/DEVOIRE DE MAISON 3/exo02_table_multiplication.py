

print("✖️ --- GÉNÉRATEUR DE TABLE D'OPERATION ---")

print("NB : \n addition = 1 \n soustraction = 2 \n multiplication = 3 \n division = 4")

print(" ")

operation = input("quel operaration souhaitez vous effectuer ?: ")
print(" ")

table = int(input("Quelle table souhaites-tu afficher ? "))

print(" ")

limite = int(input("jusqu'a combien voulez vous etendre le calcule ?: "))

print("\n" + "=" * 40)

print(f" TABLE DE {table} ")

print("========================================")

for i in range( limite + 1):
  
  if operation == "1":
    resultats = i + table
    signe = "+"

  elif operation == "2" :
    resultats = i - table
    signe = "-"
  
  elif operation == "3" :
    resultats = i * table
    signe = "x"

  elif operation == "4" :
    resultats = i / table
    signe = "/" 
    
  print(f"\n{i} {signe} {table} = {resultats}")     