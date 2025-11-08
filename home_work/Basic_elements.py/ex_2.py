import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.salesforce.com/")

forget = driver.find_element(By.CSS_SELECTOR, "#forgot_password_link")
forget.click()
title = driver.title

for text in title:
    if "rest your passward in title":
        continue
    else:
        print("error you ere in the wrong page")
 
driver.find_element(By.CSS_SELECTOR, "#un").send_keys("beni sim")
driver.find_element(By.CSS_SELECTOR, "#continue").click()

error_massage = driver.find_element(By.CSS_SELECTOR, "#username-error").text
print(error_massage)
