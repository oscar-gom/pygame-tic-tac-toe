import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont('Arial', 72)
win_font = pygame.font.SysFont('Arial', 18)

txt_x = font.render("X", True, "white")
txt_o = font.render("O", True, "white")

x_turn = True
won = False
spaces = ["", "", "",
          "", "", "",
          "", "", ""]


def show_winner_message(winner):
    surf_pane = pygame.Surface((200, 150))
    surf_pane.fill((0, 0, 0, 0.5))
    rect_pane = surf_pane.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    if winner == "x":
        screen.blit(surf_pane, rect_pane)
        txt_win = win_font.render("X wins!\nPress space to play again", True, "white")
        rect_txt_win = txt_win.get_rect(center=(320, 320))
        screen.blit(txt_win, rect_txt_win)
    elif winner == "o":
        screen.blit(surf_pane, rect_pane)
        txt_win = win_font.render("O wins!\nPress space to play again", True, "white")
        rect_txt_win = txt_win.get_rect(center=(320, 320))
        screen.blit(txt_win, rect_txt_win)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0] and not won:
        mouse_pos = pygame.mouse.get_pos()

        if 0 <= mouse_pos[0] <= 212 and 0 <= mouse_pos[1] <= 212 and spaces[0] == "":
            if x_turn:
                spaces[0] = "x"
                x_turn = False
            else:
                spaces[0] = "o"
                x_turn = True
        elif 428 >= mouse_pos[0] >= 212 >= mouse_pos[1] >= 0 and spaces[1] == "":
            if x_turn:
                spaces[1] = "x"
                x_turn = False
            else:
                spaces[1] = "o"
                x_turn = True
        elif 428 <= mouse_pos[0] <= 640 and 0 <= mouse_pos[1] <= 212 and spaces[2] == "":
            if x_turn:
                spaces[2] = "x"
                x_turn = False
            else:
                spaces[2] = "o"
                x_turn = True
        elif 0 <= mouse_pos[0] <= 212 <= mouse_pos[1] <= 428 and spaces[3] == "":
            if x_turn:
                spaces[3] = "x"
                x_turn = False
            else:
                spaces[3] = "o"
                x_turn = True
        elif 212 <= mouse_pos[0] <= 428 and 212 <= mouse_pos[1] <= 428 and spaces[4] == "":
            if x_turn:
                spaces[4] = "x"
                x_turn = False
            else:
                spaces[4] = "o"
                x_turn = True
        elif 640 >= mouse_pos[0] >= 428 >= mouse_pos[1] >= 212 and spaces[5] == "":
            if x_turn:
                spaces[5] = "x"
                x_turn = False
            else:
                spaces[5] = "o"
                x_turn = True
        elif 0 <= mouse_pos[0] <= 212 and 428 <= mouse_pos[1] <= 640 and spaces[6] == "":
            if x_turn:
                spaces[6] = "x"
                x_turn = False
            else:
                spaces[6] = "o"
                x_turn = True
        elif 212 <= mouse_pos[0] <= 428 <= mouse_pos[1] <= 640 and spaces[7] == "":
            if x_turn:
                spaces[7] = "x"
                x_turn = False
            else:
                spaces[7] = "o"
                x_turn = True
        elif 428 <= mouse_pos[0] <= 640 and 428 <= mouse_pos[1] <= 640 and spaces[8] == "":
            if x_turn:
                spaces[8] = "x"
                x_turn = False
            else:
                spaces[8] = "o"
                x_turn = True

    screen.fill("black")

    for i, symbol in enumerate(spaces):
        row = i // 3
        col = i % 3
        square_x = col * 212
        square_y = row * 212

        text_width, text_height = font.size(symbol)
        text_x = square_x + (212 - text_width) // 2
        text_y = square_y + (212 - text_height) // 2

        if symbol == "x":
            screen.blit(txt_x, (text_x, text_y))
        elif symbol == "o":
            screen.blit(txt_o, (text_x, text_y))

    # check win
    if spaces[0] == "x" and spaces[1] == "x" and spaces[2] == "x":
        pygame.draw.line(screen, (255, 255, 255), (0, 106), (screen.get_width(), 106), width=4)
        show_winner_message("x")
        won = True
    elif spaces[3] == "x" and spaces[4] == "x" and spaces[5] == "x":
        pygame.draw.line(screen, (255, 255, 255), (0, 318), (screen.get_width(), 318), width=4)
        show_winner_message("x")
        won = True
    elif spaces[6] == "x" and spaces[7] == "x" and spaces[8] == "x":
        pygame.draw.line(screen, (255, 255, 255), (0, 530), (screen.get_width(), 530), width=4)
        show_winner_message("x")
        won = True
    elif spaces[0] == "x" and spaces[3] == "x" and spaces[6] == "x":
        pygame.draw.line(screen, (255, 255, 255), (110, 0), (110, screen.get_height()), width=4)
        show_winner_message("x")
        won = True
    elif spaces[1] == "x" and spaces[4] == "x" and spaces[7] == "x":
        pygame.draw.line(screen, (255, 255, 255), (322, 0), (322, screen.get_height()), width=4)
        show_winner_message("x")
        won = True
    elif spaces[2] == "x" and spaces[5] == "x" and spaces[8] == "x":
        pygame.draw.line(screen, (255, 255, 255), (534, 0), (534, screen.get_height()), width=4)
        show_winner_message("x")
        won = True
    elif spaces[0] == "x" and spaces[4] == "x" and spaces[8] == "x":
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (640, 640), width=4)
        show_winner_message("x")
        won = True
    elif spaces[2] == "x" and spaces[4] == "x" and spaces[6] == "x":
        pygame.draw.line(screen, (255, 255, 255), (640, 0), (0, 640), width=4)
        show_winner_message("x")
        won = True

    if spaces[0] == "o" and spaces[1] == "o" and spaces[2] == "o":
        pygame.draw.line(screen, (255, 255, 255), (0, 106), (screen.get_width(), 106), width=4)
        show_winner_message("o")
        won = True
    elif spaces[3] == "o" and spaces[4] == "o" and spaces[5] == "o":
        pygame.draw.line(screen, (255, 255, 255), (0, 318), (screen.get_width(), 318), width=4)
        show_winner_message("o")
        won = True
    elif spaces[6] == "o" and spaces[7] == "o" and spaces[8] == "o":
        pygame.draw.line(screen, (255, 255, 255), (0, 530), (screen.get_width(), 530), width=4)
        show_winner_message("o")
        won = True
    elif spaces[0] == "o" and spaces[3] == "o" and spaces[6] == "o":
        pygame.draw.line(screen, (255, 255, 255), (110, 0), (110, screen.get_height()), width=4)
        show_winner_message("o")
        won = True
    elif spaces[1] == "o" and spaces[4] == "o" and spaces[7] == "o":
        pygame.draw.line(screen, (255, 255, 255), (322, 0), (322, screen.get_height()), width=4)
        show_winner_message("o")
        won = True
    elif spaces[2] == "o" and spaces[5] == "o" and spaces[8] == "o":
        pygame.draw.line(screen, (255, 255, 255), (534, 0), (534, screen.get_height()), width=4)
        show_winner_message("o")
        won = True
    elif spaces[0] == "o" and spaces[4] == "o" and spaces[8] == "o":
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (640, 640), width=4)
        show_winner_message("o")
        won = True
    elif spaces[2] == "o" and spaces[4] == "o" and spaces[6] == "o":
        pygame.draw.line(screen, (255, 255, 255), (640, 0), (0, 640), width=4)
        show_winner_message("o")
        won = True

    if won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            spaces = ["", "", "",
                      "", "", "",
                      "", "", ""]
            x_turn = True
            won = False

    pygame.draw.line(screen, (255, 255, 255), (212, 0), (212, 640), width=4)
    pygame.draw.line(screen, (255, 255, 255), (428, 0), (428, 640), width=4)
    pygame.draw.line(screen, (255, 255, 255), (0, 212), (640, 212), width=4)
    pygame.draw.line(screen, (255, 255, 255), (0, 428), (640, 428), width=4)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
