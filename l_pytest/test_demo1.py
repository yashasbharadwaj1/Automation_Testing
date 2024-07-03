# Any pytest file should start with test_ 
# pytest methods shoud start with test_ 
# Any code should be wrapped in methods only
# Method name should make sense 
# you can skip tests with @pytest.mark.skip 


import pytest 

@pytest.mark.smoke 
@pytest.mark.skip 
def test_first_program():
    num = 1 
    assert num == 1 

def test_CreditCard_1():
    card = "Credit Card"
    assert card == "Credit Card" 
