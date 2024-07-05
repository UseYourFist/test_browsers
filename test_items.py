from selenium.webdriver.common.by import By
    
def test_add_to_cart_button_shows(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket') != [], 'There is no add to cart button here'