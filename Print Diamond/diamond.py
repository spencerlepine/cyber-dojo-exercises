alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def print_diamond(letter):
    letterCount = alphabet.index(letter);
    lineCount = letterCount + letterCount + 1
    middle = ( (lineCount + 2 // 2) // 2 ) - 1 # Convert to index format

    # Print top of diamond
    for r in range(middle):
        for c in range(lineCount):
            if (c == middle-r or c == middle+r):
                print(alphabet[r], end="")
            else:
                print(" ", end="")
                
        print('')
    
    # Print bottom of diamond
    for c in range(lineCount):
        if (c == middle-middle or c == middle+middle):
            print(alphabet[middle], end="")
        else:
            print(" ", end="")
            
    print('')
                
    # Print bottom of diamond
    for r in range(middle-1, -1, -1):
        for c in range(lineCount):
            if (c == middle-r or c == middle+r):
                print(alphabet[r], end="")
            else:
                print(" ", end="")
                        
        print('') # Finish the line with auto '\n'
            
