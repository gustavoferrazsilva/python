from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

WP_LINK = 'https://web.whatsapp.com'

## XPATHS
SEND = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]' 
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]' 
NEW_CHAT = '//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div/div[2]/div[1]/div[1]/span'

driver = webdriver.Chrome()
driver.get(WP_LINK)

def enviar(nome):
    try:
        mensagem = driver.find_element(By.XPATH, MESSAGE_BOX) 
        mensagem.click()
        mensagem.send_keys(f'Olá*{nome}*, tudo bem ?')
        mensagem.send_keys(Keys.CONTROL, Keys.RETURN)
        mensagem.send_keys(f'Esta é uma mensagem de *Teste.')
        sleep(3)
        botao = driver.find_element(By.XPATH, SEND)
        botao.click()
        return 'Enviado'
    except Exception as e:
        return 'Sem whatsapp'

listaTelefones = ['5518981492620','5518996121783']
listaNome = ['Jane', 'Gustavo']

contador = True
while contador:
    sleep(3)
    try:
        driver.find_element(By.XPATH, NEW_CHAT)
        contador = False
    except:
        print('Por favor escaneie o QR Code')
        contador = True

envio = []
for nome, telefone in zip(listaNome, listaTelefones):
    try:
        sleep(5)
        url = f'https://web.whatsapp.com/send?phone={telefone}' 
        driver.get(url)
        sleep (8)
        status = enviar(nome)
        print(f'Telefone: {telefone} - {nome} | {status}')
    except Exception as e:
        driver.execute_script("window.stop();")
        print(f'Telefone: {telefone} | ERRO AO ENVIAR')
        status = 'Erro ao enviar'
    envio.append(status)

print (envio)
sleep(8)
driver.close()