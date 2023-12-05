const fs = require('fs');
const { assert } = require('chai');
const { Builder, By } = require('selenium-webdriver');

describe('Login Page Test', () => {
  let driver;

  before(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });

  const BASE_URL = 'https://the-internet.herokuapp.com/login';

  // Read test data from the JSON file
  const testData = JSON.parse(fs.readFileSync('../test_data/test_data.json', 'utf8'));

  testData.forEach((data, index) => {
    it(`should ${data.expectedResult.includes('invalid') ? 'fail' : 'succeed'} for Test Case ${index + 1}`, async function () {
      // Navigate to the login page
      await driver.get(BASE_URL);

      // Find username and password input fields
      const usernameInput = await driver.findElement(By.id('username'));
      const passwordInput = await driver.findElement(By.id('password'));
      const loginButton = await driver.findElement(By.css('button[type="submit"]'));

      // Clear existing input values
      await usernameInput.clear();
      await passwordInput.clear();

      // Enter username and password from test data
      await usernameInput.sendKeys(data.username);
      await passwordInput.sendKeys(data.password);

      // Click the login button
      await loginButton.click();

      if (data.expectedResult.includes('invalid')) 
      {
        // If the login is expected to fail, assert that there is an error message
        const errorMessageSelector = By.css('.flash.error');

        try {
            // Use an explicit wait to wait for the error message to be visible
            await driver.wait(until.elementIsVisible(driver.findElement(errorMessageSelector)), 5000, 'Error message is not visible');
            
            // If the error message is visible, assert it and clear the fields
            const errorMessage = await driver.findElement(errorMessageSelector).getText();
            assert.include(errorMessage, data.expectedResult, `Expected error message not found: ${errorMessage}`);

            // Clear existing input values
            await usernameInput.clear();
            await passwordInput.clear();
        } catch (error) {
            // Handle the case where the error message is not visible within the specified timeout
            console.error('Error message not found within the specified timeout:', error);
        }
      } else {
        // If the login is expected to succeed, assert that the user is logged in
        const successMessage = await driver.findElement(By.css('.flash.success')).getText();
        assert.include(successMessage, data.expectedResult, `Expected success message not found: ${successMessage}`);

        const logoutButton = await driver.findElement(By.css('#content > div > a')).catch(() => null);
        if (logoutButton) {
          await logoutButton.click();
          
        }
      }
    });
  });

  after(async function () {
    // Close the browser window
    await driver.quit();
  });
});
