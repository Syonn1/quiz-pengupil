from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/login.php")
    
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.NAME, "submit")
    
    username.send_keys("valid_user")
    password.send_keys("valid_password")
    submit_button.click()
    
    time.sleep(2)
    assert "index.php" in driver.current_url
    driver.quit()

def test_login_invalid():
    driver = webdriver.Chrome()
    driver.get("http://localhost/login.php")
    
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.NAME, "submit")
    
    username.send_keys("invalid_user")
    password.send_keys("wrong_password")
    submit_button.click()
    
    time.sleep(2)
    assert "Register User Gagal" in driver.page_source
    driver.quit()

def test_login_empty_fields():
    driver = webdriver.Chrome()
    driver.get("http://localhost/login.php")
    
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    
    time.sleep(2)
    assert "Data tidak boleh kosong" in driver.page_source
    driver.quit()

if __name__ == "__main__":
    test_login_valid()
    test_login_invalid()
    test_login_empty_fields()
