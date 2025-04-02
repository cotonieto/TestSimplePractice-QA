from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os



driver_path = "C:/Users/coton/Documents/ViaroExercise/chromedriver.exe"   #<--please change the rout when running locally
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    #step 1 get into the login page 
    driver.get("https://secure.simplepractice.com")
    time.sleep(2)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/login_step1_simple_practice.png") #<--please change the rout when running locally
    
    #step2 insert valid credentials
    user = driver.find_element(By.ID, "user_email")
    user.send_keys("somab63683@lewenbo.com")
    password = driver.find_element(By.ID, "user_password")
    password.send_keys("GoodLuck777")
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/login_step2_simple_practice.png")  #<--please change the rout when running locally
    
    #step3 click login button
    driver.find_element(By.XPATH, "//input[@id='submitBtn']" ).click()
    time.sleep(10)
    driver.save_screenshot("C:/Users/coton/Documents/ViaroExercise/screenshots/login_step3_simple_practice.png")  #<--please change the rout when running locally
    
    #verification user redirected
    if "https://secure.simplepractice.com/calendar/appointments" in driver.current_url:
        print("Test Passed: User redirected to the main page")
    else:
        print("Test Failed: User was not redirected to the main page")
        
except Exception as e:
    print (f"Execution Error: {e}")
    
finally:
    driver.quit()