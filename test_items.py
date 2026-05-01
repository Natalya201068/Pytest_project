from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_cart_in_page(browser):
    browser.get(link)
    button = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    # text_btn = button.text
    # assert text_btn == "Add cart to basket"
    assert button.is_displayed()
