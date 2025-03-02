from libs.web_browser import web_browser
from libs.login import login
from libs.abrir_sandbox import abrir_sandbox
from libs.pegar_dados import pegar_dados
from libs.perguntar_fechar_sandbox import perguntar_fechar_sandbox

driver = web_browser()

login(driver)
abrir_sandbox(driver)
pegar_dados(driver)
perguntar_fechar_sandbox(driver)

driver.quit()

