# Importando duas bibliotecas necessarias
import requests
from bs4 import BeautifulSoup

# Passando o link do site 
response = requests.get('https://g1.globo.com/')

# Transformando e lendo o site com o beautifulsoup
content = response.content
site = BeautifulSoup(content, 'html.parser')

#FIXANDO O HTML DA NOTICIA NA VARIAVEL
noticias = site.findAll('div', attrs={'class' :'feed-post-body'})

# FUNÇÃO PARA VALIDAR SOMENTE NOMES
def valida_nomes():
    while True:
           #FUNÇÃO UPPER PARA TRANSFORMAR OS NOMES EM MAIUSCULO NA HORA DE PRINTAR NO TERMINAL
            name = input("Digite seu nome: ").upper()
            if all(c.isalpha() or c.isspace() for c in name):
                break
            else:
                 print("Por favor digite um nome válido (somente letras e espaços)")
    return name

# NESSE CASO A PROPRIA VARIÁVEL CHAMA A FUNÇÃO 
nome_pessoa = valida_nomes()

# FUNÇÃO PARA VALIDAR SOMENTE NUMEROS
def validar_numeros():
    while True:
    
        # Verifica se a entrada é composta por numeros maiores que 0 e menor que 8
        while True:
              qtd_noticias = int(input("Digite o número de noticias de [0 a 8]: "))
              if qtd_noticias > 0 and qtd_noticias <= 8 :
                   break
              else:
                   print()
                   print('ERRO! Por favor, digite um numero entre [0 e 8]')
       
        # Verifica se a entrada é composta apenas por dígitos
        qtd_noticias = str(qtd_noticias)
        if qtd_noticias.isdigit():
            numero = int(qtd_noticias)
            return numero
        else:
            print("Por favor, digite apenas números.")
        return numero
contador = 1

# NESSE CASO A PROPRIA VARIÁVEL CHAMA A FUNÇÃO
resp = validar_numeros()

# ULTILIZANDO UM LAÇO PARA ITERAR SOBRE AS ULTIMAS NOTICIAS DO SITE.
for noticia in noticias:
        if contador == resp + 1 :
            break
        
        #BUSCA DA CLASS DO TITULO
        print()
        titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
        print(f'{contador} -- TITULO: {titulo.text}')
       
        # Capturando o link e colocando-o em uma variavel
        link = titulo['href'] 
        sub_titulo = noticia.find('a', attrs={'class':'feed-post-body-title'})
        
        #VERIFICANDO SE CONTEM UM SUBTITULO DENTRO DO TITULO
        if (sub_titulo):
            print(f'SUBTITULO: {sub_titulo.text}')
        print(f'Link: {link}')
        print()
        contador +=1
