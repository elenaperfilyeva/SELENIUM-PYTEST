from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    __url = "http://127.0.0.1:8000/"

    __poems_list_header = (By.CSS_SELECTOR, "div.poem-row.first-row.last-row")
    __poems_list_item = (By.XPATH, "//div[contains(@class, 'poem-row') and not(contains(@style, 'background'))]")
    __new_poems_btn = (By.XPATH, "//button[text()='New Poems']")
    __loader = (By.CSS_SELECTOR, ".loader")
    __search_field = (By.XPATH, "//input[@name='poemSearch']")
    __results_header = (By.XPATH, "//div[text()='Results']")
    __search_result_row = (By.XPATH,
        "//div[contains(@style,'width')][2]//div[contains(@class, 'poem-row') and not(contains(@style, 'background'))]")
    __empty_search_result_message = (By.XPATH, "//span[text()='Try Another Search']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open(self.__url)

    def count_displayed_poems(self):
        super()._when_visible(self.__poems_list_header)
        return len(super()._find_elements(self.__poems_list_item))

    def get_displayed_poems(self) -> list:
        super()._when_visible(self.__poems_list_header)
        poems = []
        rows = self.driver.find_elements(*self.__poems_list_item)
        for row in rows:
            author = row.find_elements(By.XPATH, './div')[0].text
            poem = row.find_elements(By.XPATH, './div')[1].text
            poems.append((author, poem))
        return poems

    def get_new_poems(self):
        super()._click(self.__new_poems_btn)
        super()._when_visible(self.__loader, 5)
        super()._when_not_visible(self.__loader, 5)

    def search(self, search_request):
        super()._when_visible(self.__search_field)
        super()._type(self.__search_field, search_request)
        super()._press_enter(self.__search_field)

    def get_search_results(self, search_request) -> list:
        super()._when_visible(self.__search_field)
        super()._type(self.__search_field, search_request)
        super()._press_enter(self.__search_field)
        super()._when_visible(self.__results_header, 5)

        # for each row in search results
        # add tuple (author, poem) to search_results list
        search_results = []
        rows = self.driver.find_elements(*self.__search_result_row)
        for row in rows:
            author = row.find_elements(By.XPATH, './div')[0].text
            poem = row.find_elements(By.XPATH, './div')[1].text
            search_results.append((author, poem))
        return search_results

    @property
    def empty_search_results_message(self):
        super()._when_visible(self.__empty_search_result_message)
        return super()._get_text(self.__empty_search_result_message)
