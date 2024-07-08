import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")


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


code_applied_msg = driver.find_element(By.CLASS_NAME, "promoInfo").text

print(code_applied_msg)
