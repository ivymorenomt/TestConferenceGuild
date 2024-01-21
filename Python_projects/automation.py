from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchTest:
    def __init__(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()

    def navigate_to_google(self):
        # Navigate to Google.com
        self.driver.get("https://www.google.com") 

    def perform_search(self, search_query):
        # Find the search input element by name attribute
        search_box = self.driver.find_element(By.NAME, "q")

        # Type the search query
        search_box.send_keys(search_query)

        # Use explicit wait to wait for the 'Google Search' button to be clickable
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "btnK"))
        )

        # Click the 'Google Search' button
        search_button.click()

    def validate_search_results(self, expected_text):
        # Use explicit wait to wait for the search results to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Get the search results
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")

        # Validate each search result
        for result in search_results:
            result_text = result.text
            assert expected_text.lower() in result_text.lower(), f"Expected text not found in result: {result_text}"

    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Instantiate the class
google_test = GoogleSearchTest()

# Execute the test steps
google_test.navigate_to_google()
google_test.perform_search("QA Testing Google")
google_test.validate_search_results("QA Testing")

# Close the browser after the test
google_test.close_browser()
