import string
import game
import pytest

def test_show_board(capfd):
    output, _ = capfd.readouterr()
    game.show_board(board=[
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ])
    assert type(output) == str
    assert set(output) < set("|_XO ")

def test_show_board_full(capfd):
    output, _ = capfd.readouterr()
    game.show_board(board=[
        ["X", "Y", "ZZZ"],
        ["O", "O", "O"],
        [None, True, 2],
    ])
    assert type(output) == str
    assert set(output) < set('xy')
