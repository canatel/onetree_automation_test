from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from features.pages.common import Locator


class HomePage(BasePage):

    HOME_TITLE = Locator(By.XPATH, "//h1[text() = 'Home']")
    HOME_WELCOME_MESSAGE = Locator(
        By.XPATH, "//p[contains(text(),'logged in!!')]")
    LOGOUT_BUTTON = Locator(By.XPATH, "//a[text() = 'Logout']")

    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def is_home_title_displayed(self):
        return self.is_element_displayed(self.HOME_TITLE)

    def is_welcome_message_displayed(self):
        return self.is_element_displayed(self.HOME_WELCOME_MESSAGE)

    def is_logout_button_displayed(self):
        return self.is_element_displayed(self.LOGOUT_BUTTON)

    def logout(self):
        logout_button = self.find_element(*self.LOGOUT_BUTTON)
        self.click_on_element(logout_button)

    def elements_displayed(self):
        return self.is_home_title_displayed() \
            and self.is_welcome_message_displayed() \
            and self.is_logout_button_displayed()
