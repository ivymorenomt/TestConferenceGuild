from selenium import webdriver

class GoogleSearchTest:
    def __init__(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()

    def navigate_to_google(self):
        # Navigate to Google.com
        self.driver.get("https://www.google.com")

    def perform_search(self, search_query):
        # Find the search input element by name attribute
        search_box = self.driver.find_element("name", "q")

        # Type the search query
        search_box.send_keys(search_query)

        # Find and click the 'Google Search' button
        search_button = self.driver.find_element("name", "btnK")
        search_button.click()

    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Instantiate the class
google_test = GoogleSearchTest()

# Execute the test steps
google_test.navigate_to_google()
google_test.perform_search("QA Testing Google")

# Close the browser after the test
google_test.close_browser()

'''
Class (GoogleSearchTest):

The class GoogleSearchTest is a blueprint that defines a set of instructions for testing Google search functionality.
Attributes (self.driver):

self.driver is an attribute of the class. It represents an instance of the Selenium WebDriver (webdriver.Chrome()), allowing interaction with the web browser.
Methods (__init__, navigate_to_google, perform_search, close_browser):

__init__: This method is a constructor that initializes the class. It creates an instance of the Chrome driver (self.driver) when an object of the class is created.
navigate_to_google: This method navigates the browser to Google.com.
perform_search: This method performs a search on Google by locating the search input element, entering a search query, and clicking the 'Google Search' button.
close_browser: This method closes the browser, releasing resources.
Object (google_test):

google_test is an object instantiated from the GoogleSearchTest class. It represents a specific test scenario where a user navigates to Google, 
performs a search, and closes the browser.

Putting It Together:

The class (GoogleSearchTest) provides a structure with methods and attributes for testing Google search functionality.
The object (google_test) is an instance of the class, representing a specific test case or scenario.
Methods of the class are applied to the object (google_test) to execute the steps of the test scenario.
In summary, this code demonstrates the concepts of class, attributes, methods, and objects in the context of testing Google search using Selenium. 
The class defines the testing instructions, attributes represent elements to interact with, methods perform actions, and the object is an instance of a specific test scenario.
'''