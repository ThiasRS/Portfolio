from utils.helpers import register_and_login_new_user
from pages.shop_page import ShopPage
from pages.home_page import HomePage


def test_verification_age_visibility(driver):
    # Zufälligen Nutzer registrieren und einloggen
    register_and_login_new_user(driver)

    # Navigieren zum Shop
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Prüfen ob die Altersverifikation erscheint
    shop_page = ShopPage(driver)
    confirm_age_button = shop_page.find(shop_page.CONFIRM_AGE_BUTTON)
    assert confirm_age_button.is_displayed()