def nextWordLength(string, width, currentIndex):
    currentIndex = currentIndex + 1  # Skip the current space

    for c in range(currentIndex, len(string)):
        if string[c] == ' ':  # Read until the next space is found
            return (c - currentIndex)
    
    # Couldn't break at word boundary, found end of string.
    return "END OF STRING"

def wordWrapper(string, width):
    if not isinstance(string, str):
        raise TypeError('Please provide a string argument')
        
    if not isinstance(width, int):
        raise TypeError('Please provide a number for width argument')
    
    newString = ''
    
    textWidthCounter = 0
    for i in range(len(string)):
        if textWidthCounter == 0 and string[i] == ' ':
            continue
            
        if i > 0:
            if string[i] == ' ':
                nextWord = nextWordLength(string, width, i)

                if nextWord != "END OF STRING":
                    if ((textWidthCounter == width) or
                    ((textWidthCounter + nextWord) >= width)):
                        newString += '\n'
                        textWidthCounter = 0
                        continue
                    
            elif (textWidthCounter > 0) and textWidthCounter % width == 0:
                newString += '{}\n'.format(string[i])
                textWidthCounter = 0
                continue
            
        newString += string[i]
        textWidthCounter += 1

    return newString
