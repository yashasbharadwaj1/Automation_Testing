from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

wrong_password = "password"


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(6)

driver.find_element(
    By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material"
).click()

windowsOpenedList = driver.window_handles

driver.switch_to.window(windowsOpenedList[1])

email = driver.find_element(By.CSS_SELECTOR, "p[class='im-para red'] strong").text

# print(email)

assert email == "mentor@rahulshettyacademy.com"

array = email.split("@")
var = array[1]
array1 = var.split(".")
username = array1[0]

# print(username)

driver.close()

driver.switch_to.window(windowsOpenedList[0])

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)


driver.find_element(By.CSS_SELECTOR, "#password").send_keys(wrong_password)

driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-danger")
    )
)
error_msg = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text

# print(error_msg)

assert error_msg == "Incorrect username/password."
