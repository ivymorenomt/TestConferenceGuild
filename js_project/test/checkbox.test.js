const { assert } = require('chai');
const { Builder, By, until } = require('selenium-webdriver');

describe('Checkboxes Page Test', () => {
  let driver;

  before(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });

  it('should toggle checkboxes on the Checkboxes page', async function () {
    // Navigate to the Checkboxes page
    await driver.get('https://the-internet.herokuapp.com/checkboxes');

    // Find checkboxes
    const checkboxes = await driver.findElements(By.css('input[type="checkbox"]'));

    // Assert there are two checkboxes on the page
    assert.equal(checkboxes.length, 2, 'Expected two checkboxes on the page');

    // Check the first checkbox if it is unchecked
    if (!(await checkboxes[0].isSelected())) {
      await checkboxes[0].click();
    }

    // Uncheck the second checkbox if it is checked
    if (await checkboxes[1].isSelected()) {
      await checkboxes[1].click();
    }

    // Assert that the first checkbox is checked and the second checkbox is unchecked
    assert.isTrue(await checkboxes[0].isSelected(), 'First checkbox should be checked');
    assert.isFalse(await checkboxes[1].isSelected(), 'Second checkbox should be unchecked');
  });

  

  after(async function () {
    // Close the browser window
    await driver.quit();
  });
});
