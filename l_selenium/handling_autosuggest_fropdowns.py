import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")

time.sleep(2)


countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click() 
        break 
    
# How to get dynamic text values ? 
# ans = using get_attribute func like below 
 
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) 

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"