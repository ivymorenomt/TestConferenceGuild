import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestCheckbox:
    @pytest.fixture
    def driver(self):
        # driver = webdriver.Chrome()
        # yield driver
        # driver.quit()

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # This line enables headless mode
        driver = webdriver.Chrome(options=chrome_options)

        yield driver
        driver.quit()

    def test_toggle_checkboxes(self, driver):
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        assert len(checkboxes) == 2

        checkbox1, checkbox2 = checkboxes[0], checkboxes[1]

        if not checkbox1.is_selected():
            checkbox1.click()

        if checkbox2.is_selected():
            checkbox2.click()

        assert checkbox1.is_selected(), "CB1 should be checked"
        assert not checkbox2.is_selected(), "CB2 should be unchecked"
