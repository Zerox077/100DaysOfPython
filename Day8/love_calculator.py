def calculate_love_score(name1, name2):
   true = sum([f"{name1}{name2}".upper().count(letter) for letter in "TRUE"])
   love = sum([f"{name1}{name2}".upper().count(letter) for letter in "LOVE"])
   print(f"{true}{love}")
calculate_love_score("Amit", "Simu")
