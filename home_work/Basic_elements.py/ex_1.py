import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://prd.canvusapps.com/signup")

driver.find_element(By.ID, "user_name").send_keys("binymin sim")
driver.find_element(By.ID, "user_email").send_keys("benyaminsim1212@gamil.com")
driver.find_element(By.ID, "user_password").send_keys("beni3570")
driver.find_element(By.ID, "user_password_confirmation").send_keys("beni3570")
driver.find_element(By.ID, "company_name").send_keys("compie")

driver.find_element(By.NAME, "commit").click()

error_element = driver.find_element(By.CSS_SELECTOR, ".alert-error")
error_message = error_element.get_attribute("textContent")

print(error_message)






