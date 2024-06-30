import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

"""
selenium locators 
ID,XPATH,CSSSelector,Classname,
Name,LinkText
"""

# Inserting in Form

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#Static DropDown 
# if u see select tag dropdown go and use Select class
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female") 

#selects first 1
dropdown.select_by_index(0) 

# in case u have value attribute
#dropdown.select_by_value()


# Xpath syntax - //tagname[@attribute='value']
driver.find_element(By.XPATH,
"//input[@type='submit']").click()

#CSS selector syntax - tagname[attribute='value']  
#id , .classname 

driver.find_element(By.CSS_SELECTOR,"input[name='name']")\
.send_keys("Rahul")

driver.find_element(By.CSS_SELECTOR,
"#inlineRadio1")

message = driver.find_element(By.CLASS_NAME,
"alert-success").text

print(message) 

assert "Success" in message

driver.find_element(By.XPATH,
"(//input[@type='text'])[3]").send_keys("hemlo")

driver.find_element(By.XPATH,
"(//input[@type='text'])[3]").clear()


time.sleep(3)