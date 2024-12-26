import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

# Constants
URL = "https://www.seleniumeasy.com/test/table-search-filter-demo.html"
SEARCH_TERM = "New York"
EXPECTED_ENTRIES = 5

# Setup function for WebDriver
def setup_driver(browser="chrome"):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode for testing
        service = Service()  # Path to ChromeDriver if required
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService()  # Path to GeckoDriver if required
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser: Choose 'chrome' or 'firefox'")
    return driver

@pytest.fixture(scope="function")
def driver():
    driver_instance = setup_driver(browser="chrome")
    yield driver_instance
    driver_instance.quit()

def test_search_functionality(driver):
    # Navigate to the website
    driver.get(URL)

    # Locate the search box and input the search term
    search_box = driver.find_element(By.ID, "task-table-filter")
    search_box.send_keys(SEARCH_TERM)
    time.sleep(2)  # Allow time for filtering

    # Validate the search results
    table_rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
    visible_rows = [row for row in table_rows if row.is_displayed()]

    assert len(visible_rows) == EXPECTED_ENTRIES, (
        f"Expected {EXPECTED_ENTRIES} visible rows but found {len(visible_rows)}"
    )

if __name__ == "__main__":
    pytest.main(["-v", "--disable-warnings", __file__])
