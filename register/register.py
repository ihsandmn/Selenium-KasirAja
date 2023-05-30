import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Scenario Register

    def test_register_user(self):  # Register User Successfully
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//a[normalize-space()='ingin mencoba, daftar ?']"
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Hey Bro")
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("heybro@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='daftar']").click()
        time.sleep(2)

    def test_register_user_failed_1(
        self,
    ):  # Register User Unsuccessfully - Nama Toko Empty
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//a[normalize-space()='ingin mencoba, daftar ?']"
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys("heybro@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='daftar']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_register_user_failed_2(self):  # Register User Unsuccessfully - Email Empty
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//a[normalize-space()='ingin mencoba, daftar ?']"
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Hey Bro")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='daftar']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_register_user_failed_3(
        self,
    ):  # Register User Unsuccessfully - Invalid Email
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//a[normalize-space()='ingin mencoba, daftar ?']"
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Hey Bro")
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("heybro")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("qwerty10")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='daftar']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)

    def test_register_user_failed_4(
        self,
    ):  # Register User Unsuccessfully - Empty Password
        driver = self.browser
        driver.get("https://kasirdemo.belajarqa.com")
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//a[normalize-space()='ingin mencoba, daftar ?']"
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Hey Bro")
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("heybro@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='daftar']").click()
        time.sleep(2)
        response_data = driver.find_element(By.XPATH, "//div[@role='alert']").text
        print(response_data)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
