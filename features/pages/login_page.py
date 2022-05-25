from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from features.pages.common import Locator


class LoginPage(BasePage):

    USERNAME_LABEL = Locator(By.XPATH, "//label[@for='username']")
    USERNAME_INPUT = Locator(By.ID, "username")
    PASSWORD_LABEL = Locator(By.XPATH, "//label[@for='password']")
    PASSWORD_INPUT = Locator(By.ID, "password")
    USERNAME_LABEL_0 = Locator(
        By.XPATH, "//label[@for='formly_1_input_username_0']")
    USERNAME_INPUT_0 = Locator(By.ID, "formly_1_input_username_0")
    USERNAME_LABEL_MESSAGE_0 = Locator(
        By.XPATH, "(//div[contains(text(), 'You did not enter a username')])[1]")
    USERNAME_LABEL_MESSAGE_1 = Locator(
        By.XPATH, "(//div[contains(text(), 'You did not enter a username')])[2]")
    USERNAME_ERROR_MESSAGE_LABEL = Locator(
        By.XPATH, "//div[contains(text(), 'Your username must be between 3 and 50 characters long')]")
    PASSWORD_ERROR_MESSAGE_LABEL = Locator(
        By.XPATH, "//div[contains(text(), 'Your username must be between 3 and 100 characters long')]")
    LOGIN_ERROR_MESSAGE = Locator(
        By.XPATH, "//div[contains(text(), 'Username or password is incorrect')]")
    USERNAME_DESCRIPTION_LABEL = Locator(
        By.ID, "formly_1_input_username_0_description")

    LOGIN_BUTTON = Locator(By.XPATH, "//div[@class='form-actions']/button")

    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def is_username_label_and_input_displayed(self):
        return self.is_element_displayed(self.USERNAME_LABEL) and self.is_element_displayed(self.USERNAME_INPUT)

    def is_password_label_and_input_displayed(self):
        return self.is_element_displayed(self.PASSWORD_LABEL) and self.is_element_displayed(self.PASSWORD_INPUT)

    def is_username_0_label_and_input_displayed(self):
        return self.is_element_displayed(self.USERNAME_LABEL_0) and self.is_element_displayed(self.USERNAME_INPUT_0)

    def is_username_label_message_0_displayed(self):
        return self.is_element_displayed(self.USERNAME_LABEL_MESSAGE_0)

    def is_username_label_message_1_displayed(self):
        return self.is_element_displayed(self.USERNAME_LABEL_MESSAGE_1)

    def is_username_description_label_displayed(self):
        return self.is_element_displayed(self.USERNAME_DESCRIPTION_LABEL)

    def is_username_error_message_label_displayed(self):
        return self.is_element_displayed(self.USERNAME_ERROR_MESSAGE_LABEL)

    def is_password_error_message_label_displayed(self):
        return self.is_element_displayed(self.PASSWORD_ERROR_MESSAGE_LABEL)

    def is_login_error_message_displayed(self):
        return self.is_element_displayed(self.LOGIN_ERROR_MESSAGE)

    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def is_login_button_disabled(self):
        return self.is_element_disabled(*self.LOGIN_BUTTON)

    def get_username_text(self):
        return self.get_element_text(*self.USERNAME_INPUT)

    def get_password_text(self):
        return self.get_element_text(*self.PASSWORD_INPUT)

    def get_username_0_text(self):
        return self.get_element_text(*self.USERNAME_INPUT_0)

    def login(self, username, password):
        username_input = self.find_element(*self.USERNAME_INPUT)
        username_0_input = self.find_element(*self.USERNAME_INPUT_0)
        password_input = self.find_element(*self.PASSWORD_INPUT)
        login_button = self.find_element(*self.LOGIN_BUTTON)

        username_input.send_keys(username)
        password_input.send_keys(password)
        username_0_input.send_keys(username)

        self.click_on_element(login_button)

    def elements_displayed(self):
        return self.is_username_label_and_input_displayed() \
            and self.is_password_label_and_input_displayed() \
            and self.is_username_0_label_and_input_displayed() \
            and self.is_username_label_message_0_displayed() \
            and self.is_username_label_message_1_displayed() \
            and self.is_username_description_label_displayed() \
            and self.is_login_button_displayed()

    def validate_error_message_displayed(self, message):
        if message == 'Username or password is incorrect':
            return self.is_login_error_message_displayed()
        elif message == 'Your username must be between 3 and 50 characters long':
            return self.is_username_error_message_label_displayed()
        else:
            return self.is_password_error_message_label_displayed()
