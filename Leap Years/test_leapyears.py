from leapyears import leapyearOrNot

def test_commonYear_function():
    # No divisible by 4, 100, or 400.
    assert leapyearOrNot(2001) is False  # Common year
    
def test_typicalLeapYear_function():
    # Divisible by 4, but NOT by 100.
    assert leapyearOrNot(1996) is True  # Typical Leap year
    
def test_atypicalCommonYear_function():
    # Divisible by 4, but NOT by 400.
    assert leapyearOrNot(1900) is False  # Atypical common year
    
def test_atypicalLeapYear_function():
    # Divisible by 4, 100, and 400.
    assert leapyearOrNot(2000) is True  # Atypical Leap year
