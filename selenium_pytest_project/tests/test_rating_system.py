from utils.helpers import register_and_login_new_user, generate_payment_and_address_data, generate_random_string
from pages.home_page import HomePage
from pages.shop_page import ShopPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage


def test_rating_system_visibility(driver):
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

    # Daten im Checkout Prozess ausfüllen und Produkt kaufen
    payment_info = generate_payment_and_address_data()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_shipment_payment_information(payment_info)
    checkout_page.click_buy_now_button()

    # Wieder zum shop navigieren
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Zur Produktpage navigieren
    shop_page = ShopPage(driver)
    shop_page.click_first_product()

    # Prüfen ob Bewertungstextfeld verfügbar ist
    product_page = ProductPage(driver)
    text_area = product_page.find(product_page.TEXT_AREA)
    assert text_area.is_displayed(), "Kein Textfeld sichtbar!"


def test_review_text_characters(driver):
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

    # Daten im Checkout Prozess ausfüllen und Produkt kaufen
    payment_info = generate_payment_and_address_data()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_shipment_payment_information(payment_info)
    checkout_page.click_buy_now_button()

    # Wieder zum shop navigieren
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Zur Produktpage navigieren
    shop_page = ShopPage(driver)
    shop_page.click_first_product()

    # Bewertung mit 501 Zeichen schreiben. Maximalzeichen 500.
    too_long_text = generate_random_string(501)
    product_page = ProductPage(driver)
    product_page.write_product_review(too_long_text)

    # Prüfen ob error message erscheint
    error_message = product_page.find(product_page.ERROR_MSG)
    assert error_message.is_displayed(), "Keine Error Message erschienen."


def test_review_text_code(driver):
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

    # Daten im Checkout Prozess ausfüllen und Produkt kaufen
    payment_info = generate_payment_and_address_data()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_shipment_payment_information(payment_info)
    checkout_page.click_buy_now_button()

    # Wieder zum shop navigieren
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Zur Produktpage navigieren
    shop_page = ShopPage(driver)
    shop_page.click_first_product()

    # Bewertung mit code schreiben
    code_text = """<span style="font-family: 'Courier New', Courier, monospace; color: red; font-size: 24px;">Hacked Font</span>"""
    product_page = ProductPage(driver)
    product_page.write_product_review(code_text)

    # Bewertung abschicken
    product_page.click_review_send_button()

    # Prüfen ob Fehlermeldung erscheint
    invalid_input_message = product_page.find(product_page.INVALID_INPUT_MSG)
    assert invalid_input_message.is_displayed(), "Keine Fehlermeldung erschienen"