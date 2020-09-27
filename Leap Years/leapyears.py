def leapyearOrNot(year):
    # Check if year is divisible by 100 (implicitly tests "% 4")
    if year % 100 == 0:
        if year % 400 == 0:
            # Yes, I am a leap year!!
            return True
    
    # One last check to see if it is divisible by 4.
    elif year % 4 == 0:
        return True
   
    return False
