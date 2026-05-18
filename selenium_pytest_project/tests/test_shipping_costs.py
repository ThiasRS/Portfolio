from utils.helpers import register_and_login_new_user
from pages.home_page import HomePage
from pages.shop_page import ShopPage
from pages.checkout_page import CheckoutPage


def test_difference_amount_shipping_cost(driver):
    # Zufälligen Nutzer registrieren und einloggen
    register_and_login_new_user(driver)

    # Navigieren zum Shop
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Altersverifizierung überspringen
    shop_page = ShopPage(driver)
    shop_page.skip_age_verification()

    # Produkt in Warenkorb reinlegen
    shop_page.add_first_product_to_cart()

    # Zum Warenkorb navigieren
    shop_page.click_cart_button()

    # Prüfen ob Differenzbetrag auf der Seite sichtbar ist
    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_difference_amount_displayed()