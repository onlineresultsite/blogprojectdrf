import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the workbook and sheet outside the functions






@pytest.fixture(scope="module")
def setup():
    # Setup the WebDriver with Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Optional, if running in headless mode

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    # Teardown
    driver.quit()

def login(driver, username, password):
    driver.get("http://13.53.206.233:8000/login/")
    
    try:
        # Wait for username input field to be visible
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys(username)

        # Find password input field
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()

        # Verify login success (adjust as necessary for your application)
        WebDriverWait(driver, 20).until(
            EC.url_changes("http://13.53.206.233:8000/login/")
        )

        # Check if the login was successful based on URL or a specific element
        if driver.current_url == "http://13.53.206.233:8000/home/":
            status = "Success"
            message = "Login successful"
        else:
            status = "Failure"
            message = "Login failed or unexpected URL"

    except TimeoutException as e:
        status = "Failure"
        message = f"TimeoutException occurred: {e}"

    except NoSuchElementException as e:
        status = "Failure"
        message = f"NoSuchElementException occurred: {e}"

    finally:
        # Debugging information
        print(f"Current URL: {driver.current_url}")
        print(f"Page HTML: {driver.page_source[:1000]}")  # Print the first 1000 characters of HTML
        
        # Write results to the Excel sheet
        global row_counter
        # Add your code to write the result to the Excel sheet here


@pytest.mark.parametrize("username, password", [
    ("akshay", "akTR@300"),
])
def test_my_requests(setup, username, password):
    driver = setup
    login(driver, username, password)



