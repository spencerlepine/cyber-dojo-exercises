from wordwrap import wordWrapper, nextWordLength
import pytest

def test_wordWrapper_takes_two_arg_function():
    with pytest.raises(TypeError):
        wordWrapper('Lorem Ipsum', 10, 'Arg3')
        
def test_raises_exception_on_non_int_arguments():
    with pytest.raises(TypeError):
        wordWrapper('Lorem Ipsum', 'StringNotInt')

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        wordWrapper(9, 10)  # 9 is in the string place
        
def test_function_returns_string():
    isReturnString = wordWrapper('Lorem Ipsum', 10)
    assert isinstance(isReturnString, str)
        
def test_string_returned_contains_new_line():
    sampleString = "Lorem Ipsum is simply dummy text of the printing..."
    textWidth = 15
    
    stringToCheck = wordWrapper(sampleString, textWidth)
    
    if len(sampleString) > textWidth:  # Only if it would need a new line
        assert '\n' in stringToCheck

# try to break lines at word boundaries.
def test_string_breaks_at_word_boundary():
    sampleString = "Lorem Ipsum is simply dummy text of the printing and..."
    textWidth = 25
    
    answerString = "Lorem Ipsum is simply\ndummy text of the\nprinting and..."
    
    stringToCheck = wordWrapper(sampleString, textWidth)
    
def test_nextWordLength_returns_length():
    sampleString = "Lorem Ipsum is simply dummy text of"
    textWidth = 10
    currentIndex = 5  # "_Ip'
    
    wordLengthToCheck = nextWordLength(sampleString, textWidth, currentIndex)
    
    assert wordLengthToCheck == 5

#def test_long_paragraph_breaks_accurately():
    #sampleString = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    #stringToCheck = wordWrapper(sampleString, 25)
    
    #answerString = "Lorem Ipsum is simply\ndummy text of the\nprinting and typesetting\nindustry. Lorem Ipsum has\nbeen the industry's\nstandard dummy text ever\nsince the 1500s, when an\nunknown printer took a\ngalley of type and\nscrambled it to make a\ntype specimen book. It\nhas survived not only\nfive centuries, but also\nthe leap into electronic\ntypesetting, remaining\nessentially unchanged. It\nwas popularised in the\n1960s with the release of\nLetraset sheets\ncontaining Lorem Ipsum\npassages, and more\nrecently with desktop\npublishing software like\nAldus PageMaker including\nversions of Lorem Ipsum."
    
    #assert answerString == stringToCheck
    
