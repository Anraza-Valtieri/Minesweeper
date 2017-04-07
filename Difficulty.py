import pygame
import Misc

button_width = 120
button_height = 60
button_gap = button_width * 1.5
easy_pos = [Misc.display_width / 2 - button_width / 2 - button_gap, Misc.display_height / 2]
med_pos = [Misc.display_width / 2 - button_width / 2, Misc.display_height / 2]
hard_pos = [Misc.display_width / 2 - button_width / 2 + button_gap, Misc.display_height / 2]

def gameDifficulty():
    options = True

    while options:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            if event.type is pygame.MOUSEBUTTONDOWN:
                POS_X, POS_Y = pygame.mouse.get_pos()
                if (easy_pos[0] < POS_X < easy_pos[0] + button_width and easy_pos[1] < POS_Y < easy_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.easy, Misc.difficulty)
                    options = False
                elif (med_pos[0] < POS_X < med_pos[0] + button_width and med_pos[1] < POS_Y < med_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.medium, Misc.difficulty)
                    options = False
                elif (hard_pos[0] < POS_X < hard_pos[0] + button_width and hard_pos[1] < POS_Y < hard_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.hard, Misc.difficulty)
                    options = False

        Misc.gameDisplay.fill(Misc.BLACK)
        if Misc.difficulty is Misc.easy_mode:
            game_difficulty = Misc.easy
            text_color = Misc.LIGHT_GREEN
        elif Misc.difficulty is Misc.medium_mode:
            game_difficulty = Misc.medium
            text_color = Misc.LIGHT_YELLOW
        elif Misc.difficulty is Misc.hard_mode:
            game_difficulty = Misc.hard
            text_color = Misc.LIGHT_RED

        # elif Misc
        Misc.message_to_screen(game_difficulty, text_color, -50, "XL")
        Misc.button(Misc.easy, easy_pos[0], easy_pos[1], button_width, button_height, Misc.GREEN, Misc.LIGHT_GREEN, "S")
        Misc.button(Misc.medium, med_pos[0], med_pos[1], button_width, button_height, Misc.YELLOW, Misc.LIGHT_YELLOW, "S")
        Misc.button(Misc.hard, hard_pos[0], hard_pos[1], button_width, button_height, Misc.RED, Misc.LIGHT_RED, "S")

        Misc.refresh()
