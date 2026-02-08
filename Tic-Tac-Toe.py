import random

class PreviousValue(Exception):
    """player attempted to choose an occupied space"""
    pass

class InvalidChoice(Exception):
    """player attempted to choose a space not on the board"""
    pass

def pick_name(player):
    player[0] = input("Please enter your name:\n")
    return player

def print_board(board):
    print("   A   B   C")
    for i in range(0, 3):
        # REMINDER: board[row][col]
        print(f"{i+1}  {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("  ___|___|___")
        else:
            print("     |   |")

def pick_symbol():
    while True:
        print("\n" * 50)
        choice = input("Player 1, please pick a symbol\n1) X\n2) O\n3) Pass\n").upper()
        if choice in ["1", "X"]:
            return "X"
        elif choice in ["2", "O"]:
            return "O"
        elif choice in ["3", "PASS"]:
            return random.choice(["X", "O"])
        else:
            print("Invalid choice. Please enter X, O, or Pass")
            input("Press enter to continue\n")

def board_choice(play_turn, symbol, p2, board_array):
    #whose turn it is, the symbol the current player uses,
    # player 2 (comp or user), current board

    choice_dict = {
        "1A": [0, 0], "1B": [0, 1], "1C": [0, 2],
        "2A": [1, 0], "2B": [1, 1], "2C": [1, 2],
        "3A": [2, 0], "3B": [2, 1], "3C": [2, 2],
        "A1": [0, 0], "B1": [0, 1], "C1": [0, 2],
        "A2": [1, 0], "B2": [1, 1], "C2": [1, 2],
        "A3": [2, 0], "B3": [2, 1], "C3": [2, 2]
    }
    if play_turn == 2 and p2 == "comp": #computer turn
        available_moves = []
        for row in range(3):
            for col in range(3):
                if board_array[row][col] == " ":
                    available_moves.append((row, col))
        choice = random.choice(available_moves)
        board_array[choice[0]][choice[1]] = symbol
        print_board(board_array)
        return board_array

    #players turn - no if here
    print_board(board_array)
    while True:
        try:
            choice = input("Please choose where to place your symbol\n"
                           "acceptable options: 1B, 2C, A3\n").upper() #row and then column, in uppercase
            if choice not in choice_dict.keys():
                raise InvalidChoice("Please choose a valid spot")

            if board_array[choice_dict[choice][0]][choice_dict[choice][1]] != " ":
                raise PreviousValue("This spot has already been played, please pick a different one")
            else:
                board_array[choice_dict[choice][0]][choice_dict[choice][1]] = symbol
                print("\n" * 50)
                print_board(board_array)
                return board_array
        except PreviousValue as e:
            print(e)
            continue
        except InvalidChoice as e:
            print(e)
            continue

def check_board(game_array):
    # check the array for win conditions
    # returns game result as a string
    for i in range(3): # check rows
        if game_array[i][0] != " " and game_array[i][0] == game_array[i][1] == game_array[i][2]:
            return "win"
    for j in range(3): # check columns
        if game_array[0][j] != " " and game_array[0][j] == game_array[1][j] == game_array[2][j]:
            return "win"
    if game_array[1][1] != " " and (game_array[0][0] == game_array[1][1] == game_array[2][2] or game_array[2][0] == game_array[1][1] == game_array[0][2]):
        return "win"
    for row in game_array:
        for col in row:
            if col == " ":
                return None
    return "cats game"


if __name__ == "__main__":
    playing = True
    while playing:
        player_one = [" ", " "]
        player_two = [" ", " "]
        print("Welcome to")
        board_arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # sets an array for the board
        board_abc = [["T", "I", "C"], ["T", "A", "C"], ["T", "O", "E"]]
        print_board(board_abc)
        player2 = None
        input("Press enter to continue\n")
        while player2 is None:  # picking a game mode
            print("\n" * 50)
            gamemode = input("Please enter a game mode:\n1) 1-Player\n2) 2-Player\n3) Exit\n").lower()
            if gamemode in ["1", "one"]:
                print("1-player mode selected")
                player_two[0] = player2 = "comp"
                print("Player One")
                pick_name(player_one)
            elif gamemode in ["2", "two"]:
                print("2-player mode selected")
                player2 = "user"
                print("Player One")
                pick_name(player_one)
                print("Player Two")
                pick_name(player_two)
            elif gamemode in ["3", "exit", "quit"]:
                playing = False
                break
            else:
                print("Invalid input")
        if player2 is None:
            break
        options = ["X", "O"]
        player_one[1] = pick_symbol()

        options.remove(player_one[1])
        player_two[1] = options[0]
        turn_count = 1
        game = True
        while game: # Let's start playing here
            print("\n" * 50)
            player_turn = 2 - turn_count % 2
            if player_turn == 1:
                current_symbol = player_one[1]
                print(f"{player_one[0]}'s ({current_symbol}) turn\n")
            else:
                current_symbol = player_two[1]
                if player2 != "comp":
                    print(f"{player_two[0]}'s ({current_symbol}) turn\n")
                else:
                    print(f"Comp's ({current_symbol}) turn\n")

            board_arr = board_choice(player_turn, current_symbol, player2, board_arr)

            input("Press enter to continue\n")

            game_status = check_board(board_arr)
            if game_status == None:
                turn_count += 1
                continue

            if game_status == "win":
                if player_turn == 1:
                    print(f"{player_one[0]} ({current_symbol}) wins!\n")
                else:
                    current_symbol = player_two[1]
                    if player2 != "comp":
                        print(f"{player_two[0]} ({current_symbol}) wins!\n")
                    else:
                        print(f"Comp ({current_symbol}) wins!\n")
                game = False
                break
                
            if game_status == "cats game":
                print("Game ended in a draw!\n")
                game = False
                break

        while True:
            game_end = input("Do you want to play again?\n"
                             "1) Yes\n"
                             "2) No\n").upper()
            if game_end in ["YES", "1"]:
                break
            if game_end in ["NO", "2"]:
                playing = False
                break