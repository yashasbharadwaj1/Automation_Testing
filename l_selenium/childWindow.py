import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

driver.implicitly_wait(5)

driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()

# it returns lists of  windows opened by selenium driver order wise 
windowsOpenedList = driver.window_handles

# print(windowsOpenedList)

# to switch the scope of driver between windows
driver.switch_to.window(windowsOpenedList[1])

child_window_msg = driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text

print(child_window_msg)
assert child_window_msg == "New Window"

driver.close()


driver.switch_to.window(windowsOpenedList[0])

parent_window_msg = driver.find_element(By.TAG_NAME, "h3").text

print(parent_window_msg)

assert parent_window_msg == "Opening a new window"
