import pytest

from pages.home_page import HomePage


@pytest.mark.display
class TestDisplayPoems:
    def test_amount_of_poems_on_page_load(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        expected_amount_of_poems = 5
        actual_amount_of_poems = home_page.count_displayed_poems()

        assert actual_amount_of_poems == expected_amount_of_poems, \
            f"Wrong amount of poems on load page: " \
            f"expected amount of poems '{expected_amount_of_poems}', " \
            f"displayed '{actual_amount_of_poems}'"

    def test_new_poems(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        current_poems = home_page.get_displayed_poems()
        home_page.get_new_poems()
        new_poems = home_page.get_displayed_poems()

        assert current_poems != new_poems, \
            "List of poems is not updated after clicking 'New Poems' button"
