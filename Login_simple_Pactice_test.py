import os 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

def login_and_verify(driver):
    try:
        #Step 1 go into the login page
        driver.get("https://secure.simplepractice.com")
        time.sleep(2)
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_1.png")
        
        #Step 2 insert valid credentials 
        user = driver.find_element(By. ID, "user_email")
        user.send_keys(os.getenv("USER_EMAIL"))
        
        password = driver.find_element(By.ID, "user_password")
        password.send_keys(os.getenv("USER_PASSWORD"))
        
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_2.png")
        
        #step2 click in enter button 
        driver.find_element(By.XPATH, "//input[@id='submitBtn']").click()
        time.sleep(10)
        driver.save_screenshot(f"{SCREENSHOTS_DIR}/login_step_3.png")
        
        #verification
        if "https://secure.simplepractice.com/calendar/appointments" in driver.current_url:
            print("Successful Test: User redirected to the main page")
            return True
        else:
            print("Unsuccessful Test: The user was not redirected to the main page")
            return False
        
    except Exception as e:
        print(f"Error in execution: {e}")
        return False
    
def main():
    driver = setup_driver()
    try:
        success = login_and_verify(driver)
        return  0 if success else 1
    finally:
        driver.quit()
if __name__ == "__main__":
    exit(main())
