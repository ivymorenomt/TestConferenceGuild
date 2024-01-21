from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestCheckbox: # explain what is the intention of this class
    def setup_method(self, method):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def teardown_method(self, method):
        self.driver.quit()

    
    def test_toggle_checkboxes(self):
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']") # multiple ways to find it.
        assert len(checkboxes) == 2

        checkbox1, checkbox2 = checkboxes[0], checkboxes[1]

        if not checkbox1.is_selected():
            checkbox1.click()

        if checkbox2.is_selected():
            checkbox2.click()

        assert checkbox1.is_selected(), "CB1 should be checked"
        assert not checkbox2.is_selected(), "CB2 should be unchecked"

