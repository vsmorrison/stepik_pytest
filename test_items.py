import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_item_to_cart_button(browser):
    browser.get(link)
    add_to_cart_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_cart_button.is_displayed(), "Button is unavailable"
    time.sleep(5)
