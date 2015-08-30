import pytest

from lib.piece import Piece
from lib.board import Board, InvalidMoveError
from itertools import chain

class TestBoard:

    def setup_method(self, method):
        self.b = Board()
        self.valid_pos = {'row': 0, 'col': 1}
        self.invalid_pos = {'row': 0, 'col': -5}
        self.color = 'red'

    def test_default_board_size(self):
        assert len(self.b.grid) == 3 

    def test_board_is_seeded_with__none(self):
        flat_grid = self.b.flattened_grid()
        assert all(val is None for val in flat_grid)

    def test_board_set_with_invalid_pos(self):
        with pytest.raises(InvalidMoveError) as excinfo:
            self.b.set(self.invalid_pos, self.color)
        assert 'position is off the board' in str(excinfo.value)

    def test_board_set_valid(self):
        self.b.set(self.valid_pos, self.color)

        assert isinstance(self.b.get(self.valid_pos), Piece)

    def test_board_set_invalid(self):
        self.b.set(self.valid_pos, self.color)
        
        with pytest.raises(InvalidMoveError) as excinfo:
            self.b.set(self.valid_pos, self.color)
        assert 'Space allready occupied' in str(excinfo.value)



