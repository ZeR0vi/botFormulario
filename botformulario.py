import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Solicita os dados todos de uma vez
dados = input("Digite os dados no formato: Nome, CPF, CPNJ, RzSocial, RH/CNH...\n")

# Divide os dados em uma lista
try:
    nome, cpf, cpnj, razaoSocial, rgCnh, filiacao, dataNascimento, estadoCivil, profissao, banco, agencia, conta, email, cep, pais, estado, cidade, bairro, rua, nmrCasa, complemento= [dado.strip() for dado in dados.split(",")]
except ValueError:
    print("Erro: Certifique-se de fornecer os dados separados por vírgula.")
    exit()

# Aguarda carregar a página
time.sleep(5)

driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado
driver.get("https://beta.agendor.com.br/people/new")

# Preenche os campos (Ajuste os seletores conforme necessário)
try:
    driver.find_element(By.NAME, "name").send_keys(nome)
    driver.find_element(By.NAME, "cpf").send_keys(cpf)
    driver.find_element(By.NAME, "cpnj").send_keys(cpnj)
    print("Dados preenchidos com sucesso!")
except Exception as e:
    print(f"Erro ao preencher o formulário: {e}")