def display_matchsticks(matchsticks):
    print("Matchsticks remaining:", matchsticks)
    print(" ".join(["|" for _ in range(matchsticks)]))

def player_move(matchsticks):
    while True:
        try:
            num = int(input("Enter the number of matchsticks you want to remove (1, 2, or 3): "))
            if num < 1 or num > 3:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue
            if num > matchsticks:
                print("Not enough matchsticks remaining. Try again.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    matchsticks = 20

    while matchsticks > 0:
        display_matchsticks(matchsticks)
        print("Player 1's turn")
        player1_move = player_move(matchsticks)
        matchsticks -= player1_move

        if matchsticks == 0:
            print("Player 1 wins!")
            break

        display_matchsticks(matchsticks)
        print("Player 2's turn")
        player2_move = player_move(matchsticks)
        matchsticks -= player2_move

        if matchsticks == 0:
            print("Player 2 wins!")

if __name__ == "__main__":
    play_game()
