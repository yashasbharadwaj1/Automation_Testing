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