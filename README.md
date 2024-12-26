# QA-Selenium-Automation-with-Python
# Selenium Automation: Search Functionality Test

## Objective
Automate the validation of the search functionality on the Selenium Playground website's Table Search Demo.

## Prerequisites
- Python 3.8 or higher.
- Google Chrome or Mozilla Firefox installed.
- WebDriver for the chosen browser:
  - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
  - [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- `pip` installed.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/selenium-automation.git
   cd selenium-automation
   ```
2. Install dependencies:
   ```bash
   pip install selenium pytest
   ```

## Running the Script
1. Execute the test script:
   ```bash
   pytest qa_selenium_test.py
   ```

2. For detailed test output:
   ```bash
   pytest qa_selenium_test.py -v
   ```

## Approach
1. **Setup WebDriver**:
   - Initializes WebDriver based on the selected browser (default: Chrome) and runs in headless mode.
2. **Navigate to URL**:
   - Directs the browser to the Selenium Playground Table Search Demo page.
3. **Search and Validate**:
   - Locates the search box and inputs the term "New York."
   - Waits for filtering and validates that exactly 5 rows are visible in the table.

## Browser Compatibility
- Google Chrome (default).
- Mozilla Firefox (adjust `setup_driver` in `qa_selenium_test.py` if needed).

## Notes
- Includes a `time.sleep` call for simplicity; replace with explicit waits for production use.
- If browser compatibility issues arise, ensure browser and driver versions are aligned.

## Contributing
Feel free to fork this repository, open issues, or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
