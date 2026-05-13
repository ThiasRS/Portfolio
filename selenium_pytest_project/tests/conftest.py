import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # WebDriver starten
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver  # Hier wird der WebDriver an den Test "übergeben"

    driver.quit()