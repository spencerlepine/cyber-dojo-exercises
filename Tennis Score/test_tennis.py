from tennis import tennis

def test_tennis_duece():
    assert tennis(3, 3) == "Duece"

def test_tennis_advantage():
    assert tennis(4, 3) == "Advantage"
    
def test_tennis_winner_a():
    assert tennis(4, 2) == "Game - Player 1 wins"
    
def test_tennis_winner_b():
    assert tennis(2, 4) == "Game - Player 2 wins"
    
def test_tennis_midgame():
    assert tennis(2, 2) == "30 - 30"
    
def test_tennis_start():
    assert tennis(0, 0) == "love - love"