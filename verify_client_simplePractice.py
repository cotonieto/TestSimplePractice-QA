from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import os



driver_path = "C:/Users/coton/Documents/ViaroExercise/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    #step 1 go to the login page
    driver.get("https://secure.simplepractice.com")
    time.sleep(2)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/verify_client_step1_simple_practice.png")
    
    #step2 insert valid credentials and login button
    user = driver.find_element(By.ID, "user_email")
    user.send_keys("somab63683@lewenbo.com")
    password = driver.find_element(By.ID, "user_password")
    password.send_keys("GoodLuck777")
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/verify_client_step2_simple_practice.png")
    driver.find_element(By.XPATH, "//input[@id='submitBtn']" ).click()
    time.sleep(10)
    
    #step 3 click in client box
    driver.find_element(By.XPATH, "//a[@href='/clients']" ).click()
    time.sleep(10)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/verify_client_step3_simple_practice.png")
    searh_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.utility-search"))
    )
    searh_field.send_keys("Urur")
    time.sleep(3)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/verify_client_step3_simple_practice.png")
    
    #Step4 checkk for coincidences 
    try:
        
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.record-name")))
        
        full_name = element.text.strip()
        
        if "Urur" in full_name:
            print("Test Passed: User is registered already!")
        else:
            print("Test failed: User not found")
    
        driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/verify_client_step4_simple_practice.png")
    except TimeoutException:
        #if nothing shows after some time the below message will be printed 
        print("Test Failed: no result found")
        driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/verify_client_step4_failure_simple_practice.png")  # Tomar screenshot de la falla
        
        
    if "https://secure.simplepractice.com/clients?search=Urur" in driver.current_url:
        print("Test Passed: Verification of registered user completed")
    else:
        print("Test Failed: User not registered")
        
except Exception as e:
    print (f"Error durante la ejecucion: {e}")
    
finally:
    driver.quit()