from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

print("Testing Stated")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("LinkedIn")
time.sleep(1)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(1)
driver.get("https://www.linkedin.com/login")
driver.find_element_by_name("session_key").send_keys("7259504665")
driver.find_element_by_name("session_password").send_keys("lipigowda07")
driver.find_element_by_class_name("login__form_action_container ").click()
driver.find_element_by_id("ember27").click()
driver.find_element_by_id("ember28").click()
time.sleep(10)

driver.close()
print("Tested Successfully")