import pytest 

@pytest.mark.smoke
def test_second_program():
    message = "Hello" 
    assert message == "Hi" , "Test failed because strings do not match" 
    
def test_third_program():
    a= 4
    b= 6 
    assert a+2 == b,"Test failed because Addition does not match" 

@pytest.mark.xfail
def test_CreditCard_2():
    card_no = 111
    assert card_no == 111 

# parametirized fixture argument    
# this test runs 3 times as 3 params are passed to it
def test_crossBrowser(crossBrowser):
    print(crossBrowser) 
    print(crossBrowser[0])