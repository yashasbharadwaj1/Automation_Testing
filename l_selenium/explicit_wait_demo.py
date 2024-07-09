import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

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

expected_names_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actual_product_names_list = []
for result in results:
    product_name = result.find_element(By.CSS_SELECTOR, "h4[class='product-name']").text
    actual_product_names_list.append(product_name)

print(actual_product_names_list)

assert expected_names_list == actual_product_names_list

# chaining of web elements
for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p[class='amount']")
price_sum = 0
for price in prices:
    price_sum = price_sum + int(price.text)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

print(f"Total amount :- {total_amount}")
assert price_sum == total_amount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit wait for specific element
wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))
)

code_applied_msg = driver.find_element(By.CLASS_NAME, "promoInfo").text

# print(code_applied_msg)

assert code_applied_msg == "Code applied ..!"

total_discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(f"Total discount :- {total_discount}")
assert total_discount < total_amount
