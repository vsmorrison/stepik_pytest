import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_button(browser):
    browser.get(LINK)
    add_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_button.is_displayed(), "Button is unavailable"
    time.sleep(5)
