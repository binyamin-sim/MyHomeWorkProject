

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.ebay.com/sch/ebayadvsearch")


driver.find_element(By.CSS_SELECTOR, "#_nkw").send_keys("tent")
driver.find_element(By.CSS_SELECTOR, "#_ex_kw").send_keys("test ", "automation ", "gal")
driver.find_element(By.CSS_SELECTOR, "[value='LH_BIN']").click()

search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
search_button.click()
driver.back()


input("sd")