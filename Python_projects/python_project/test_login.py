import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage:
    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # This line enables headless mode
        cls.driver = webdriver.Chrome(options=chrome_options)



    def setup_method(self):
        self.base_url = 'https://the-internet.herokuapp.com/login'
        self.test_data = json.loads(open('./test_data/test_data.json', 'r').read())

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("test_input", json.loads(open('./test_data/test_data.json', 'r').read()))
    def test_login_page(self, test_input):
        self.driver.get(self.base_url)

        # Find username and password input fields
        username_input = self.driver.find_element(By.ID, 'username')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        # Clear existing input values
        username_input.clear()
        password_input.clear()

        # Enter username and password from test data
        username_input.send_keys(test_input['username'])
        password_input.send_keys(test_input['password'])

        # Click the login button
        login_button.click()

        if 'invalid' in test_input['expectedResult']:
            # If the login is expected to fail, assert that there is an error message
            error_message_selector = (By.CSS_SELECTOR, '.flash.error')

            try: # try and catch explain it how it works - divide by zero scenario
                # Use an explicit wait to wait for the error message to be visible
                WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(error_message_selector))

                # If the error message is visible, assert it and clear the fields
                error_message = self.driver.find_element(*error_message_selector).text
                assert test_input['expectedResult'] in error_message, f'Expected error message not found: {error_message}'

                # Clear existing input values
                username_input.clear()
                password_input.clear()
            except Exception as e:
                # Handle the case where the error message is not visible within the specified timeout
                print(f'Error message not found within the specified timeout: {e}')
        else:
            # If the login is expected to succeed, assert that the user is logged in
            success_message = self.driver.find_element(By.CSS_SELECTOR, '.flash.success').text
            assert test_input['expectedResult'] in success_message, f'Expected success message not found: {success_message}'

            # Perform logout if the logout button is present
            logout_button = self.driver.find_element(By.CSS_SELECTOR, '#content > div > a')
            if logout_button:
                logout_button.click()
