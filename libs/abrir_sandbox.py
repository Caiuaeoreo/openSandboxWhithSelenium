from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def abrir_sandbox(driver):
    try:
        time.sleep(10)
        sandbox_aws = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div[1]/div[2]/div/div[1]/div/button'))
        )
        sandbox_aws.click()
        time.sleep(5)
        print("Sandbox criada.")
    except Exception as e:
        print("Erro ao tentar criar a sandbox ( Normalmente ou já existe uma sandbox ou a página não carregou a tempo ):", e)
        exit()

