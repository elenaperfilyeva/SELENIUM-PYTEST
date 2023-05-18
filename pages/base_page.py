from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> WebElement:
        return self.driver.find_elements(*locator)

    def _when_visible(self, locator: tuple, time: int = 3):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _when_not_visible(self, locator: tuple, time: int = 3):
        wait = WebDriverWait(self.driver, time)
        not wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 3):
        self._when_visible(locator, time)
        self._find_element(locator).send_keys(text)

    def _press_enter(self, locator: tuple, time: int = 3):
        self._when_visible(locator, time)
        self._find_element(locator).send_keys(Keys.ENTER)

    def _click(self, locator: tuple, time: int = 10):
        self._when_visible(locator, time)
        self._find_element(locator).click()

    def _get_text(self, locator: tuple, time: int = 3) -> str:
        self._when_visible(locator, time)
        return self._find_element(locator).text

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find_element(locator)._is_displayed()
        except NoSuchElementException:
            return False

    def _open(self, url: str):
        self.driver.get(url)
