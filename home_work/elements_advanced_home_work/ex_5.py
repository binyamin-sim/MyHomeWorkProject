from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ebay.com/sch/ebayadvsearch")
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".floating-label #_nkw")))
driver.find_element(By.CSS_SELECTOR, ".floating-label #_nkw").send_keys("guitar")

el = driver.find_element(By.CSS_SELECTOR, "[id$='_sacat']")
dd = Select(el)
dd.select_by_visible_text("Musical Instruments & Gear")

driver.find_element(By.CSS_SELECTOR, "[aria-label^='Enter minimum price range value']").send_keys("50")
driver.find_element(By.CSS_SELECTOR, "[aria-label^='Enter maximum price range value']").send_keys("60")
driver.find_element(By.CSS_SELECTOR, "[id$=LH_Auction]").click()
driver.find_element(By.CSS_SELECTOR, ".field.adv-keywords__btn-help>.btn.btn--primary").click()


wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class$='s-card__price']")))
guiter_list_price_el = driver.find_elements(By.CSS_SELECTOR, "[class$='s-card__price']")

guiter_list_price = []
for guiter in guiter_list_price_el:
    text = guiter.text.strip()  
    text = text.replace(",", "")  
    text = re.sub(r"[^\d\.]", "", text) 
    if text:
        price = int(float(text))  
        guiter_list_price.append(price)


for item in guiter_list_price:
        if item < 50 or item > 60:
            print(f"You received an incorrect price result {item}")
            break
else:
    print("the prices are correct")

