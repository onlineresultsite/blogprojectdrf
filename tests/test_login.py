# ecom_app/tests/test_login.py



import pytest
import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the workbook and sheet outside the functions
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Test Results"

row_counter = 1
@pytest.fixture(scope="module")
def setup():
    # Setup the WebDriver
    driver = driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')  # Use the browser you prefer
    yield driver
    # Teardown
    driver.quit()

@pytest.fixture
def login_setup():
    # Placeholder for any additional setup actions specific to each user login
    pass

def login(driver, username, password):
    driver.get("http://13.53.206.233:8000/login/")

    try:
        # Wait for username input field to be visible
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[1]/input"))
        )
        username_input.send_keys(username)

        # Find password input field
        password_input = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[2]/input")
        password_input.send_keys(password)

        # Click on the login button
        login_button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[3]/button")
        login_button.click()


    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
        assert False, "Timeout waiting for element."

    finally:
        # Add any necessary cleanup or verification steps here
        pass

@pytest.mark.parametrize("username, password", [
   


     ("akshay", "akTR@300",),        # collection report, todays performance,

])

def test_my_requests(setup, username, password):
    driver = setup

    login(driver, username, password)


