import random

# This function makes the random throws and determines the winner of the throw, returns 1 or 0 as appropriate
def throws(player1, player2):
    options = {1: "Rock", 2: "Scissors", 3: "Paper"}

    input("Press Enter to make your move")

    player1_move = random.randint(1, 3)
    player2_move = random.randint(1, 3)

    print(f"{player1} chose: {options[player1_move]}")
    print(f"{player2} chose: {options[player2_move]}")

    if (player1_move == 1 and player2_move == 3) or (player1_move == 2 and player2_move == 1) or (player1_move == 3 and player2_move == 2):
        print(f"{player1} wins this round")
        return 1, 0  # Point for player 1
    elif (player2_move == 1 and player1_move == 3) or (player2_move == 2 and player1_move == 1) or (player2_move == 3 and player1_move == 2):
        print(f"{player2} wins this round")
        return 0, 1  # Point for player 2
    else:
        print("It's a tie this round!")
        return 0, 0  # Tie, no points awarded
    

# Ask for player names
player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")

# Display rules
print("\nRULES:")
print("* Rock beats Scissors")
print("* Scissors beats Paper")
print("* Paper beats Rock")
print("* 10 rounds are played")
print("* Whoever wins the most rounds wins the game")
print("* In case of a tie, an extra round will be played for a tiebreaker")

# Play 10 rounds
pointsP1 = 0
pointsP2 = 0

for i in range(1, 11):
    print(f"\n--- Throw {i} ---")
    p1, p2 = throws(player1, player2)
    pointsP1 += p1
    pointsP2 += p2

    # If someone already has more than 5 victories, the loop can be cut
    if pointsP1 > 5 or pointsP2 > 5:
        break

# In case of a tie, ONE extra round is played
if pointsP1 == pointsP2:
    print("\nIt's a tie! Playing one extra round.")
    p1, p2 = throws(player1, player2)
    pointsP1 += p1
    pointsP2 += p2

# Display final result
winner = player1 if pointsP1 > pointsP2 else player2
# prints the winner and the highest points with the max function
print(f"\nThe winner is {winner} with {max(pointsP1, pointsP2)} points!")