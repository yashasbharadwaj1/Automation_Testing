import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Xpath syntax - //tagname[@attribute='value']->
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