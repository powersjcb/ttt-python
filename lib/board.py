from piece import Piece

class Board:
    
    def __init__(self, **kwargs):
        options = {'board_size': 3}
        options.update(kwargs)
        self.board_size = options['board_size']
        self.grid = [[None for x in range(self.board_size)] for y in range(self.board_size)]

    def flattened_grid(self):
        flat = []
        for row in self.grid:
            for item in row:
                flat.append(item)
        return flat

    def get(self, pos):
        return self.grid[pos['row']][pos['col']]

    def set(self, pos, color):
        print pos
        if not self.on_board(pos):
            raise InvalidMoveError('position is off the board')
        elif self.get(pos) is not None:
            raise InvalidMoveError('Space allready occupied')
        p = Piece(self, pos, color)
        self.grid[pos['row']][pos['col']] = p
        return None

    def on_board(self, pos):
        s = self.board_size
        return pos['row'] >= 0 and pos['col'] >= 0 and pos['row'] < s and pos['col'] < s





class InvalidMoveError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
