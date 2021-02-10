def print_columns(text="", justify="left"):
    # Splt the words
    words = text.split('$')
    
    # Find the longest word
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    column_width = len(longest_word)

    # Begin making columns
    for word in words:
        this_word = None #" "  * column_width
            
        # Make sure \n is at end always
        newLine = False
        if '\n' in word:
            word = word[:-1]
            newLine = True
        
        if justify == "right":
            this_word = word.rjust(column_width)
        elif justify == "left":
            this_word = word.ljust(column_width)
        elif justify == "center":
            this_word = word.center(column_width)
                
        print(f"{this_word}", end="")
        
        if newLine:
            print("")
        else:
            print(" ", end="")
