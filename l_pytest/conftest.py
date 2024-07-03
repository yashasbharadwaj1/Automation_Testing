import pytest

@pytest.fixture(scope='class') 
def setup():
    # runs before tests execution
    print("I will be executing first") 
    yield 
    # runs after tests execution 
    print("I will be excecuted last ")