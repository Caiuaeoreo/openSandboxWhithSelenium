#from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#
#def web_browser():
#    options = Options()
#    # Defina o caminho para o perfil do Firefox
#    profile_path = "/path/to/your/firefox/profile"
#    options.set_preference("profile", profile_path)
#
#    # Usar o Firefox com o perfil configurado
#    driver = webdriver.Firefox(options=options)
#    driver.get("https://learn.acloud.guru/cloud-playground/cloud-sandboxes")
#    driver.maximize_window()
#    print("-------------------------- Acessado CloudGuru --------------------------")
#    return driver


from selenium import webdriver
import time

def web_browser():
    driver = webdriver.Chrome()
    driver.get("https://learn.acloud.guru/cloud-playground/cloud-sandboxes")
    driver.maximize_window()
    time.sleep(1)
    #driver.minimize_window()
    print("-------------------------- Acessado CloudGuru --------------------------")
    time.sleep(3)
    return driver
