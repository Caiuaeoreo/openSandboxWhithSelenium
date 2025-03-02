from selenium.webdriver.common.by import By
import time

def fechar_sandbox(driver):
    try:
        # Botão para fechar a sandbox
        botao_fechar = driver.find_element(By.XPATH, '//*[@id="tabs-:rg:--tabpanel-0"]/div/div[1]/div/div[3]/button')
        botao_fechar.click()
        time.sleep(2)
        botao_fechar2 = driver.find_element(By.XPATH, '//*[@id="chakra-modal-:r2a:"]/footer/button[2]')
        botao_fechar2.click()
        print("Sandbox fechada.")
    except Exception as e:
        print("Erro ao tentar fechar a sandbox:", e)
