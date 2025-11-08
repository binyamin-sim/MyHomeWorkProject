from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.mytinytodo.net/demo/#list/1")

driver.find_element(By.CSS_SELECTOR, "#task").send_keys("test1")
driver.find_element(By.CSS_SELECTOR, "#newtask_submit").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#task").send_keys("test2")
driver.find_element(By.CSS_SELECTOR, "#newtask_submit").click()

wait = WebDriverWait(driver, 10) 
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tasklist > li:nth-child(1) .task-title")))
tasks_text1 = driver.find_element(By.CSS_SELECTOR, "#tasklist > li:nth-child(1) .task-title").text
if tasks_text1 == "test1":
    print("your mission are seccessfully task 1 is added")
else:
    print("something wrong")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tasklist > li:nth-child(2) .task-title")))
tasks_text2= driver.find_element(By.CSS_SELECTOR, "#tasklist > li:nth-child(2) .task-title").text
if tasks_text2 == "test2":
    print("your mission are seccessfully task 2 is added")
else:
    print("something wrong")


print(tasks_text1)
print(tasks_text2)