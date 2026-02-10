import mangman2


def test_create_game_lives():
    lives, blank_space, guessed_letters = mangman2.create_game("dog")
    assert lives == 6


def test_create_game_blank_spaces():
    lives, blank_space, guessed_letters = mangman2.create_game("dog")
    assert blank_space == ["_", "_", "_"]


def test_create_game_guessed_letters_empty():
    lives, blank_space, guessed_letters = mangman2.create_game("dog")
    assert guessed_letters == []


def test_game_over_win():
    assert mangman2.game_over(["d", "o", "g"], 3) == True


def test_game_over_loss():
    assert mangman2.game_over(["_", "_", "_"], 0) == True

