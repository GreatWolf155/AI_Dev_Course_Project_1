"""
BOOKMARK 0
Start menu
print user instructions
user input play/stop
play/stop
    start game
        shuffle board
        reset display board
        BOOKMARK 1
        Start Turn
        display board
        user input card 1
        display board
        user input card 2
        display board

        is matching pair?
            yes
                is game over?
                    yes
                        Goto Bookmark 0
                    no
                        Goto Bookmark 1
            no
                Goto Bookmark 1
    end game
"""
import random

def init_game():
    blank = [[]] * 12
    cards = ["A", "B", "C", "D", "E", "F"]
    board = cards * 2
    random.shuffle(board)
    return board, blank

def print_board(cards):
    print(cards[0:3])
    print(cards[3:6])
    print(cards[6:9])
    print(cards[9:12])
    print("\n")

def choose_card(choice, solution, table):
    table[choice] = solution[choice]
    return table

if __name__ == "__main__":
    playing = True
    while playing:
        print("\n" * 50)
        print("MAIN MENU")
        start_game = input("start game?\n1) Yes\n2) No\n")
        if start_game.upper() == "NO" or start_game.upper() == "N" or start_game == '2':
            playing = False
            break
        elif start_game.upper() == "YES" or start_game.upper() == "Y" or start_game == '1':
            print("Instructions:")
            print("1. Pick a card, using the numbers 0 - 11\n   the first row would be 0 - 2, for instance")
            print("2. Pick another card to try to match with it")
            print("3. If the two cards are a match, they will remain visible.\n   Otherwise, both will flip back over")
            print("4. When all cards have been revealed, the game is over")
            next_turn = True
            solution_key, playing_board = init_game()
            while next_turn:
                print_board(playing_board)

                # switch to true for testing
                display_key = False
                if display_key:
                    print_board(solution_key)

                card_one = int(input("enter first card\n"))
                playing_board = choose_card(card_one, solution_key, playing_board)
                print_board(playing_board)

                card_two = int(input("enter second card\n"))
                playing_board = choose_card(card_two, solution_key, playing_board)
                print_board(playing_board)

                if playing_board[card_one] != playing_board[card_two] or card_one == card_two:
                    playing_board[card_one] = []
                    playing_board[card_two] = []

                input()
                print("\n" * 50)

                if playing_board == solution_key:
                    keep_playing = input("congratulations\nplay again?\nyes\nno\n")
                    next_turn = False
                    if keep_playing.upper() == "YES":
                        continue
                    else:
                        playing = False
                        break
