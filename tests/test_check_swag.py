from pages.swag_labs import SwagLabsPage

def test_check_icon(browser):
    swag_lab_page = SwagLabsPage(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_icon()

def test_check_name_field(browser):
    swag_lab_page = SwagLabsPage(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_name_field()

def test_check_password_field(browser):
    swag_lab_page = SwagLabsPage(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_password_field()