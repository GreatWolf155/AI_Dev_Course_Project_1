import pygame
import random
import sys

# --- 1. SETUP ---
pygame.init()
WIDTH, HEIGHT = 600, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Deluxe")

# Fonts & Colors
font = pygame.font.SysFont("Arial", 26, bold=True)
header_font = pygame.font.SysFont("Arial", 40, bold=True)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
BLACK = (30, 30, 30)
RED = (200, 50, 50)

# Game State Management
STATE_MENU = "menu"
STATE_NAME_INPUT = "names"
STATE_PLAYING = "playing"
current_state = STATE_MENU

# Data
p1_name = ""
p2_name = ""
active_input = 1  # Tracking which name we are typing
p1_wins = 0
p2_wins = 0
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 1
game_over = False
game_mode = "pvp"

# --- 2. LOAD IMAGES ---
try:
    x_img = pygame.transform.scale(pygame.image.load("x.png").convert_alpha(), (120, 120))
    o_img = pygame.transform.scale(pygame.image.load("o.png").convert_alpha(), (120, 120))
except:
    x_img = pygame.Surface((120, 120));
    x_img.fill(WHITE)
    o_img = pygame.Surface((120, 120));
    o_img.fill(GOLD)


def draw_text(text, x, y, color=WHITE, center=False, is_header=False):
    f = header_font if is_header else font
    surf = f.render(text, True, color)
    rect = surf.get_rect(center=(x, y)) if center else surf.get_rect(topleft=(x, y))
    screen.blit(surf, rect)


def reset_game():
    global board, turn, game_over
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    turn = 1
    game_over = False


def check_win(player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: return True
    return False


# --- 3. MAIN LOOP ---
while True:
    screen.fill(BG_COLOR)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()

        # STATE: MENU
        if current_state == STATE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "pvc";
                    p2_name = "Computer";
                    current_state = STATE_NAME_INPUT
                if event.key == pygame.K_2:
                    game_mode = "pvp";
                    current_state = STATE_NAME_INPUT

        # STATE: NAME INPUT (Handling the typing)
        elif current_state == STATE_NAME_INPUT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_mode == "pvc" or active_input == 2:
                        # Finalize and Start
                        if not p1_name: p1_name = "Player 1"
                        if game_mode == "pvp" and not p2_name: p2_name = "Player 2"
                        current_state = STATE_PLAYING
                    else:
                        active_input = 2
                elif event.key == pygame.K_BACKSPACE:
                    if active_input == 1:
                        p1_name = p1_name[:-1]
                    else:
                        p2_name = p2_name[:-1]
                else:
                    if len(p1_name) < 10 and active_input == 1:
                        p1_name += event.unicode
                    elif len(p2_name) < 10 and active_input == 2:
                        p2_name += event.unicode

        # STATE: PLAYING
        elif current_state == STATE_PLAYING:
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                if 100 < y < 700:
                    row, col = (y - 100) // 200, x // 200
                    if board[row][col] == 0:
                        board[row][col] = 1
                        if check_win(1):
                            p1_wins += 1; game_over = True
                        else:
                            turn = 2
                if y > 710:  # Forfeit
                    if turn == 1:
                        p2_wins += 1
                    else:
                        p1_wins += 1
                    reset_game()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r: reset_game()
                if event.key == pygame.K_e:
                    print(f"Final: {p1_name} ({p1_wins}) - {p2_name} ({p2_wins})")
                    pygame.quit();
                    sys.exit()

    # Comp Logic
    if current_state == STATE_PLAYING and game_mode == "pvc" and turn == 2 and not game_over:
        pygame.time.delay(300)
        available = [(r, c) for r in range(3) for c in range(3) if board[r][c] == 0]
        if available:
            r, c = random.choice(available)
            board[r][c] = 2
            if check_win(2): p2_wins += 1; game_over = True
        turn = 1
        if not any(0 in row for row in board): game_over = True

    # --- 4. DRAWING ---
    if current_state == STATE_MENU:
        draw_text("TIC-TAC-TOE", 300, 150, GOLD, True, True)
        draw_text("1) Single Player (vs CPU)", 300, 320, WHITE, True)  # Line 1
        draw_text("2) Two Players (Local PvP)", 300, 380, WHITE, True)  # Line 2
        draw_text("Press 1 or 2 to Choose", 300, 550, (180, 180, 180), True)

    elif current_state == STATE_NAME_INPUT:
        draw_text("PLAYER REGISTRATION", 300, 150, GOLD, True, True)
        # P1 Input
        p1_color = GOLD if active_input == 1 else WHITE
        draw_text(f"Player 1 Name: {p1_name}_", 100, 250, p1_color)

        # P2 Input (Only if PvP)
        if game_mode == "pvp":
            p2_color = GOLD if active_input == 2 else WHITE
            draw_text(f"Player 2 Name: {p2_name}_", 100, 350, p2_color)
        else:
            draw_text("Opponent: Computer", 100, 350, (150, 150, 150))

        draw_text("Press ENTER to confirm", 300, 500, WHITE, True)

    elif current_state == STATE_PLAYING:
        # UI & Board
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 100))
        draw_text(f"{p1_name}: {p1_wins}", 50, 35)
        draw_text(f"{p2_name}: {p2_wins}", 400, 35)
        for i in range(1, 3):
            pygame.draw.line(screen, LINE_COLOR, (i * 200, 100), (i * 200, 700), 8)
            pygame.draw.line(screen, LINE_COLOR, (0, 100 + i * 200), (600, 100 + i * 200), 8)
        for r in range(3):
            for c in range(3):
                if board[r][c] == 1: screen.blit(x_img, (c * 200 + 40, r * 200 + 140))
                if board[r][c] == 2: screen.blit(o_img, (c * 200 + 40, r * 200 + 140))

        pygame.draw.rect(screen, RED, (225, 710, 150, 35), border_radius=8)
        draw_text("GIVE UP", 300, 727, WHITE, True)

        if game_over:
            pygame.draw.rect(screen, BLACK, (80, 280, 440, 200), border_radius=15)
            draw_text("ROUND OVER", 300, 320, GOLD, True)
            draw_text("[R] to Restart Game", 300, 370, WHITE, True)
            draw_text("[E] to Exit Game", 300, 410, RED, True)

    pygame.display.update()