import time

# Third-party libraries
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, \
    ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# Project modules
from features.pages.common import Locator
from features.utils.typing import Any, Chrome, List, Tuple, Union, WebElement
from features.utils.settings import config, parse_config

config = parse_config()


class BasePage:

    def __init__(self, driver: Chrome):
        """Class constructor."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @staticmethod
    def wait_for(time_in_seconds: int):
        """Stop execution thread for time in seconds.

        Parameters
        ----------
        time_in_seconds: int
            Mainly fetched from feature file, string which means
            a time quantity in seconds.

        """
        time.sleep(int(time_in_seconds))

    def navigate_to(self, url: str):
        """Browse to specified URL.

        Parameters
        ----------
        url: str
            url or ip address to navigate to.

        """
        self.driver.maximize_window()
        self.driver.get(url)

    def find_element(self, *strategy: str) -> WebElement:
        """Find an element on the page DOM to interact with it.

        Parameters
        ----------
        *strategy: Tuple
            Unpacked tuple of two values (By, Value)

        Returns
        -------
        WebElement
            Python WebElement DOM representation.

        """
        return self.driver.find_element(*strategy)

    def is_element_displayed(self, locator: Locator, timeout: int = 0) -> bool:
        """
        Return True if the element is displayed, False if it isn't.

        Parameters
        ----------
        locator : Locator
            Locator tuple of two values (By, Value)

        Returns
        -------
        bool
            True if the element is displayed False otherwise.

        """

        wait = self.wait
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_to_element_by_coordinates(self, element: WebElement):
        """Scroll browser window to specified element coordinates.

        Parameters
        ----------
        element: WebElement
            Python WebElement DOM representation to scroll to.

        """
        coordinates = element.location_once_scrolled_into_view
        self.driver.execute_script(
            f"window.scrollTo({coordinates['x']}, {coordinates['y']});"
        )

    def click_on_element(self, element: Union[Locator, WebElement]):
        """Wait until an element is visible and then click it."""

        if isinstance(element, Locator):
            element = self.find_element(*element)

        self.scroll_to_element_by_coordinates(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click()", element)
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].click()", element)
