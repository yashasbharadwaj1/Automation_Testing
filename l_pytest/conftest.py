import pytest

@pytest.fixture(scope='class') 
def setup():
    # runs before tests execution
    print("I will be executing first") 
    yield 
    # runs after tests execution 
    print("I will be excecuted last ") 
    
@pytest.fixture()
def dataLoad():
    print("user profile is being created") 
    return ["Rahul","Shetty","rahulshettyacademy.com"] 


@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param 

