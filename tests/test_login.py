# ecom_app/tests/test_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

class LoginPageTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Ensure ChromeDriver is correctly installed
        cls.selenium.implicitly_wait(10)  # Wait for elements to load

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()  # Close browser after tests
        super().tearDownClass()

    def test_login_page(self):
        # Navigate to the login page
        self.selenium.get('http://13.53.206.233:8000/login/')  # Use the actual URL

        try:
            # Find the login form elements (adjust selectors as needed)
            username_input = self.selenium.find_element(By.XPATH, '/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[1]/input')  # Adjust ID if necessary
            password_input = self.selenium.find_element(By.XPATH, '/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[2]/input')  # Adjust ID if necessary
        
            login_button = self.selenium.find_element(By.XPATH, '/html/body/div/section/div/div/div/div/div/div[1]/div/form/div[3]/button')  # Adjust ID if necessary

            # Input username and password
            username_input.send_keys('akshay')  # Replace with a valid username
            password_input.send_keys('akTR@300')  # Replace with a valid password
          
            # Click the login button
            login_button.click()

            # Check if login was successful
            try:
                # Adjust selector to check for successful login (e.g., redirected URL or success message)
                success_message = self.selenium.find_element(By.XPATH, '/html/body/div/header/nav/div/div/a[1]')  # Adjust ID or use an appropriate method
                self.report_success("Login successful")
            except:
                self.report_error("Login failed. Check credentials or login process.")
        except Exception as e:
            self.report_error(f"An error occurred: {e}")

    def report_success(self, message):
        print(f"Success: {message}")
        self.generate_report(message, success=True)

    def report_error(self, message):
        print(f"Error: {message}")
        self.generate_report(message, success=False)

    def generate_report(self, message, success):
        report_path = '/home/ubuntu/blogprojectdrf/tests/report.html'
        with open(report_path, 'a') as report_file:
            if success:
                report_file.write(f"<p style='color: green;'>{message}</p>")
            else:
                report_file.write(f"<p style='color: red;'>{message}</p>")
