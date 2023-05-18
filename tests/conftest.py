import sqlite3

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    yield _driver
    _driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute test (chrome or firefox)"
    )


@pytest.fixture
def database_conn():
    """ Fixture to set up the temporary database"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE poems
        (author, poem)''')
    yield conn


@pytest.fixture
def test_data_conn(database_conn):
    cursor = database_conn.cursor()
    sample_data = [
        ('John Milton', 'Comus'),
        ('John Dryden', 'Song To A Fair Young Lady Going Out Of Town In The Spring'),
        ('John Dryden', 'Mac Flecknoe'),
        ('John Dryden', 'Happy The Man'),
        ('John Dryden', 'The Medal'),
        ('John Dryden', 'Farewell, Ungrateful Traitor!'),
        ('John Dryden', 'Heroic Stanzas'),
        ('John Dryden', 'Absalom And Achitophel'),
        ('John Dryden', "Alexander's Feast; Or, The Power Of Music"),
        ('John Dryden', 'Song From Marriage-A-La-Mode'),
        ('John Dryden', 'To The Pious Memory Of The Accomplished Young Lady Mrs. Anne Killigrew'),
        ('John Clare', 'Summer Winds'),
        ('William Morris', 'The Story of Sigurd the Volsung (excerpt)'),
        ('William Morris', "Atalanta's Race"),
        ('William Morris', 'Sir Galahad, a Christmas Mystery'),
        ('William Morris', 'Spring'),
        ('William Morris', 'The Defence of Guenevere'),
        ('William Morris', "King Arthur's Tomb"),
        ('William Morris', "Song VI: Cherish Life that Abideth"),
        ('William Morris', "Summer Dawn")
    ]
    cursor.executemany('INSERT INTO poems VALUES(?, ?)', sample_data)
    yield database_conn
