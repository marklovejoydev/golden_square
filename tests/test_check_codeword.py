from lib.check_codeword import*

def test_check_codeword_correct():
    codeword = check_codeword("horse")
    assert codeword == "Correct! Come in."
    
def test_check_codeword_close():
    codeword = check_codeword("hose")
    assert codeword == "Close, but nope."
    

def test_check_codeword_wrong():
    codeword = check_codeword("nope")
    assert codeword == "WRONG!"
    