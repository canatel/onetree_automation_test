from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage

__all__ = [cls for cls in dir() if cls.endswith("Page")]
