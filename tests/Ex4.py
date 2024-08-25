from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import os

# Set up the ChromeDriver service and options
service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# Open the temporary HTML file in the browser
driver.get("file://" + os.path.abspath("hello.html"))

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

# Print "hello world!" to the console
print("hello world!")

# Close the driver
driver.quit()

