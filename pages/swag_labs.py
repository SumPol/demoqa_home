from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabsPage(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True


    def exist_name_field(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True


    def exist_password_field(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True