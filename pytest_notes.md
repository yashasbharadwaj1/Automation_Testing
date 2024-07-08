pytest notes and commands 


Any pytest file should start with test_ 
pytest methods shoud start with test_ 
Any code should be wrapped in methods only
Method name should make sense 

py.test  - to run all tests in the project . hit this command from root level

to run tests in a specific file
py.test test_demo2.py -v -s 

-v is verbose more info like metadata, -s also prints any print statements to stdout included in our tests 

to run specific tests based on regular expression matching function name 
use -k 
py.test -k CreditCard 

to run only tests which are marked or tagged with some name using @pytest.mark somename 

py.test -m smoke 

you can skip tests with @pytest.mark.skip  

@pytest.mark.xfail is used to mark tests that are known to fail due to a bug or unimplemented feature. This helps in tracking such tests without cluttering the test report with failures you're already aware of.


@pytest.fixture is a decorator in the pytest testing framework that defines a fixture function. 
Fixtures provide a way to set up some initial state or dependency that your tests need. They are useful for code reuse and managing setup and teardown logic in a clean and modular way.

Key Points
Setup and Teardown: Fixtures can handle setup and teardown operations, which are actions that need to be performed before and after a test runs.

Reusability: Fixtures allow you to define common setup logic that can be reused across multiple tests, reducing code duplication.

Dependency Injection: Fixtures are injected into test functions via their function arguments. This makes it easy to share state and dependencies between tests.

Scope: Fixtures can have different scopes (function, class, module, session) which control how often the fixture is invoked:

function: Default scope, the fixture is invoked for each test function.
class: The fixture is invoked once per class of tests.
module: The fixture is invoked once per module.
session: The fixture is invoked once per test session.

for the fixtures to be available across all the tests 
u need to write them in conftest.py 


@pytest.mark.usefixtures("setup") 
instaed of passing fixtures names to every test function we can make use of decorator 
@pytest.mark.usefixtures("setup") to run for the entire class 

@pytest.fixture(scope='class') 
class: The fixture is invoked once per class of tests.

to generate html report for all tests 

pip install pytest-html 

then run the below command 

py.test --html=report.html 

