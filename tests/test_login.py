

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Define the URL, username, and password
URL = "http://13.53.206.233:8000/login/"  # Replace with your login URL
USERNAME = "akshay"
PASSWORD = "akTR@300"

@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_login(browser):
    browser.get(URL)
    
    # Find the username and password input fields and the login button
    username_field = browser.find_element(By.ID, "username")  # Adjust the locator as needed
    password_field = browser.find_element(By.ID, "form2Example22")  # Adjust the locator as needed
    login_button = browser.find_element(By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[3]/button")  # Adjust the locator as needed

    # Input the username and password
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    
    # Click the login button
    login_button.click()

    # Verify login success by checking for a specific element that is present only on the login success page
    try:
        success_element = browser.find_element(By.ID, "/html/body/div/header/nav/div/div/a[1]/span")  # Adjust the locator as needed
        assert success_element.is_displayed()
        print("Login successful")
        with open("report.html", "w") as report:
            report.write("<html><body><h1>Login Test Report</h1><p>Login successful</p></body></html>")
    except Exception as e:
        print(f"Login failed: {e}")
        with open("report.html", "w") as report:
            report.write(f"<html><body><h1>Login Test Report</h1><p>Login failed: {e}</p></body></html>")
        pytest.fail(f"Login failed: {e}")
