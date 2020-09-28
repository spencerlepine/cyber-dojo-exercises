from doors import changeDoors, skipModulus, Door

def test_changeDoors_function():
    # Does changeDoors return the full array of objects?
    assert len(changeDoors()) == 100

def test_doorStartsClosed_method():
    doorTest = Door()
    
    assert doorTest.position == 'Closed'

def test_doorToggle_method():
    doorTest = Door()
    doorTest.toggle()
    
    assert doorTest.position == 'Open'
    
def test_doorsStepOne_function():
    assert 'Closed' not in changeDoors(1)

def test_skipModulusOne_function():
    assert skipModulus(100, 1) == 100
    
def test_skipModulusThree_function():
    assert skipModulus(100, 3) == 33
    
def test_skipModulusFour_function():
    assert skipModulus(100, 4) == 25
    