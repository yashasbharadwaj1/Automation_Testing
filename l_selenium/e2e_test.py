import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(6)

# a[href='/angularpractice/shop'] --> by using regular expression (*) is written as a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

ProductWebElements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")


for productElement in ProductWebElements:
    title = productElement.find_element(By.XPATH, "div/h4/a").text
    if title == "Blackberry":
        productElement.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()


driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()


driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()


successText = driver.find_element(
    By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
).text

print(successText)

assert "Success! Thank you!" in successText
