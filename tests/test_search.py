import pytest

from pages.home_page import HomePage


@pytest.mark.search
class TestSearchPoems:

    @pytest.mark.parametrize("search_request",
                             [("Morris"),
                              ("Comus"),
                              ("John Dryden"),
                              ("Summer Winds")])
    def test_search_positive(self, driver, test_data_conn, search_request):
        home_page = HomePage(driver)
        home_page.open()

        actual_search_results = home_page.get_search_results(search_request)

        cursor = test_data_conn.cursor()
        expected_search_results = list(cursor.execute(
            f'SELECT * '
            'FROM poems '
            f'WHERE author LIKE "%{search_request}%" OR poem LIKE "%{search_request}%"'))

        assert len(actual_search_results) == len(expected_search_results), \
            f"Length of expected and actual results are not equal: " \
            f"actual length '{len(actual_search_results)}', expected length '{len(expected_search_results)}'"

        assert actual_search_results == expected_search_results, \
            f"Irrelevant search results for request: '{search_request}'"

    @pytest.mark.parametrize("search_request",
                             ["SearchRequestForEmptyResult"])
    def test_search_negative(self, driver, search_request):
        home_page = HomePage(driver)
        home_page.open()

        home_page.search(search_request)

        assert home_page.empty_search_results_message == "Try Another Search"
