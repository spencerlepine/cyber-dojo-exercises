from lcd import print_lcd

def test_prints_zero(capsys):
    print_lcd(0)
    
    captured = capsys.readouterr()
    assert captured.out == " _ \n| |\n|_|\n"


def test_prints_big_num(capsys):
    print_lcd(90210)
    
    captured = capsys.readouterr()
    assert captured.out == " _  _  _     _ \n|_|| | _|  || |\n  ||_||_   ||_|\n"