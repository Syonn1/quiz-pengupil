from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/login.php")
    
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.NAME, "submit")
    
    username.send_keys("irul")
    password.send_keys("irul123")
    submit_button.click()
    
    time.sleep(2)
    assert "index.php" in driver.current_url
    driver.quit()

if __name__ == "__main__":
    test_login_valid()
