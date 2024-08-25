import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver service
        self.service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_title(self):
        # Test if the title is correct
        self.driver.get("file://" + os.path.abspath("temp_hello_world.html"))
        self.assertEqual(self.driver.title, "hello world")
