from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()


def test_google(setup):
    driver = setup
    driver.get("https://google.com/")
    txt=driver.find_element(By.XPATH,'//textarea[@id="APjFqb"]')
    txt.send_keys("Hello world");
    txt.send_keys(Keys.ENTER);
    