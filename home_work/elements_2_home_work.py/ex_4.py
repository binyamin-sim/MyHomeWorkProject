from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://whatismyipaddress.com/")

ip_address = driver.find_element(By.CSS_SELECTOR, "#ipv4 a").text
print(ip_address)

driver.get("https://apps.db.ripe.net/db-web-ui/query")


wait = WebDriverWait(driver, 10)
search_input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchInput")))

search_input_element.send_keys(ip_address)
driver.find_element(By.CSS_SELECTOR, ".search-button").click()

wait = WebDriverWait(driver, 10)
search_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "(//ul[@class='showripemanaged'])[2]//li")))

result = []
result_el = driver.find_elements(By.XPATH, "(//ul[@class='showripemanaged'])[2]//li")
for item in result_el:
    item_name = item.text
    if item_name:
        result.append(item_name)

for item_name in result:
    print(item_name)

input("j")