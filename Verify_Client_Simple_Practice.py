import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

# Initial setup
load_dotenv()
SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def setup_driver():
    service = Service(executable_path="C:\\chromedriver\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver

def search_client_and_verify(driver):
    try:
        # Step 1: Go to login page
        driver.get("https://secure.simplepractice.com")
        time.sleep(2)
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_1.png")
        
        # Step 2: Enter valid credentials
        user = driver.find_element(By.ID, "user_email")
        user.send_keys(os.getenv("USER_EMAIL"))
        
        password = driver.find_element(By.ID, "user_password")
        password.send_keys(os.getenv("USER_PASSWORD"))
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_2.png")
        
        # Step 3: Click login button
        driver.find_element(By.XPATH, "//input[@id='submitBtn']").click()
        time.sleep(10)
        
        # Step 4: Click on Clients menu
        driver.find_element(By.XPATH, "//a[@href='/clients']").click()
        time.sleep(10)
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/clients_page.png")
        
        # Step 5: Search for client
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.utility-search"))
        )
        search_field.send_keys("Lana")
        time.sleep(3)
        
        try:
            # Step 6: Verify client exists
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.record-name")))
            full_name = element.text.strip()
            
            if "Lana" in full_name:
                print("Successful Test: Last name is registered")
            else:
                print("Unsuccessful Test: Last name not found")
            
            driver.save_screenshot(f"{SCREENSHOTS_DIR}/search_result.png")
        except TimeoutException:
            print("Unsuccessful Test: Last name cell did not appear on the page")
            driver.save_screenshot(f"{SCREENSHOTS_DIR}/search_failure.png")
            
        # Verification
        if "https://secure.simplepractice.com/clients" in driver.current_url:
            print("Successful Test: User remains on clients page")
            return True
        else:
            print("Unsuccessful Test: User was not on the correct page")
            return False
            
    except Exception as e:
        print(f"Error in execution: {e}")
        return False

def main():
    driver = setup_driver()
    try:
        success = search_client_and_verify(driver)
        return 0 if success else 1
    finally:
        driver.quit()

if __name__ == "__main__":
    exit(main())