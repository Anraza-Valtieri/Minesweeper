import pygame
import Misc

button_width = 150
button_height = 75
button_gap = button_width * 1.5
easy_pos = [Misc.display_width / 2 - button_width / 2 - button_gap, Misc.display_height / 2]
med_pos = [Misc.display_width / 2 - button_width / 2, Misc.display_height / 2]
hard_pos = [Misc.display_width / 2 - button_width / 2 + button_gap, Misc.display_height / 2]
back_pos = [Misc.display_width - button_width - 100, Misc.display_height - button_height - 50]
ez_pos = [Misc.display_width - button_width/2, button_height/3]
ez_color = Misc.GREY

def gameDifficulty():
    options = True
    if Misc.EZ_SENSOR is True:
        option_color = Misc.PINK
    else:
        option_color = Misc.BLACK

    while options:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            if event.type is pygame.MOUSEBUTTONDOWN:
                POS_X, POS_Y = pygame.mouse.get_pos()
                if (easy_pos[0] < POS_X < easy_pos[0] + button_width and easy_pos[1] < POS_Y < easy_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.easy, Misc.difficulty)
                elif (med_pos[0] < POS_X < med_pos[0] + button_width and med_pos[1] < POS_Y < med_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.medium, Misc.difficulty)
                elif (hard_pos[0] < POS_X < hard_pos[0] + button_width and hard_pos[1] < POS_Y < hard_pos[1] + button_height):
                    Misc.difficulty = Misc.set_difficulty(Misc.hard, Misc.difficulty)
                elif (ez_pos[0] < POS_X < ez_pos[0] + button_width/3 and ez_pos[1] < POS_Y < ez_pos[1] + button_height/3):
                    if Misc.EZ_SENSOR is False:
                        Misc.EZ_SENSOR = True
                        option_color = Misc.PINK
                    else:
                        Misc.EZ_SENSOR = False
                        option_color = Misc.BLACK
                elif (back_pos[0] < POS_X < back_pos[0] + button_width and back_pos[1] < POS_Y < back_pos[1] + button_height):
                    options = False

        Misc.gameDisplay.fill(option_color)
        if Misc.difficulty is Misc.easy_mode:
            game_difficulty = Misc.easy
            text_color = Misc.LIGHT_GREEN
        elif Misc.difficulty is Misc.medium_mode:
            game_difficulty = Misc.medium
            text_color = Misc.LIGHT_YELLOW
        elif Misc.difficulty is Misc.hard_mode:
            game_difficulty = Misc.hard
            text_color = Misc.LIGHT_RED

        Misc.message_to_screen(game_difficulty, text_color, -50, "XL")
        Misc.button(Misc.easy, easy_pos[0], easy_pos[1], button_width, button_height, Misc.GREEN, Misc.LIGHT_GREEN, "S")
        Misc.button(Misc.medium, med_pos[0], med_pos[1], button_width, button_height, Misc.YELLOW, Misc.LIGHT_YELLOW, "S")
        Misc.button(Misc.hard, hard_pos[0], hard_pos[1], button_width, button_height, Misc.RED, Misc.LIGHT_RED, "S")
        Misc.button("BACK", back_pos[0], back_pos[1], button_width, button_height, Misc.GREY, Misc.WHITE, "S")
        Misc.button("EZ MODE", ez_pos[0], ez_pos[1], button_width / 3, button_height / 3, ez_color, ez_color, "XS")

        Misc.refresh()
