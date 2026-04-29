from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login_automation(driver, username, password):
    # Seite aufrufen
    driver.get("https://www.saucedemo.com/")

    # Wartestrategie
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))

    # Elemente finden und Aktion ausführen
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()