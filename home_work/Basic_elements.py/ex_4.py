from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ksp.co.il/web/")

cookies = driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedSecondary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorSecondary.MuiButton-root.MuiButton-contained.MuiButton-containedSecondary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorSecondary.muirtl-x6p6hi")
cookies.click()

searech_el = driver.find_element(By.CSS_SELECTOR, "#searchTextBox")
shopping_card_el = driver.find_element(By.CSS_SELECTOR, ".MuiBadge-invisible.MuiBadge-anchorOriginTopRight.MuiBadge-anchorOriginTopRightRectangular.MuiBadge-overlapRectangular.MuiBadge-colorSecondary.muirtl-1wdm5po")
gaming_button = driver.find_element(By.CSS_SELECTOR, "#categoryimage3")

selectores = [searech_el, shopping_card_el, gaming_button]

for elemens in selectores:
    text = elemens.text
    id_name = elemens.get_attribute("id")
    tag = elemens.tag_name
    is_disp = elemens.is_displayed()
    is_enab = elemens.is_enabled()

    print(f"1. Text (.text): {text if text else 'No text visible'}")
    print(f"2. ID (.get_attribute('id')): {id_name if id_name else 'No ID'}")
    print(f"3. Tag (.tag_name): {tag}")
    print(f"4. Displayed? (.is_displayed()): {is_disp}")
    print(f"5. Enabled? (.is_enabled()): {is_enab}")
    print("*" *20)


input("d")