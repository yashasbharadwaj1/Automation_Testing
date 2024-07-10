from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.implicitly_wait(5) 

driver.maximize_window()

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click() 

vegetablesWebElementsList = driver.find_elements(By.XPATH,"//tr/td[1]")

browserSortedVegetables = []
for vegetable in vegetablesWebElementsList:
    browserSortedVegetables.append(vegetable.text)

originalBrowserSortedVegetables = browserSortedVegetables.copy() 

browserSortedVegetables.sort() 

assert browserSortedVegetables ==originalBrowserSortedVegetables

