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


# parametarization
# sending multilple data
@pytest.fixture(params=[("chrome","Rahul"),("Firefox","Shetty"),("IE")])
def crossBrowser(request):
    return request.param 

