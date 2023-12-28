from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestCheckbox:
    def setup_method(self, method):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def teardown_method(self, method):
        self.driver.quit()

    
    def test_toggle_checkboxes(self):
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        assert len(checkboxes) == 2

        checkbox1, checkbox2 = checkboxes[0], checkboxes[1]

        if not checkbox1.is_selected():
            checkbox1.click()

        if checkbox2.is_selected():
            checkbox2.click()

        assert checkbox1.is_selected(), "CB1 should be checked"
        assert not checkbox2.is_selected(), "CB2 should be unchecked"

# '''
# Class (TestCheckbox):

# - TestCheckbox is a class that represents a set of tests related to checkbox functionality.

# Attributes (self.driver):
# - self.driver is an attribute of the class, representing the Selenium WebDriver (webdriver.Chrome()). It is used to interact with the web browser.

# Methods (setup_method, teardown_method, test_toggle_checkboxes):
# - setup_method: This method sets up the test environment by creating a new instance of the Chrome driver and navigating to 
# the specified URL (https://the-internet.herokuapp.com/checkboxes).
# - teardown_method: This method is called after the test execution and closes the browser (self.driver.quit()), releasing resources.
# - test_toggle_checkboxes: This method contains the actual test scenario. It finds the checkboxes on the page, interacts with them, and asserts the expected conditions.

# Test Execution:
# The test is executed by creating an object of the TestCheckbox class and invoking its methods.
# The setup_method method is called to set up the test environment.
# The test_toggle_checkboxes method is executed, performing the checkbox toggling test.
# The teardown_method method is called to clean up after the test.

# Putting It Together:

# The class provides a structure for testing checkbox functionality.
# Attributes (self.driver) represent the WebDriver instance.
# Methods (setup_method, teardown_method, test_toggle_checkboxes) define the testing process.
# Test execution involves creating an object of the class and invoking its methods.
# In summary, this code demonstrates the structure of a test class for checkbox functionality using Selenium. 
# It includes setup, teardown, and an actual test method to interact with checkboxes on a web page.
# '''