from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_empty_fields():
    driver = webdriver.Chrome()
    driver.get("http://localhost/login.php")
    
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    
    time.sleep(2)
    assert "Data tidak boleh kosong" in driver.page_source
    driver.quit()

if __name__ == "__main__":
    test_login_empty_fields()
