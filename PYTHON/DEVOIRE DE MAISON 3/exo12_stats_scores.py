

scores = [320, 450, 280, 500, 390, 460]

while len(scores) <8 :
  nb_matchs = len(scores)

  total_points = sum(scores)

  record_max = max(scores)

  score_min = min(scores)

  moyenne = total_points / nb_matchs


  print("🏆 --- STATISTIQUES DU TOURNOI E-SPORT ---")

  print(f"\nMatchs enregistrés : {scores}\n")
  print("=" * 40)
  print("BILAN OFFICIEL DE L'ÉQUIPE :")

  print(f"\n• Nombre de matchs disputés : {nb_matchs} matchs")

  print(f"\n• Total des points cumulés : {total_points} points")

  print(f"\n• Meilleur score (Record) : {record_max} points (MVP 🌟)")

  print(f"\n• Score le plus bas : {score_min} points")

  print(f"\n• Moyenne par match : {moyenne:.2f} points/match")

  print("========================================")
  if len(scores) == 7 :
    break
 
  new_score = int(input("quel est le nouveau score oblenur ?: "))
  scores.append(new_score)