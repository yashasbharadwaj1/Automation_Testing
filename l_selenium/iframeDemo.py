from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.implicitly_wait(6)

# iframe id or frame name can be passed comming from
# <iframe tag>
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.CSS_SELECTOR, "body p").clear

driver.find_element(By.CSS_SELECTOR, "body p").send_keys("hmm")


# it switches to normal selenium default scope
driver.switch_to.default_content()


heading = driver.find_element(By.TAG_NAME, "h3").text


print(heading)
