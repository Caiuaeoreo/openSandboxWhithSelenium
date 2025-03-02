from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from prettytable import PrettyTable

def pegar_dados(driver):
    username = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[1]/div[2]/input').get_attribute('value')
    password = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[2]/div[2]/input').get_attribute('value')
    url = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[3]/div[2]/input').get_attribute('value')
    access_key_id = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[4]/div[2]/input').get_attribute('value')
    secret_access_key = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[5]/div[2]/input').get_attribute('value')
    auto_shutdown = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[6]/div[2]').text

    table = PrettyTable()
    table.field_names = ["Campo", "Valor"]

    table.add_row(["Username", username])
    table.add_row(["Password", password])
    table.add_row(["URL", url])
    table.add_row(["Access Key ID", access_key_id])
    table.add_row(["Secret Access Key", secret_access_key])
    table.add_row(["Auto Shutdown", auto_shutdown])

    print(table)

#from selenium.webdriver.common.by import By
#import time
#
#def pegar_dados(driver):
#    username = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[1]/div[2]/input').get_attribute('value')
#    password = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[2]/div[2]/input').get_attribute('value')
#    url = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[3]/div[2]/input').get_attribute('value')
#    access_key_id = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[4]/div[2]/input').get_attribute('value')
#    secret_access_key = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[5]/div[2]/input').get_attribute('value')
#    auto_shutdown = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[2]/div[6]/div[2]').text
#
#    print(f"Username: {username}")
#    print(f"Password: {password}")
#    print(f"URL: {url}")
#    print(f"Access Key ID: {access_key_id}")
#    print(f"Secret Access Key: {secret_access_key}")
#    print(f"Auto Shutdown: {auto_shutdown}")
