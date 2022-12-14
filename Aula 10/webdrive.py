import io
import sys
import zipfile
import os
import urllib.request as request

from requests import get
from bs4 import BeautifulSoup
from os import system

system ('cls')
# função de download
BUFF_SIZE=1024
def download(response,output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len (data)
        if not data:
            break
        output.write(data)
    print('Tamanho do arquivo {bytes}'.format(bytes=total_downloaded))

def zip(path):
    if not os.path.exists(path):
        print(f'Arquivo {path} não existe!')
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos Extraídos")



# montando url download - início
url = 'https://chromedriver.chromium.org/downloads'

response = get (url)

print(response.status_code)

html_soup = BeautifulSoup(response.text, 'html.parser')

tags = html_soup.find_all('ul') 

for  i in range(len(tags)): # percorrer todos os itens da lista "tags"#
    if tags[i].text.find('you are using Chrome version') > 0:
        listas = tags[i].find_all('li')
        if len(listas) >= 1:
            print (listas[1].text)
            print(listas[1].text[-13:])
            urldownload = f'https://chromedriver.storage.googleapis.com/{listas[1].text[-13:]}/chromedriver_win32.zip'
            print(urldownload)
            # montando url download - fim

            # realizando download automático - início
            response = request.urlopen(urldownload)
            pasta = os.path.abspath(os.getcwd())

            out_file = io.FileIO(f'{pasta}\chromedriver_win32.zip', mode ='w')
            download(response,out_file)
            zip(f'{pasta}\chromedriver_win32.zip')
            print(f'Download realizado na página {urldownload}')