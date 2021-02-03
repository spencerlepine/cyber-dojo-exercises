def digitCount(numStr):
    numbersFound = [0] * 10

    for c in numStr: 
        numbersFound[int(c)] += 1
        
    return numbersFound
        
def generate_wonderland():
    toMult = [2, 4, 5, 6]
    
    for i in range(111111, 999999):
        thisNumber = digitCount(str(i)) # => '111111'
        
        for n in toMult:
            if thisNumber == digitCount(str(n *i)):
                return i
        