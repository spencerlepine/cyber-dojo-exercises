def score_word(score):
    words = ['love', '15', '30', '40']
    return words[score] # Score == 0 - 3

def tennis(score1, score2):
    # Winner if a score is greater by two AND >= 4
    if (score1 > 3 and score2 + 2 <= score1):
        return "Game - Player 1 wins"
    elif (score2 > 3 and score1 + 2 <= score2):
        return "Game - Player 2 wins"    
        
    if (score1 >= 3 and score2 >= 3):
        if (score1 != score2):
            return "Advantage"
        else:
            return "Duece"
        
    # Game is still underway
    return f"{score_word(score1)} - {score_word(score2)}"