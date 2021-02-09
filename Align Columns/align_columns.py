def print_columns(text="", justify="left"):
    # Splt the words
    words = text.split('$')
    
    print(words) 
    
    # Find the longest word
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    column_width = len(longest_word)
   
    # Begin making columns
    for word in range(len(words)):
        this_word = " " * column_width
            
        if justify == "right":
            this_word = words[0].rjust(column_width)
        elif justify == "left":
            this_word = words[0].ljust(column_width)
        elif justify == "left":
            this_word = words[0].center(column_width)
                
            print(f"{this_word} ", end="")
            words.pop(0)

 


# Make it so word[0] prints \n within it, if so.
# Just go through each word and print the corresponing thing