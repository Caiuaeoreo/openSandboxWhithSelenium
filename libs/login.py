from selenium.webdriver.common.by import By
import time

def login(driver):
    time.sleep(10)
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys("email@email.com")

    pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    pass_field.send_keys("senhadoseuuser")

    time.sleep(15)

    sign_in = driver.find_element(By.XPATH, '//*[@id="login"]')
    sign_in.click()
    
    time.sleep(5)
