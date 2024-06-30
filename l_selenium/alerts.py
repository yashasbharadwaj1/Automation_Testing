import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/") 

name = "yashas"
driver.find_element(By.CSS_SELECTOR,"#name")\
.send_keys(name)

driver.find_element(By.ID,
"alertbtn").click() 

# Switching to alert mode
alert = driver.switch_to.alert
alertText =alert.text 
print(alertText)

assert name in alertText 

# to click on Ok
alert.accept()  
# to click on Cancel
#alert.dismiss() 

time.sleep(2)