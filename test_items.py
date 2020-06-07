import time


def test_button_exist(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
