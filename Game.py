import Misc
import mainmap
import bomb
import num


class Tile_Status:
    opened, unopened, flagged = range(3)


class map_tiles:
    def __init__(self, game):
        self.map = {}# save this
        for pos in game.map.xymap:
            if pos not in game.bomb.mines:
                self.map[pos] = [Misc.call_tile(game.num.calculatepoint(game.num, pos, game.bomb)), Tile_Status.unopened]
            else:
                self.map[pos] = [Misc.call_tile(9), Tile_Status.unopened]

    def get_tile(self, pos):
        if self.map[pos][1] is Tile_Status.unopened:
            return Misc.call_tile(None)
        elif self.map[pos][1] is Tile_Status.opened:
            return self.map[pos][0]
        elif self.map[pos][1] is Tile_Status.flagged:
            return  Misc.call_tile(-1)

    def tile_status(self, pos):
        return self.map[pos][1]

    def open_tile(self, pos):
        self.map[pos][1] = Tile_Status.opened

    def toggle_flag(self, pos):
        if self.tile_status(pos) is Tile_Status.unopened:
            self.map[pos][1] = Tile_Status.flagged
        elif self.tile_status(pos) is Tile_Status.flagged:
            self.map[pos][1] = Tile_Status.unopened
    def get_map(self):
        return self.map

class Game:
    def __init__(self, (row,column,difficulty), seed=None):
        self.map = mainmap.Mainmap
        self.bomb = bomb.Bombs
        self.num = num.Num
        self.dead = False
        print "laststate: " + str(seed)
        if seed is None:
            # We have to create in this order at all cost!
            self.map.create(self.map, row, column)  # Create map of X and Y
            self.bomb.create(self.bomb, row, column, difficulty, self.map)  # Create Bomb maps of X andY with Z% of bombs
            self.num.create(self.num, self.map)  # Init neighbouring cell arrays
            self.size = row * column
        elif seed != "laststate":
            self.map.create(self.map, row, column)  # Create map of X and Y
            self.bomb.create(self.bomb, row, column, difficulty,
                             self.map)  # Create Bomb maps of X andY with Z% of bombs
            self.num.create(self.num, self.map)  # Init neighbouring cell arrays
            self.bomb.read(self.bomb, seed, self.map, self.num) # This point we have refreshed the data
            self.size = self.map.rows*self.map.columns
        else:
            self.map.create(self.map, row, column)  # Create map of X and Y
            self.bomb.create(self.bomb, row, column, difficulty,
                             self.map)  # Create Bomb maps of X andY with Z% of bombs
            self.num.create(self.num, self.map)  # Init neighbouring cell arrays
            print str(seed)
            self.bomb.readstate(self.bomb, seed, self.map, self.num)  # This point we have refreshed the data
            self.size = self.map.rows * self.map.columns

        self.game_tiles = map_tiles(self)
        self.start_x = (Misc.display_width - self.map.columns * Misc.pixel_size) / 2
        self.start_y = (Misc.display_height - self.map.rows * Misc.pixel_size) / 2
        for xy in self.map.preopened:
            open_tile(self, xy);

    def display(self):
        for pos in self.map.xymap:
            tile = self.game_tiles.get_tile(pos)
            coord = [self.start_x + pos[0] * Misc.pixel_size, self.start_y + pos[1] * Misc.pixel_size]
            Misc.gameDisplay.blit(tile, coord)

    def death_event(self):
        for pos in self.bomb.mines:
            self.game_tiles.map[pos][1] = Tile_Status.opened

    def victory_event(self):
        for pos in self.bomb.mines:
            self.game_tiles.map[pos] = [Misc.call_tile(-2), Tile_Status.opened]

    def check_win(self):
        if len(self.map.opened) is self.size - len(self.bomb.mines):
            self.victory_event()
            return True

    def open_tile(self, pos):
        if pos in self.map.xymap and pos not in self.map.opened:
            self.game_tiles.open_tile(pos)
            dead = self.map.open(self.map, pos, self.bomb, self.num)
            if not dead:
                return self.num.calculatepoint(self.num, pos, self.bomb)
            else:
                self.death_event()
                return -1

    def toggle_flag(self, pos):
        if pos in self.map.xymap:
            if self.game_tiles.tile_status(pos) is not Tile_Status.opened:
                self.game_tiles.toggle_flag(pos)

    def get_seed_name(self):
        return self.bomb.dumpmap(self.bomb,self.map)

    def save_state(self):
        return self.bomb.dumpmap2(self.bomb,self.map)

def open_tile(game, pos):
    if game.game_tiles.tile_status(pos) is not Tile_Status.flagged:
        pos_no = game.open_tile(pos)
        if pos_no is 0:
            for neighbour in game.num.neighbours[pos]:
                if game.game_tiles.tile_status(neighbour) is Tile_Status.unopened:
                    open_tile(game, neighbour)
        elif pos_no is -1:
            return True
