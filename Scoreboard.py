import pygame
import Misc
import Score
import Play

title_POS = 50 - Misc.display_height / 2
scroll_speed = -15

name_POS_X = 50
score_POS_X = Misc.display_width - 300
replay_size = [100, 30]
replay_POX_X = Misc.display_width - replay_size[0] - 30
name_POS_Y = 150
POS_Y_gap = 50
replay_elevation = 10
back_size = [100, 50]
back_POS_X = Misc.display_width - back_size[0] - 80

# create scoreboard link list
def gameScoreboard():
    scoreboard = True
    players = []
    #Score.newll.printList()

    test = Score.newll.printList()

    while test.isEmpty() is False:
        players.append(test.pop())

    # SCROLL
    scroll_pos = 0
    scroll_limit = (len(players) - 8) * POS_Y_gap + 20

    while scoreboard:
        #  UPPER SCROLL LIMIT
        if scroll_pos > 0:
            scroll_pos = 0
        # LOWER SCROLL LIMIT
        if scroll_pos < -scroll_limit:
            if scroll_limit >= 0:
                scroll_pos = -scroll_limit
            else:
                scroll_pos = 0

        Misc.gameDisplay.fill(Misc.BLACK)
        Misc.message_to_screen("SCOREBOARD", Misc.WHITE, scroll_pos + title_POS, "XL")
        Misc.message_to_screen_uncentered("Player", Misc.WHITE, scroll_pos + name_POS_Y - POS_Y_gap, "M", name_POS_X)
        Misc.message_to_screen_uncentered("Score", Misc.WHITE, scroll_pos + name_POS_Y - POS_Y_gap, "M", score_POS_X)

        replay_pox_y = scroll_pos + name_POS_Y
        for i in range(len(players)):
            pos_y = replay_pox_y + i * POS_Y_gap
           # print players[i]
            #print players[i][0]
            Misc.message_to_screen_uncentered(players[i][0], Misc.WHITE, pos_y, "S", name_POS_X)
            Misc.message_to_screen_uncentered(players[i][1], Misc.WHITE, pos_y, "S", score_POS_X)
            Misc.button("REPLAY", replay_POX_X, pos_y - replay_elevation, replay_size[0], replay_size[1], Misc.GREY, Misc.WHITE, "S")

        back_pos_y = scroll_pos + name_POS_Y + len(players) * POS_Y_gap
        Misc.button("BACK", back_POS_X, back_pos_y, back_size[0], back_size[1], Misc.GREY, Misc.WHITE, "S")

        # INPUT HANDLING
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            # Button Events
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button is 1:
                    POS_X, POS_Y = pygame.mouse.get_pos()
                    # Back Button
                    if (back_POS_X < POS_X < back_POS_X + back_size[0] and back_pos_y < POS_Y < back_pos_y + back_size[1]):
                        scoreboard = False
                    # Replay Buttons
                    elif (replay_POX_X < POS_X < replay_POX_X + replay_size[0] and replay_pox_y < POS_Y < replay_pox_y - replay_elevation + (len(players)-1) * POS_Y_gap + replay_size[1]):
                        button_pos = POS_Y - (name_POS_Y - replay_elevation) - scroll_pos
                        if button_pos % POS_Y_gap <= replay_size[1]:
                            Play.play_game_seed(players[button_pos / POS_Y_gap][2])
                            scoreboard = False
                            #print players[button_pos / POS_Y_gap][2]
                if event.button is 4:
                    scroll_pos -= scroll_speed
                if event.button is 5:
                    scroll_pos += scroll_speed

        # # UP and DOWN button scrolling
        # if pygame.key.get_pressed()[pygame.K_UP]:
        #     scroll_pos -= scroll_speed
        # if pygame.key.get_pressed()[pygame.K_DOWN]:
        #     scroll_pos += scroll_speed

        pygame.display.flip()

        Misc.refresh()
