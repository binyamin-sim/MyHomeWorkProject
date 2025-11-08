from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

current_title_1 = driver.title
if current_title_1 == "selenium web site" or "Selenium" in current_title_1:
    print("yes")
else:
    print("no")

driver.get("https://www.google.com")
current_title_2 = driver.title
if current_title_2 == "Google" or "google" in current_title_2:
    print("yes")
else:
    print("no")

driver.back()
current_title_1 = driver.title
if current_title_1 == "selenium web site" or "Selenium" in current_title_1:
    print("yes")
else:
    print("no")

