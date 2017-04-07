import pygame
import Misc
import Scoreboard
import Difficulty
import Play

TITLE_POS = -250

ButtonLength = 200
ButtonWidth = 50
ButtonGap = 60

START_BUTTON_POS_X = Misc.display_width/2 - ButtonLength/2
LOAD_BUTTON_POS_X = START_BUTTON_POS_X
SCOREBOARD_BUTTON_POS_X= START_BUTTON_POS_X
DIFFICULTY_BUTTON_POS_X = START_BUTTON_POS_X
EXIT_BUTTON_POS_X = START_BUTTON_POS_X

START_BUTTON_POS_Y = Misc.display_height/2
LOAD_BUTTON_POS_Y = START_BUTTON_POS_Y + ButtonGap
SCOREBOARD_BUTTON_POS_Y = LOAD_BUTTON_POS_Y + ButtonGap
DIFFICULTY_BUTTON_POS_Y = SCOREBOARD_BUTTON_POS_Y + ButtonGap
EXIT_BUTTON_POS_Y = DIFFICULTY_BUTTON_POS_Y + ButtonGap


def game_intro():
    intro = True

    while intro is True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button is 1:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    # LOAD BUTTON
                    if (LOAD_BUTTON_POS_X < pos_x < LOAD_BUTTON_POS_X + ButtonLength and
                          LOAD_BUTTON_POS_Y < pos_y < LOAD_BUTTON_POS_Y + ButtonWidth):
                        game_loop = True
                        while game_loop:
                            game_loop = Play.play_game_seed("laststate")
                    # START BUTTON
                    elif (START_BUTTON_POS_X < pos_x < START_BUTTON_POS_X + ButtonLength and
                        START_BUTTON_POS_Y < pos_y < START_BUTTON_POS_X + ButtonWidth):
                        game_loop = True
                        while game_loop:
                            game_loop = Play.play_game(Misc.difficulty,None)
                    elif (SCOREBOARD_BUTTON_POS_X < pos_x < SCOREBOARD_BUTTON_POS_X + ButtonLength and
                        SCOREBOARD_BUTTON_POS_Y < pos_y < SCOREBOARD_BUTTON_POS_Y + ButtonWidth):
                        Scoreboard.gameScoreboard()
                    # DIFFICULTY BUTTON
                    elif (DIFFICULTY_BUTTON_POS_X < pos_x < DIFFICULTY_BUTTON_POS_X + ButtonLength and
                        DIFFICULTY_BUTTON_POS_Y < pos_y < DIFFICULTY_BUTTON_POS_Y + ButtonWidth):
                        Difficulty.gameDifficulty()
                    # EXIT BUTTON
                    elif (EXIT_BUTTON_POS_X < pos_x < EXIT_BUTTON_POS_X + ButtonLength and
                        EXIT_BUTTON_POS_Y < pos_y < EXIT_BUTTON_POS_Y + ButtonWidth):
                        pygame.quit()
                        quit()

        Misc.gameDisplay.fill(Misc.BLACK)
        Misc.gameDisplay.blit(Misc.wallpaper, Misc.display_origin)
        Misc.message_to_screen("MINESWEEPER", Misc.GREY, TITLE_POS, "XXL")

        Misc.button("START",START_BUTTON_POS_X, START_BUTTON_POS_Y, ButtonLength, ButtonWidth, Misc.GREY, Misc.WHITE, "S")
        Misc.button("LOAD", LOAD_BUTTON_POS_X, LOAD_BUTTON_POS_Y, ButtonLength, ButtonWidth,
                    Misc.GREY, Misc.WHITE, "S")
        Misc.button("SCOREBOARD", SCOREBOARD_BUTTON_POS_X, SCOREBOARD_BUTTON_POS_Y, ButtonLength, ButtonWidth, Misc.GREY, Misc.WHITE, "S")
        Misc.button("DIFFICULTY", DIFFICULTY_BUTTON_POS_X, DIFFICULTY_BUTTON_POS_Y, ButtonLength, ButtonWidth, Misc.GREY, Misc.WHITE, "S")
        Misc.button("EXIT", EXIT_BUTTON_POS_X, EXIT_BUTTON_POS_Y, ButtonLength, ButtonWidth, Misc.GREY, Misc.WHITE, "S")

        Misc.refresh()
