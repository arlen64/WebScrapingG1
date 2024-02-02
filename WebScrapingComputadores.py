from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Abrindo o site com o selenium
driver = webdriver.Chrome()

# Passando o site para a variável do python
site = "https://www.novaliderinformatica.com.br/computadores-gamers"

# Entrando com o chrome drive no site escolhido
driver.get(site)
#procurando os titulos dos produtos
titulos = driver.find_elements(By.XPATH,"//a[@class= 'nome-produto']")

#procurando os preços dos produtos
precos = driver.find_elements(By.XPATH,"//strong[ @class= 'preco-promocional']")

#criando uma planilha
WebProdutos = openpyxl.Workbook()

#criando a pagina 'produtos'
WebProdutos.create_sheet('produtos')

#Criando os arquivos passando como parâmetro a lista de produtospip
pagina_de_produtos = WebProdutos['produtos']

# Inserindo valores nas colunas da página produtos
pagina_de_produtos ['A1'].value = 'nome_produto'
pagina_de_produtos['B1'].value = 'preço_produto'

# usando a função 'zip' do for para adcionar somente os dados que contem nas duas listas ex.(titulos, precos)
# A função só adciona na planilha os dados que tem valores nas duas listas. ex(titulos,precos)
for titulo, preco in zip(titulos,precos):
    pagina_de_produtos.append([titulo.text,preco.text])

# Salvando a planilha e lembrar da extensão xlsx, colocando o cmd por última linha para ele salvar depois de atualizar o 'for'. 
WebProdutos.save('produtosInfo24.xlsx')
