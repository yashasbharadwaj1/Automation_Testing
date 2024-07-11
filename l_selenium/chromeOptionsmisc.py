from selenium import webdriver 
from selenium.webdriver.common.by import By 

# to run in detached or headless mode 
# this means browser invocation 
# does not open on screen it runs in background

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# to handle ssl certificates errors
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 


driver.implicitly_wait(10) 


# to excecute javascript 

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screen_scrolled.png")

