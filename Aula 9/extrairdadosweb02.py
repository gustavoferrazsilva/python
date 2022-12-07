from requests import get
from bs4 import BeautifulSoup
from os import system
system ('cls')

url = 'https://www.imdb.com/search/title/?release_date=2022-01-01,2022-12-31&sort=user_rating,desc'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

filmes = html_soup.find_all('div',class_= 'lister-item mode-advanced') # leitura do arquivo html

print(len(filmes))

for indice in range(10):
    filme_dados = filmes[indice]
    nome = filme_dados.h3.a.text
    lancamento = filme_dados.h3.find('span',class_='lister-item-year text-muted unbold')
    votos = filme_dados.find('span',attrs = {'name': 'nv'})
    episodios = filme_dados.h3.find('small','text-primary unbold')

    x =''
    if episodios is not None: 
        ep = filme_dados.find_all('a')
        x = ' - Epsisodio: ' + ep[2].text
    print (f'{indice+1} - {nome} {lancamento.text}\nPontuação: {filme_dados.strong.text} - votos: {votos.text}')