from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.asos.com/")

driver.find_element(By.CSS_SELECTOR, "#chrome-search").send_keys("adidas")

wait = WebDriverWait(driver, 10) 
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-results #search-result-1>span")))
adidas_samba_el = driver.find_element(By.CSS_SELECTOR, "#search-results #search-result-1>span")
el = adidas_samba_el.get_attribute("aria-label")

if el == "Adidas Samba":
    adidas_samba_el.click()
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".productMediaContainer_kmkXR.mediaContainer_rdzv9 .productHeroContainer_dVvdX:nth-child(1)")))
    driver.find_element(By.CSS_SELECTOR, ".productMediaContainer_kmkXR.mediaContainer_rdzv9 .productHeroContainer_dVvdX:nth-child(1)").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MRMAA")))
    driver.find_element(By.CSS_SELECTOR, ".MRMAA").click()
input("d")
