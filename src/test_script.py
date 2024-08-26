from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Initialize temp_file_path to avoid NameError
temp_file_path = ""

# Set up the ChromeDriver service and options
service = Service(executable_path=os.path.join("C:", "swathi_online training", "JarFiles", "Chromedriver", "chromedriver-win64", "chromedriver-win64", "chromedriver.exe"))
options = webdriver.ChromeOptions()

try:
    driver = webdriver.Chrome(service=service, options=options)

    # Define your variables
    n1 = "Hello"
    n2 = "World"

    # Create the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>hello world</title>
    </head>
    <body>
    <h1>{n1} <br> {n2}</h1>Hello World!!!!Welcome Swathi

    <p> {n1} <br> </p>
    </body>
    </html>
    """

    # Write the HTML content to a temporary file
    temp_file_path = os.path.abspath("temp_hello_world.html")
    with open(temp_file_path, "w") as file:
        file.write(html_content)

    # Open the temporary HTML file in the browser
    driver.get("file://" + temp_file_path)

    # Maximize the browser window
    driver.maximize_window()
    time.sleep(15)

    # Print "hello world!" to the console
    print("hello world!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the driver is closed and the file is removed
    if 'driver' in locals():
        driver.quit()

    if temp_file_path and os.path.exists(temp_file_path):
        os.remove(temp_file_path)
