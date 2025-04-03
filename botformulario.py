import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Solicita os dados todos de uma vez
dados = input("Digite os dados no formato: Nome, CPF, CPNJ, RzSocial, RH/CNH...\n")

#caminho_driver = 'C:\Users\david\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Divide os dados em uma lista
try:
    nome = [dado.strip() for dado in dados.split(",")]
    #, cpf, cpnj, razaoSocial, rgCnh, filiacao, dataNascimento, estadoCivil, profissao, banco, agencia, conta, email, cep, pais, estado, cidade, bairro, rua, nmrCasa, complemento
except ValueError:
    print("Erro: Certifique-se de fornecer os dados separados por vírgula.")
    exit()


time.sleep(5)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Faz com que o navegador fique aberto

# Iniciar o driver com essa opção
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.agendor.com.br/entrar/")

# Preenche os campos (Ajuste os seletores conforme necessário)
try:
    driver.find_element(By.ID, "email").send_keys(nome)
  #  driver.find_element(By.NAME, "cpf").send_keys(cpf)
   # driver.find_element(By.NAME, "razao").send_keys(razaoSocial)
   # driver.find_element(By.NAME, "cargo").send_keys(profissao)
    

    print("Dados preenchidos com sucesso!")
except Exception as e:
    print(f"Erro ao preencher o formulário: {e}")