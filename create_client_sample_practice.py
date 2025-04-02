from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os



driver_path = "C:/Users/coton/Documents/ViaroExercise/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
     #step 1 get into the login page
    driver.get("https://secure.simplepractice.com")
    time.sleep(2)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step1_simple_practice.png")
    
    #step2 insert valid credentials and login button
    user = driver.find_element(By.ID, "user_email")
    user.send_keys("somab63683@lewenbo.com")
    password = driver.find_element(By.ID, "user_password")
    password.send_keys("GoodLuck777")
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step2_simple_practice.png")
    driver.find_element(By.XPATH, "//input[@id='submitBtn']" ).click()
    time.sleep(10)
        
    #step3 click in Client section
    driver.find_element(By.XPATH, "//a[@href='/clients']" ).click()
    time.sleep(10)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step3_simple_practice.png")
    
    #step4 click in  "+" button
    create_buttton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create')]"))
    )
    create_buttton.click()
    time.sleep(5)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step4_simple_practice.png")
    
    #step5action the visible button to create a new client 
    create_client = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create client')]"))
    )
    create_client.click()
    time.sleep(5)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step5_simple_practice.png")
    
    
    input_first_name = driver.find_element(By.XPATH, "//input[@name='firstName']")
    input_first_name.send_keys("Carlos")
    input_last_name = driver.find_element(By.XPATH, "//input[@name='lastName' and @type='text']")
    input_last_name.send_keys("Urur")
    time.sleep(2)
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='button primary' and contains(text(), 'Continue')]"))
    )
    continue_button.click()
    #time.sleep(5)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/new_client_step6_simple_practice.png")
    
    
    #verification user redirected
    if "https://secure.simplepractice.com/clients" in driver.current_url:
        print("Test Passed: New User created!")
    else:
        print("Test Failed: User was not created properly")
        
except Exception as e:
    print (f"Execution Error: {e}")
    
finally:
    driver.quit()