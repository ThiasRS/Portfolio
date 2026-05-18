from utils.helpers import register_and_login_new_user, generate_underage_birthday, generate_wrong_format_birthday
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


def test_alcohol_visibility_when_underage(driver):
    # Zufälligen Nutzer registrieren und einloggen
    register_and_login_new_user(driver)

    # Navigieren zum Shop
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Altersverifikation als Minderjähriger
    underage_birthday = generate_underage_birthday()
    shop_page = ShopPage(driver)
    shop_page.age_verification(underage_birthday)

    # Navigieren zur Alkohol Kategorie
    shop_page.navigate_to_alcohol_category()

    # Prüfen ob Shop leer ist und Notiz für Minderjährige erscheint
    try:
        shop_page.find(shop_page.FIRST_PRODUCT, timeout=1)
        product_exists = True
    except:
        product_exists = False
    underage_notice = shop_page.find(shop_page.UNDERAGE_NOTICE)
    assert product_exists == False
    assert underage_notice.is_displayed()


def test_wrong_birthday_format(driver):
    # Zufälligen Nutzer registrieren und einloggen
    register_and_login_new_user(driver)

    # Navigieren zum Shop
    home_page = HomePage(driver)
    home_page.go_to_shop()

    # Alterverifikation im falschen Format
    wrong_format_birthday = generate_wrong_format_birthday()
    shop_page = ShopPage(driver)
    shop_page.age_verification(wrong_format_birthday)

    # Prüfen ob eine Meldung erscheint für die ungültige Eingabe
    error_message = shop_page.find(shop_page.BIRTHDAY_FORMAT_INVALID)
    assert error_message.is_displayed()
