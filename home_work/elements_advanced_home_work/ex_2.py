from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()


wait = WebDriverWait(driver, 10) 
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item_description")))

product_area_list = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_description")

for area in product_area_list:
    product_area = area.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    if product_area == "Sauce Labs Onesie" or product_area == "Sauce Labs Bolt T-Shirt":
        driver.find_element(By.CSS_SELECTOR, "[id^='add-to-cart']").click()
       
    
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link")))
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("beni")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("sim")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "#continue").click()

driver.find_element(By.CSS_SELECTOR, "#finish").click()

masg = driver.find_element(By.CSS_SELECTOR, ".complete-header").text
print(masg)

