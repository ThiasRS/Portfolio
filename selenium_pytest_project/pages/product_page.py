from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    TEXT_AREA = (By.XPATH, "//textarea")