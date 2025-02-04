import pytest
import yaml
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests in")
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests in")

@pytest.fixture(scope="session")
def config(request):
    with open("config/config.yaml", "r") as f:
        config_yaml = yaml.safe_load(f)
    
    browser = request.config.getoption("--browser").lower()
    env = request.config.getoption("--env").lower()
    
    if browser not in ["chrome", "firefox", "safari", "edge"]:
        pytest.exit(f"Browser '{browser}' is not supported. Supported browsers are chrome, firefox, safari, edge")
    
    if env not in ["staging", "production"]:
        pytest.exit(f"Environment '{env}' is not supported. Supported environments are staging, production")

    return {
        "browser": browser,
        "env": env,
        "base_url": config_yaml["base_url"],
        "implicit_wait": config_yaml["implicit_wait"]
    }

@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config["implicit_wait"])
    driver.get(config["base_url"])
    yield driver
    driver.quit()
