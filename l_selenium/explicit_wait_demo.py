import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# implicit wait -- works as a global timeout
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)

# Implicit wait does 
# not work on find_elements 
# this is the only excpetion

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)

assert count > 0

# chaining of web elements
for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit wait for specific element
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

code_applied_msg = driver.find_element(By.CLASS_NAME, "promoInfo").text

#print(code_applied_msg) 

assert code_applied_msg == "Code applied ..!"
