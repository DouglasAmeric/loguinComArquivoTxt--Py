import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://store.steampowered.com/login/?redir=%3Fl%3Dportuguese&redir_ssl=1&snr=1_4_600__global-header")

arquivo = 'user-login.txt'
with open(arquivo,'r') as file:
    linha = file.readlines()
    print(linha)
    if len(linha) >=2:
        print(linha)
        usuario = linha[0].strip()
        senha = linha[1].strip()
        print(senha)
    else:
        print("Login invalido ou nãop possui login, Favor corrigir")
        exit()

time.sleep(3)
input1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
input1.send_keys(usuario)
time.sleep(3)

input2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input")
input2.send_keys(senha)
time.sleep(3)

iniciarSessao = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button")
iniciarSessao.click()
input()