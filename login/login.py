import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Scenario Login

    def test_login_user(self):  # Login Successfuly
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("heybro@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='login']").click()
        time.sleep(2)

    def test_login_user_failed_1(self):  # Invalid Login
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("muhammadihsandaimun@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("ihsandaimun16")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='login']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_login_user_failed_2(self):  # Login Unsuccessfully - Invalid Email
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("heybro")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='login']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_login_user_failed_3(self):  # Login Unsuccessfully - Empty Email
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='login']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_login_user_failed_4(self):  # Login Unsuccessfully - Empty Password
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("heybro@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='login']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
