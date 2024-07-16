import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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
    username_input = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    username_input.send_keys(USERNAME)

    password_input = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password_input.send_keys(PASSWORD)

    # Click on the login button
    login_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']"))
    )
    login_button.click()

    # Verify login success by checking for a specific element that is present only on the login success page
    try:
        success_element = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/header/nav/div/div/a[1]/span"))
        )
        assert success_element.is_displayed()
        print("Login successful")
        with open("report.html", "w") as report:
            report.write("<html><body><h1>Login Test Report</h1><p>Login successful</p></body></html>")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Login failed: {e}")
        with open("report.html", "w") as report:
            report.write(f"<html><body><h1>Login Test Report</h1><p>Login failed: {e}</p></body></html>")
        pytest.fail(f"Login failed: {e}")
