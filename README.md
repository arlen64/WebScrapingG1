# G1 News Scraping

Este é um projeto simples de web scraping desenvolvido em Python para extrair as últimas notícias do site G1 (globo.com)<br />
Nesse projeto é realizado uma extração de até 8 notícias do site sendo elas as notícias atualizadas dando ao usuário a oportunidade de escolher quantas notícias quer exibir.<br />
Obs: O usuário não consiguirá exibir mais de 8 notícias <br />



## Bibliotecas necessárias:

- Requests
- BeautifulSoup

# Funções/variáveis:

Função valida_nomes() : Consiste em validar somente strings na variável <br />
Função validar_numeros() : Verifica se o usuário digita apenas numeros, sendo eles entre 0(zero) e 8(oito)

## Objetivo

O objetivo principal deste projeto é fornecer uma ferramenta de scraping para coletar notícias do G1 de maneira automatizada de forma que o usuário interaja com o código digitando seu nome e escolhendo quantas notícias quer exibir (até 8 notícias). <br/>
O script retorna o Título, Subtítulo e link da notícia. <br/>
Esse código pode ser usado como base para projetos mais avançados ou para entender os conceitos básicos de scraping.

## Como Usar

Para utilizar este projeto, siga os passos abaixo:

### Instalação das Dependências:

Certifique-se de ter o Python instalado em seu ambiente. Este projeto foi desenvolvido usando Python 3.x.

Utilize o comando abaixo para instalar as dependências necessárias:

```bash
pip3 install -r requirements.txt
```

### Execução do Scraping:

Após a instalação das dependências, você pode executar o arquivo `WebScrapingG1.py` para iniciar o scraping das notícias.

```bash
python3 WebScrapingG1.py
```

### Resultado:

O código irá coletar as últimas notícias do G1, exibindo os títulos, subtítulos (se conter subtítulo) e links das notícias obtidas no console. <br />
Obtendo até 8 notícias do site.

## Estrutura de Pasta

A estrutura de pastas do projeto está organizada da seguinte maneira:

```bash
-   `README.md`: Documentação explicando o projeto, instruções de uso e informações gerais.
-   `WebScrapingG1.py`: Script que contém o código fonte do projeto.
-   `requirements.txt`: Lista todas as dependências do projeto para facilitar a instalação.



## Avisos Importantes

-   **Uso Responsável:** Este projeto foi desenvolvido para fins educacionais e de aprendizado. Sempre respeite os termos de serviço dos sites ao realizar web scraping.

-   **Limitações e Restrições:** O scraping de sites pode ser contra os termos de serviço de alguns sites. Verifique as políticas de uso e os limites de solicitação do site alvo antes de executar o código.
