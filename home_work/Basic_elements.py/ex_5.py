from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.salesforce.com/")


driver.find_element(By.CSS_SELECTOR, "#username").send_keys("beni sim")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("beni1234")

check_box_el = driver.find_element(By.CSS_SELECTOR, "#rememberUn")
check_box_el.click()
is_selecet = check_box_el.is_selected()

if is_selecet:
    driver.find_element(By.CSS_SELECTOR, "#Login").click()
    error_masg = driver.find_element(By.CSS_SELECTOR, "#error").text
    print(error_masg)
else:
    print("you need firstable checked the check box")


input("jjj")