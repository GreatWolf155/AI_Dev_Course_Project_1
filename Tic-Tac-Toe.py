import random


class PreviousValue(Exception):
    """player attempted to choose an occupied space"""
    pass

class InvalidChoice(Exception):
    """player attempted to choose a space not on the board"""
    pass

choice_dict_options = {
    "1A": [0, 0], "1B": [0, 1], "1C": [0, 2],
    "2A": [1, 0], "2B": [1, 1], "2C": [1, 2],
    "3A": [2, 0], "3B": [2, 1], "3C": [2, 2],
    "A1": [0, 0], "B1": [0, 1], "C1": [0, 2],
    "A2": [1, 0], "B2": [1, 1], "C2": [1, 2],
    "A3": [2, 0], "B3": [2, 1], "C3": [2, 2]
}

def pick_name(opponent_name = None) -> str:
    """
    # players can choose names for themselves
    :param opponent_name: specifically to check if the name is taken
    :return: str - player name
    """
    while True:
        player_name = str(input("Please enter your name:\n"))
        if len(player_name) == 0:
            print("Please enter a valid name.")
        elif player_name == opponent_name:
            print("That name is already taken.")
        return player_name

def print_board(board) -> None:
    """
    prints the current board
    :param board: 2D list containing the board symbols
    :return: None
    """
    print("   A   B   C")
    for i in range(0, 3):
        # REMINDER: board[row][col]
        print(f"{i+1}  {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("  ___|___|___")
        else:
            print("     |   |")

def pick_symbol() -> str:
    """
    player chooses a symbol or can choose to pass
    :return: player symbol
    """
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
            input("Press enter to return\n")

def board_choice(play_turn, symbol, p2, board_array, choice_dict) -> list:
    """
    current player can choose a spot to take
    :param play_turn: current player turn
    :param symbol: current player's symbol
    :param p2: str - to check if player 2 is computer
    :param board_array: the board layout
    :param choice_dict: all the different options to choose from
    :return: the new board array
    """
    #whose turn it is, the symbol the current player uses,
    # player 2 (comp or user), current board
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

    #players turn - no 'if' here
    print_board(board_array)
    while True:
        try:
            choice = input("Please choose where to place your symbol\n"
                           "acceptable options: 1B, 2C, A3\n"
                           "Or type 'exit' to quit the game\n").upper() #row and then column, in uppercase
            if choice == "EXIT":
                return []
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

def check_board(game_array) -> str | None:
    """
    check the array for win conditions
    :param game_array: 2D list containing the board
    :return: str - game result
    """
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

def intro() -> None:
    """
    print out a cool intro page
    :return:
    """
    print("Welcome to")
    board_abc = [["T", "I", "C"], ["T", "A", "C"], ["T", "O", "E"]]
    print_board(board_abc)
    input("Press enter to continue\n")
    return None

def gamemode_select(player_1, player_2, is_first_game) -> tuple:
    """
    select a game mode or exit, and set player names
    :param player_1: list - for changing player name
    :param player_2: list - for changing player name
    :param is_first_game: only go to change names for the first game
    :return: tuple(bool - play, list - player_1, list - player_2, bool - is_first_game)
    """
    player2_status = None
    play = True
    while player2_status is None:  # picking a game mode
        print("\n" * 50)
        if is_first_game:
            gamemode = input("Please enter a game mode:\n1) 1-Player\n2) 2-Player\n3) Exit\n").lower()
            if gamemode in ["1", "one"]:
                print("1-player mode selected")
                player_2[0] = player2_status = "comp"
                print("Player One")
                player_1[0] = pick_name()
            elif gamemode in ["2", "two"]:
                print("2-player mode selected")
                player2_status = "user"
                print("Player One")
                player_1[0] = pick_name()
                print("Player Two")
                player_2[0] = pick_name(player_1[0])
            elif gamemode in ["3", "exit", "quit"]:
                play = False
                break
            else:
                print("Invalid input")
                continue
        else:
            player2_status = player_2[0]
    if player2_status is None:
        # player2_status is neither comp nor player
        # return playing = False
        return False, player_1, player_2, None
    return play, player_1, player_2, player2_status

def choose_symbol() -> tuple:
    """
    player chooses a symbol
    :return: tuple - symbols for both players
    """
    options = ["X", "O"]
    p1_symbol = pick_symbol()
    options.remove(p1_symbol)
    return p1_symbol, options[0]

def main() -> None:
    """
    main function
    :return: None
    """
    playing = True
    player_one = [" ", " ", 0]
    player_two = [" ", " ", 0]
    first_run = True

    while playing:
        board_arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # sets an array for the board
        (playing, player_one, player_two, player2) = gamemode_select(player_one, player_two, first_run)
        if not playing:
            break

        if first_run:
            player_one[1], player_two[1] = choose_symbol()
        first_run = False
        turn_count = 1

        while True:  # Let's start playing here
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

            board_arr = board_choice(player_turn, current_symbol, player2, board_arr, choice_dict_options)
            if board_arr == []:
                print("\n" * 50)
                print("FORFEIT DETECTED!")
                if player_turn == 1:
                    player_two[2] += 1
                    print(f"{player_one[0]} quit. Point goes to {player_two[0]}!")
                else:
                    player_one[2] += 1
                    print(f"{player_two[0]} quit. Point goes to {player_one[0]}!")
                break
            input("Press enter to continue\n")

            game_status = check_board(board_arr)
            if game_status is None:
                turn_count += 1
                continue
            if game_status == "win":
                if player_turn == 1:
                    player_one[2] += 1
                    print(f"{player_one[0]} ({current_symbol}) wins!\n")
                else:
                    player_two[2] += 1
                    current_symbol = player_two[1]
                    if player2 != "comp":
                        print(f"{player_two[0]} ({current_symbol}) wins!\n")
                    else:
                        print(f"Comp ({current_symbol}) wins!\n")
                break
            if game_status == "cats game":
                print("Game ended in a draw!\n")
                break

        while True:
            print("SCOREBOARD")
            print(f"{player_one[0].capitalize()}: {player_one[2]}\n{player_two[0].capitalize()}: {player_two[2]}")
            game_end = input("Do you want to play again?\n"
                             "1) Yes\n"
                             "2) No\n").upper()
            if game_end in ["YES", "1"]:
                break
            if game_end in ["NO", "2"]:
                playing = False
                break


if __name__ == "__main__":
    intro()
    main()