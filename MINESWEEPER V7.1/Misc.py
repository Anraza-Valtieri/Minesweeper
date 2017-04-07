import pygame

pygame.init()
pygame.display.set_caption('Minesweeper')
pygame.display.set_icon(pygame.image.load('img//MINESWEEPER_M.png'))

playerlist =[]
test_game = None



# COLORS
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHT_RED = (255, 0, 0)
GREEN = (0, 155, 0)
LIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
GAME_COLOR = BLACK

EZ_SENSOR = False
def ez_sensor(action, color):
    scale = 2
    norm = 0
    mid_alert = 50
    alert = 100
    if action is 'increase':
        if color[0] + scale < mid_alert:
            color = (color[0] + scale, 0, 0)
        elif color[0] < mid_alert:
            color = (color[0] + 1, 0, 0)
        elif mid_alert <= color[0] < alert:
            color = (color[0] - scale, 0, 0)
        elif mid_alert <= color[0] - scale < alert:
            color = (color[0] - scale, 0, 0)
        elif mid_alert <= color[0] - scale < alert:
            color = (color[0] - 1, 0, 0)
    elif action is 'INCREASE':
        if color[0] + scale < alert:
            color = (color[0] + scale, 0, 0)
        elif color[0] < alert:
            color = (color[0] + 1, 0, 0)
    elif action is 'decrease':
        if color[0] - scale > norm:
            color = (color[0] - scale, 0, 0)
        elif color[0] > norm:
            color = (color[0] - 1, 0, 0)
    return color

# RESOLUTION
display_width = 1024
display_height = 768
gameDisplay = pygame.display.set_mode((display_width, display_height))
display_origin = (0, 0)

# FONTS
FONT = ""
XSfont = pygame.font.SysFont(FONT, 8)
Sfont = pygame.font.SysFont(FONT, 25)
Mfont = pygame.font.SysFont(FONT, 50)
Lfont = pygame.font.SysFont(FONT, 80)
XLfont = pygame.font.SysFont(FONT, 120)
XXLfont = pygame.font.SysFont(FONT, 200)
# FRAME RATE
clock = pygame.time.Clock()
frame_rate = 60
timer_offset = [10, 8]

# SPRITES
pixel_size = 44
tile = pygame.image.load('img//COVERED.jpg')
tile_mine = pygame.image.load('img//MINESWEEPER_M.png')
tile_clear = pygame.image.load('img//CLEAR.png')
tile_flag = pygame.image.load('img//MINESWEEPER_F.png')
tile_clock = pygame.image.load('img//MINESWEEPER_C.png')
tile_empty = pygame.image.load('img//MINESWEEPER_0.png')
tile_1 = pygame.image.load('img//MINESWEEPER_1.png')
tile_2 = pygame.image.load('img//MINESWEEPER_2.png')
tile_3 = pygame.image.load('img//MINESWEEPER_3.png')
tile_4 = pygame.image.load('img//MINESWEEPER_4.png')
tile_5 = pygame.image.load('img//MINESWEEPER_5.png')
tile_6 = pygame.image.load('img//MINESWEEPER_6.png')
tile_7 = pygame.image.load('img//MINESWEEPER_7.png')
tile_8 = pygame.image.load('img//MINESWEEPER_8.png')
wallpaper = pygame.image.load('img//maxresdefault.jpg')
bg = pygame.image.load("img//bg.jpg")
bg = pygame.transform.scale(bg, (display_width, display_height))


# DIFFICULTY
easy = "EASY MODE"
medium = "MEDIUM MODE"
hard = "HARD MODE"
easy_mode = (8, 8, 0.1)
medium_mode = (12, 12, 0.15)
hard_mode = (20, 16, 0.25)
default_diff = easy_mode
difficulty = default_diff


def set_difficulty(mode, diff):
    if mode is easy:
        diff = easy_mode
    elif mode is medium:
        diff = medium_mode
    elif mode is hard:
        diff = hard_mode
    else:
        diff = default_diff
    return diff


def refresh():
    pygame.display.update()


# LABELS
def text_objects(msg, color, size):
    if size is "XS":
        text_surface = XSfont.render(msg, True, color)
    elif size is "S":
        text_surface = Sfont.render(msg, True, color)
    elif size is "M":
        text_surface = Mfont.render(msg, True, color)
    elif size is "L":
        text_surface = Lfont.render(msg, True, color)
    elif size is "XL":
        text_surface = XLfont.render(msg, True, color)
    elif size is "XXL":
        text_surface = XXLfont.render(msg, True, color)

    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="S", x_displace=0):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2) + x_displace, (display_height/2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


def message_to_screen_uncentered(msg, color, y_displace=0, size="S", x_displace=0):
    text_surf, text_rect = text_objects(msg, color, size)
    gameDisplay.blit(text_surf, [x_displace, y_displace])


# BUTTONS
def text_to_button(msg, color, button_x, button_y, button_width, button_height, size="S"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (button_x + button_width / 2), (button_y + button_height / 2)
    gameDisplay.blit(text_surf, text_rect)


def button(text, button_x, button_y, button_width, button_height, color, hover_color, size="S"):
    cur = pygame.mouse.get_pos()
    if button_x + button_width > cur[0] > button_x and button_y + button_height > cur[1] > button_y:
        pygame.draw.rect(gameDisplay, hover_color, (button_x, button_y, button_width, button_height))
    else:
        pygame.draw.rect(gameDisplay, color, (button_x, button_y, button_width, button_height))
    text_to_button(text, BLACK, button_x, button_y, button_width, button_height, size)


# TILES
def call_tile(tile_no):
    if tile_no is -2:
        return tile_clear
    elif tile_no is -1:
        return tile_flag
    elif tile_no is 0:
        return tile_empty
    elif tile_no is 1:
        return tile_1
    elif tile_no is 2:
        return tile_2
    elif tile_no is 3:
        return tile_3
    elif tile_no is 4:
        return tile_4
    elif tile_no is 5:
        return tile_5
    elif tile_no is 6:
        return tile_6
    elif tile_no is 7:
        return tile_7
    elif tile_no is 8:
        return tile_8
    elif tile_no is 9:
        return tile_mine
    elif tile_no is 10:
        return tile_clock
    else:
        return tile


# TIMER
def timer(frame_count, color, pos):
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    gameDisplay.blit(call_tile(10), pos)
    output_string = "{0:02}:{1:02}".format(minutes, seconds)
    message_to_screen_uncentered(
        output_string,
        color,
        pos[1] + timer_offset[1],
        "M",
        pos[0] + timer_offset[0] + pixel_size
    )


def tick(frame_count):
    frame_count += 1
    clock.tick(frame_rate)
    return frame_count
