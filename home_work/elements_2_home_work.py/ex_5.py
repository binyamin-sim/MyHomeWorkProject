from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ebay.com/")

driver.find_element(By.CSS_SELECTOR, "#gh-ac").send_keys("tent")
driver.find_element(By.CSS_SELECTOR, ".gh-search-button__label").click()

wait = WebDriverWait(driver, 10)

list_of_tent = []


for page_index in range(10):
    page_number = page_index + 1
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class='su-styled-text primary default']")))
    the_tent_title = driver.find_elements(By.CSS_SELECTOR, "[class='s-card s-card--horizontal s-card--dark-solt-links-blue']")

    current_page_items = []
    for tent in the_tent_title:
        tent_text = tent.text
        current_page_items.append(tent_text)

    list_of_tent.append({
        "page_number": page_number,
        "items": current_page_items
    })

    print(f"Finished scraping page {page_number}, collected {len(current_page_items)} items. Total collected: {len(list_of_tent)} pages.")
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".pagination__next.icon-link")))
    driver.find_element(By.CSS_SELECTOR, ".pagination__next.icon-link").click()


for page_data in list_of_tent:
    print(f"** page {page_data['page_number']} **")
    print("-" * 15)
    
    for item in page_data['items']:
        print(item)
        print("*" * 10)
    
    print("\n")