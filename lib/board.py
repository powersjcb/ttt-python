from piece import Piece

class Board:
    
    def __init__(self, **kwargs):
        options = {'board_size': 3}
        options.update(kwargs)
        self.board_size = options['board_size']
        self.board = [[None for x in range(self.board_size)] for y in range(self.board_size)]
        

