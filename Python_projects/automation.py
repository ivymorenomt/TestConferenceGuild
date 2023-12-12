# Automated testing script using Selenium (a popular testing framework)
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google.com
driver.get("https://www.google.com")

# Find the search input element by name attribute
search_box = driver.find_element("name", "q")

# Type the search query
search_box.send_keys("QA Testing Google")

# Find and click the 'Google Search' button
search_button = driver.find_element("name", "btnK")
search_button.click()

# Close the browser
driver.quit()

# Define an instance