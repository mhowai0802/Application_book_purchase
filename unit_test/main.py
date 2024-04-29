from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080")
# Login
element = driver.find_elements(By.CSS_SELECTOR, ".form-control")[0]
element.send_keys("Benjamin Davis")
element = driver.find_elements(By.CSS_SELECTOR, ".form-control")[1]
element.send_keys("strongPwd456")
driver.find_element(By.TAG_NAME, "button").click()
# Filter books
time.sleep(10)
driver.find_elements(By.TAG_NAME, "input")[0].send_keys("1984")
driver.find_elements(By.TAG_NAME, "button")[0].click()
time.sleep(10)
driver.find_elements(By.TAG_NAME, "input")[0].clear()
driver.find_elements(By.TAG_NAME, "input")[0].send_keys("Gone Girl")
driver.find_elements(By.TAG_NAME, "button")[0].click()
# Delete record
driver.find_elements(By.TAG_NAME, "input")[1].send_keys("1984")
driver.find_elements(By.TAG_NAME, "button")[1].click()
driver.close()