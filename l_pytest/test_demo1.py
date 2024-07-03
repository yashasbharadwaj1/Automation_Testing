
import pytest 

@pytest.mark.smoke 
@pytest.mark.skip 
def test_first_program():
    num = 1 
    assert num == 1 

def test_CreditCard_1():
    card = "Credit Card"
    assert card == "Credit Card" 
