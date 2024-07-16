import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def setup():
    # Setup the WebDriver with Chrome options for CI
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    # Teardown
    driver.quit()

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

        # Wait for the login to complete (example: wait for dashboard page to load)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/header/nav/div/div/a[1]"))
        )

    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
        assert False, f"Timeout waiting for element. Login failed with credentials: {username}, {password}"

@pytest.mark.parametrize("username, password", [
    ("akshay", "akTR@300"),
    # Add more username and password pairs as needed
])
def test_my_requests(setup, username, password):
    driver = setup
    login(driver, username, password)
    # Add your test assertions here (e.g., check elements on the dashboard)

    # Example assertion (replace with your actual test logic)
    assert "Dashboard" in driver.title, f"Login test failed for user: {username}"

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
