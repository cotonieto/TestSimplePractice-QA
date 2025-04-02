import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

#initial setup 
load_dotenv()   

SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless") #Docker execution
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sanbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    #chromedriver used in the PATH
    service = Service(executable_path="C:\\chromedriver\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def create_client_and_verify(driver):
    try:
        #Step 1 go to login page 
        driver.get("https://secure.simplepractice.com")
        time.sleep(2)
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_1.png")
        
        #step2 valid credentials 
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
        
        # Step 5: Click on Create button
        create_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create')]"))
        )
        create_button.click()
        time.sleep(5)
        
        # Step 6: Click on Create client button
        create_client = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create client')]"))
        )
        create_client.click()
        time.sleep(5)
        
        # Step 7: Fill client information
        input_first_name = driver.find_element(By.XPATH, "//input[@name='firstName']")
        input_first_name.send_keys("Carlos")
        input_last_name = driver.find_element(By.XPATH, "//input[@name='lastName' and @type='text']")
        input_last_name.send_keys("Lana")
        time.sleep(2)
        
        # Step 8: Click Continue button
        continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='button primary' and contains(text(), 'Continue')]"))
        )
        continue_button.click()
        
        # Verification
        if "https://secure.simplepractice.com/clients" in driver.current_url:
            print("Successful Test: User redirected to clients page")
            return True
        else:
            print("Unsuccessful Test: User was not redirected correctly")
            return False
            
    except Exception as e:
        print(f"Error in execution: {e}")
        return False

def main():
    driver = setup_driver()
    try:
        success = create_client_and_verify(driver)
        return 0 if success else 1
    finally:
        driver.quit()

if __name__ == "__main__":
    exit(main())