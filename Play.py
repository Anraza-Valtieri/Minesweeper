import pygame
import Misc
import Game
import HighScores
import cPickle as pickle
import userInput
# import picklec

timer_pos = [0, 0]

newGame = True
endGame = False
def play_game_seed(seed):
    """
    Call this and Pass the seed file name here in args to load mine files

    :param self:
    :param name:
    :return:
    
    easy_mode = (8, 8, 0.1)
    medium_mode = (12, 12, 0.15)
    hard_mode = (20, 16, 0.25)
    """
    mapdata_col = 0
    mapdata_row = 0
    try:
        with open(seed, 'rb') as fp:
            loadeddata = set()
            loadeddata = pickle.load(fp)
            mapdata_col = loadeddata[0]
            print "Read Col: " + str(loadeddata[0])
            mapdata_row = loadeddata[1]
            print "Read Row: " + str(loadeddata[1])
        data = (mapdata_col,mapdata_row,0.1)
        print str(data) + str(seed)
        play_game(data,seed)
    except:
        print "PLAY: Failed to load " + str(seed)



def play_game(game_size, seed):
    game_exit = False
    game_over = False
    game_victory = False
    game_time = 0
    global current_game
    print str(seed)
    if(seed == ""):
        current_game = Game.Game(game_size)
    else:
        current_game = Game.Game(game_size,seed)

    while not game_exit:
        # GAME OVER event
        while game_over is True:
            Misc.message_to_screen("Game Over", Misc.LIGHT_RED, -50, "L")
            Misc.message_to_screen("Press C to continue. Press Q to quit.", Misc.LIGHT_RED, 50)
            Misc.refresh()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type is pygame.KEYDOWN:
                    if event.key is pygame.K_q:
                        return endGame
                    if event.key is pygame.K_c:
                        return newGame

        # VICTORY event
        if game_victory is True:
            while game_victory is True:
                Misc.message_to_screen("YOU WIN", Misc.GREEN, -50, "L")
                Misc.message_to_screen("Press C to continue. Press Q to quit.", Misc.GREEN, 50)
                Misc.refresh()

                for event in pygame.event.get():
                    if event.type is pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type is pygame.KEYDOWN:
                        if event.key is pygame.K_q:
                            seed = current_game.get_seed_name()
                            HighScores.enterName(str(game_time / 60), seed)
                            return endGame
                        if event.key is pygame.K_c:
                            seed = current_game.get_seed_name()
                            HighScores.enterName(str(game_time / 60), seed)
                            return newGame

        # Input Handling
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos_x = (pygame.mouse.get_pos()[0] - current_game.start_x) / Misc.pixel_size
                pos_y = (pygame.mouse.get_pos()[1] - current_game.start_y) / Misc.pixel_size
                pos = (pos_x, pos_y)
                if 0 <= pos_x < game_size[0] and 0 <= pos_y < game_size[1]:
                    # LEFT CLICK
                    if event.button is 1:
                        game_over = Game.open_tile(current_game, pos)
                        if not game_over:
                           game_victory = current_game.check_win()
                    # RIGHT CLICK
                    elif event.button is 3:
                        current_game.toggle_flag(pos)
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_p:
                    game_exit = game_pause()
                elif event.key is pygame.K_o:
                    game_victory = True
            # gameOver = True

        # CHICKEN MODE
     #   print (pygame.mouse.get_pos()[0]-Misc)/Misc.pixel_size
    #    print [self.start_x + pos[0] * Misc.pixel_size, self.start_y + pos[1] * Misc.pixel_size]

        # GAME Handling
        Misc.gameDisplay.fill(Misc.BLACK)
        current_game.display()
        Misc.timer(game_time, Misc.LIGHT_RED, timer_pos)
        pygame.display.update()
        game_time = Misc.tick(game_time)

def game_pause():
    Misc.message_to_screen("GAME PAUSED", Misc.WHITE, -50, "L")
    Misc.message_to_screen("Press c to continue. s to save the current state, Press q to quit.", Misc.WHITE, 50, "S")
    Misc.refresh()
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                quit()
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_c:
                    return False
                if event.key is pygame.K_q:
                    return True
                if event.key is pygame.K_s:
                    # save game_time
                    current_game.save_state()
                    return True
