import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# Initialize the workbook and sheet outside the functions
wb = Workbook()
sheet = wb.active
sheet.title = "Test Results"

# Add header row to the sheet
headers = ["Username", "Password", "Status", "Message"]
sheet.append(headers)

# Define a style for the header row
header_font = Font(bold=True)
header_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

for cell in sheet[1]:
    cell.font = header_font
    cell.fill = header_fill

row_counter = 2

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
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Click on the login button
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
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

    finally:
        # Write results to the Excel sheet
        global row_counter
        sheet.append([username, password, status, message])
        row_counter += 1

@pytest.mark.parametrize("username, password", [
    ("akshay", "akTR@300"),
])
def test_my_requests(setup, username, password):
    driver = setup
    login(driver, username, password)

# Save the results to an Excel file after all tests have been run
def pytest_sessionfinish(session, exitstatus):
    wb.save("test_results.xlsx")
