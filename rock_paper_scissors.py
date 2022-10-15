import random
game_bag = ['''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
            ''''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
            '''
            
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']

choice = int(input("What did you choose? Type '0' for Rock '1' for paper and '2' for scissors:\n"))
if choice < 0 or choice > 2:
    raise Exception("Invalid input")
print(game_bag[choice])
computers_choice = random.randint(0, 2)
print(f"Computers choice>>>\n {game_bag[computers_choice]}")
if choice == 0 and computers_choice == 2 or choice == 2 and computers_choice == 1 or choice == 1 and computers_choice == 0:
    print("You won!")
elif choice == 0 and computers_choice == 1 or choice == 1 and computers_choice == 2 or choice == 2 and computers_choice == 0:
    print("you lose...")
else :
    print("Game is draw!")