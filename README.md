# End-to-End Web Application Testing for E-Commerce

## Overview

This project provides an automated end-to-end testing framework for e-commerce websites. It uses Selenium WebDriver with pytest to perform cross-browser testing and generate detailed test reports. The framework is designed to be easily integrated into a CI/CD pipeline for continuous testing.

## Tech Stack

- **Language:** Python
- **Testing Framework:** pytest, Selenium WebDriver
- **Reporting:** pytest-html
- **Configuration:** YAML

## Project Structure

```
End-to-End-WebApp-Testing/
├── config/
│   └── config.yaml           # Configuration file (browser, base URL)
├── pages/
│   ├── base_page.py          # Base page class with common methods
│   ├── home_page.py          # Page object for the home page
│   ├── product_page.py       # Page object for the product page
│   ├── cart_page.py          # Page object for the cart page
│   └── checkout_page.py      # Page object for the checkout page
├── tests/
│   ├── conftest.py           # pytest configuration and hooks
│   └── test_guest_checkout.py # Example test case for guest checkout
├── requirements.txt          # Project dependencies
├── pytest.ini                # pytest configuration file
└── README.md                 # Project README file
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd End-to-End-WebApp-Testing
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure browser and base URL:**
   - Modify the `config/config.yaml` file to set your desired browser and the base URL of the e-commerce website you want to test.

   ```yaml
   browser: chrome  # or firefox, safari, edge
   base_url: https://www.wrenclothing.in # Target website URL
   implicit_wait: 10 # Implicit wait time in seconds
   ```

## Running Tests

To execute the tests, use the following command in the project root directory:

```bash
PYTHONPATH=. pytest tests/test_guest_checkout.py --html=report.html
```

- **`PYTHONPATH=.`**:  Ensures that the `pages` directory is in the Python path, allowing pytest to find the page object files.
- **`pytest tests/test_guest_checkout.py`**: Runs the specified test file. You can run all tests in the `tests` directory by simply using `pytest tests/`.
- **`--html=report.html`**: Generates an HTML report named `report.html` in the project root directory.

## Viewing Reports

After running the tests, open the `report.html` file in your web browser to view the detailed test execution report. This report provides a summary of test results, execution time, and any failures.

## Page Object Model (POM)

This framework utilizes the Page Object Model design pattern. Each page of the e-commerce website is represented by a separate Python class in the `pages` directory.

- **Locators:** Page locators (e.g., CSS selectors, XPaths) are defined within the page class.
- **Actions:** Methods within the page class represent actions that can be performed on the page (e.g., `search_product`, `add_to_cart`).
- **Tests:** Test cases in the `tests` directory interact with page objects to execute test scenarios.

This approach promotes code reusability, maintainability, and a cleaner separation between test logic and page implementation.

## Example Test Case (`tests/test_guest_checkout.py`)

The `tests/test_guest_checkout.py` file demonstrates a basic test case for a guest checkout workflow. It includes steps to:

1. Open the home page.
2. Search for a product.
3. Add the product to the cart.
4. Proceed to checkout as a guest.
5. Fill in checkout details (implementation incomplete).
6. Validate order confirmation (not yet implemented).

This is just a starting point, and more test scenarios should be added to cover critical user workflows as defined in the project scope.

## Further Development

- **Implement remaining checkout steps:** Complete the checkout process in the test case, including filling in shipping and payment details.
- **Add more test scenarios:** Create tests for user account management, product interaction, order management, coupon validation, and error handling.
- **Cross-browser testing:** Configure pytest to run tests across different browsers (Chrome, Firefox, Safari, Edge) as specified in `config/config.yaml`.
- **CI/CD integration:** Integrate this framework into a GitLab CI/CD pipeline for automated test execution on code changes.
- **Improve reporting:** Explore and integrate Allure Report for more advanced and visually appealing test reports.
- **Flake mitigation:** Implement retry mechanisms and explicit waits to make tests more flake-resistant.
- **Test coverage:** Use `pytest-cov` to measure test coverage and ensure 95% coverage for critical user workflows.
