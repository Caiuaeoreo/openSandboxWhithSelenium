from libs.fechar_sandbox import fechar_sandbox

def perguntar_fechar_sandbox(driver):
    while True:
        resposta = input("Deseja fechar a sandbox? (sim/fechar): ").strip().lower()

        if resposta in ['sim', 'fechar']:
            fechar_sandbox(driver)
            break 
        else:
            print("A sandbox não foi fechada. Tente novamente.")
