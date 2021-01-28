from diamond import print_diamond

def test_function_prints(capsys):
    print_diamond("A")
    
    captured = capsys.readouterr()
    assert captured.out != ''

def test_diamond_a(capsys):
    print_diamond("A")
    
    captured = capsys.readouterr()
    assert captured.out == "A\n"

def test_diamond_b(capsys):
    print_diamond("B")
    
    captured = capsys.readouterr()
    assert captured.out == " A \nB B\n A \n"
    
def test_diamond_d(capsys):
    print_diamond("D")
    
    captured = capsys.readouterr()
    
    assert captured.out == "   A   \n  B B  \n C   C \nD     D\n C   C \n  B B  \n   A   \n"