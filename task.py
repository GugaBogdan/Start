import random

rps = ['rock', 'paper', 'scissors']

player1 = random.choice(rps)
print(f"MJ gave: {player1}")

player2 = random.choice(rps)
print(f"Guvanya gave: {player2}")

if player1 == "rock" and player2 == "scissors":
    print("Winner is MJ!")
elif player1 == "scissors" and player2 == "paper":
    print("Winner is MJ!")
elif player1 == "paper" and player2 == "rock":
    print("Winner is MJ!")
elif player1 == "rock" and player2 == "paper":
    print("Winner is Guvanya")
elif player1 == "paper" and player2 == "scissors":
    print("Winner is Guvanya")
elif player1 == "scissors" and player2 == "rock":
    print("Winner is Guvanya")
else:
    print("Tie! Run again.")
