from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

links_el = driver.find_elements(By.TAG_NAME, 'a')

for link in links_el:              
    href = link.get_attribute("href")      
    print(f"Href: {href}")


print("\n *** all selenium links *** ")
for link in links_el:
    href = link.get_attribute("href")
    if href and "selenium" in href.lower():
        print(href)
        
        

input('a')
