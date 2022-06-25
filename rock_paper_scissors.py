import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print('Let\'s play Rock, Paper, Scissors!')
pick = int(input('Please pick one: 0 - Rock, 1 - Paper, 2 - Scissors\n'))

cpu = random.randint(0,2)
map = [pick, cpu]
game_images = [rock, paper, scissors]
hand_names = ["Rock", "Paper", "Scissors"]

if map == [0,0] or map == [1,1] or map == [2,2]:
  print(f"You picked {hand_names[pick]}!")
  print(game_images[pick])
  print(f"CPU picked {hand_names[cpu]}!")
  print(game_images[cpu])
  print('It\'s a draw')
elif map == [0,1] or map == [1,2] or map == [2,0]:
  print(f"You picked {hand_names[pick]}!")
  print(game_images[pick])
  print(f"CPU picked {hand_names[cpu]}!")
  print(game_images[cpu])
  print('CPU wins')
elif map == [0,2] or map == [1,0] or map == [2,1]:
  print(f"You picked {hand_names[pick]}!")
  print(game_images[pick])
  print(f"CPU picked {hand_names[cpu]}!")
  print(game_images[cpu])
  print('You win')
else:
  print("Invalid input")