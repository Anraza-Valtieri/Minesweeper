import pygame, userInput, Misc, Scoreboard,Score
fontobject = pygame.font.Font(None,35)


def read_highscore(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close

    high_score = 0

    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)

        if score > high_score:
            high_score = score
            high_name = name

    return high_name, high_score

def save_to_file(file_name, player_name, points):
    score_file = open(file_name, 'a')
    print (player_name + ",", points, score_file)
    score_file.close()


def enterName(score, seed):
    # Create nameInput Object
    nameinput = userInput.TextInput()
    highscore_menu = True

    while highscore_menu:
        Misc.gameDisplay.blit(Misc.bg, Misc.display_origin)

        pygame.draw.rect(Misc.gameDisplay,
                         Misc.BLACK,
                         ((Misc.display_width/2)-120,
                          (Misc.display_height/2)-10,
                          300, 50), 0)
        pygame.draw.rect(Misc.gameDisplay,
                         Misc.WHITE,
                         ((Misc.display_width/2)-122,
                          (Misc.display_height/2)-12,
                          304, 54), 1)
        Misc.gameDisplay.blit(fontobject.render("Name:", 1, Misc.LIGHT_GREEN),
                    ((Misc.display_width/2)-100, (Misc.display_height/2)))

        Misc.message_to_screen("Hall of Fame", Misc.LIGHT_YELLOW, 50 - Misc.display_height / 2, "XL")
        Misc.message_to_screen("Hit Enter/Return to Save", Misc.BLUE, Misc.display_height/2 - 330, "S",
                               Misc.display_width /2 - 370)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Feed it with events every frame
        if nameinput.update(events):
            # nameinput.get_playerName()
            playerName = nameinput.get_text()
            if playerName == None or len(playerName) == 0:
                return  # do not update unless player enter his/her name
            elif playerName.isalpha():
                highscore_menu = False
                #Scoreboard.players.append([playerName, score, 'seed'])

                Score.newll.insert(playerName, int(score), seed)

                Scoreboard.gameScoreboard()
            else:
                Misc.message_to_screen("Name is not valid!", Misc.RED, 0, "S")

        # Blit its surface onto the screen
        Misc.gameDisplay.blit(nameinput.get_surface(), ((Misc.display_width/2)-20, Misc.display_height/2))

        pygame.display.update()
