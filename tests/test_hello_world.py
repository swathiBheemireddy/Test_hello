import os
from selenium import webdriver
import pytest

def test_html_file_creation():
    # Assuming the script creates 'temp_hello_world.html'
    os.system("python src/test_script.py")  # Run the script to generate the file
    assert os.path.exists('temp_hello_world.html')

def test_html_content():
    with open('temp_hello_world.html', 'r') as file:
        content = file.read()
        assert "<h1>Hello <br> World</h1>" in content

def test_webdriver_initialization():
    driver = webdriver.Chrome()
    assert driver is not None
    driver.quit()

def test_browser_title():
    driver = webdriver.Chrome()
    driver.get("file://" + os.path.abspath("temp_hello_world.html"))
    assert driver.title == "hello world"
    driver.quit()

def test_page_content():
    driver = webdriver.Chrome()
    driver.get("file://" + os.path.abspath("temp_hello_world.html"))
    body_text = driver.find_element_by_tag_name('body').text
    assert "Hello World!!!! Welcome Swathi" in body_text
    driver.quit()

def test_cleanup():
    os.remove('temp_hello_world.html')
    assert not os.path.exists('temp_hello_world.html')
