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

    try:
        # Find the username and password input fields
        username_input = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_input.send_keys(USERNAME)

        password_input = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys(PASSWORD)

        # Click on the login button
        login_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # Verify login success
        success_element = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Login']"))
        )
        assert success_element.is_displayed()
        print("Login successful")
        with open("report.html", "w") as report:
            report.write("<html><body><h1>Login Test Report</h1><p>Login successful</p></body></html>")
    except TimeoutException as e:
        print("TimeoutException: ", e)
        with open("report.html", "w") as report:
            report.write("<html><body><h1>Login Test Report</h1><p>Login failed due to TimeoutException: {}</p></body></html>".format(e))
        browser.save_screenshot('screenshot.png')
        print("Screenshot saved as 'screenshot.png'")
        print("Page source:")
        print(browser.page_source)
        pytest.fail(f"Login failed: {e}")

# Run the test and generate a report
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", "--self-contained-html", "test_login.py"])
