from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://prd.canvusapps.com/signup")

driver.find_element(By.CSS_SELECTOR, "#user_name").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "#user_email").send_keys("testest@fgfg.rtt")
driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#user_password_confirmation").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#company_name").send_keys("ptestp")
driver.find_element(By.CSS_SELECTOR, ".submit.btn.btn-primary").click()

driver.find_element(By.CSS_SELECTOR, ".alert.alert-error.alert-block.error").text

driver.find_element(By.CSS_SELECTOR, ".span6.text-right a").click()
driver.find_element(By.CSS_SELECTOR, "p > a").click()

title_page = driver.find_element(By.TAG_NAME, 'h3').text
EX_title = "Forgot Your Password"
if EX_title.lower() in title_page.lower():
    print("you are in the right page")
else:
    print("you are in the wrong page")

driver.find_element(By.CSS_SELECTOR, "#email").send_keys("sss@ss.ss")
driver.find_element(By.CSS_SELECTOR, "[value='Reset Password']").click()

input('a')