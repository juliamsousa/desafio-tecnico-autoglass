# Desafio Técnico RPA I - Grupo Autoglass 🤖

![banner](assets/autoglass-capa.png)

Repositório contendo a implementação do desafio proposto no processo seletivo do Grupo Autgoglass. O desafio foi desenvolvido utilizando a linguagem Python.

## Questão 1 

O enunciado dessa questão propõe o desenvolvimento de um programa contendo uma função que tenha como parâmetros de entrada dois números inteiros e retorne o resultado da multiplicação entre eles. Para a validação da entrada foi utilizada a função _isinstance_ que permite verificar se um objeto pertence ao tipo especificado. Para a conversão dos números ponto flutuante foi utilizada a função _round_ que arredonda o valor para inteiro.

Os casos de teste executados foram:

- Dois números inteiros como parâmetro (7, 2)
- Dois números ponto flutuante (5.8, 2.3)
- Um número inteiro e um número ponto flutuante (10, 1.1)
- Um número ponto flutuante e um número inteiro (1.5, 8)
- Dois caracteres ('a', 'b')
- Um número e um caracter (1, 'b')
- Um número na forma de caracater e outro caracter ('a', '1')

## Questão 2

O enunciado dessa questão propõe o desenvolvimento de um programa contendo uma função que receba uma lista de inteiros e mostre todos os números pares da lista. Para a implementação dos _type_hints_ foi utilizado o módulo _typing_ do Python que permite fazer a verificação de tipos diferentes, como por exemplo List[int]. Para a verificação dos tipos internos da lista também foi utilizada a função _isinstance_, percorrendo todos os itens presentes na lista e verificando se são instâncias de _int_. Para a validação se o número é par foi utilizada a função Módulo (%) que retorna o resto de uma divisão, nesse caso se o resto da divisão por 2 for zero o número é par

Os casos de teste executados foram:

- Uma lista vazia ([])
- Uma lista contendo números inteiros de 1 a 10 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
- Uma lista contendo apenas números inteiros ímpares ([1, 3, 5, 7, 9, 11, 13, 15, 17])
- Uma lista contendo apenas números inteiros pares ([2, 4, 6, 8, 10, 12, 14, 16])
- Uma lista de números ponto flutuante ([2.4, 6.8, 10.12, 14.16])
- Uma lista de caracteres (['a', 'b'])
- Uma lista contendo um número e um caracter ([1, 'b'])
- Uma lista contendo um caracter e um booleano (['a', True]

## Questão 3

O enunciado dessa questão propõe a explicação do seguinte código: 

```` 
    '''
    Importação das bibliotecas necessárias para a execução do código
    A biblioteca requests permite a realização de requisições HTTP
    utilizando Python. O módulo json permite a serialização e
    desserialização de objetos Python no formato JSON.
    
    O JSON, JavaScript Object Notation, consiste em um formato para 
    troca de dados entre sistemas
    '''
    import requests
    import json
    
    '''
    Definição da url da api e endpoint desejados para realização da
    requisição. Trata-se de uma api da ferramenta GitHub.
    '''
    url = 'https://api.github.com/some/endpoint'
    
    '''
    Definição dos headers e payload da requisição HTTP. Em uma 
    requisição HTTP os headers permitem a passagem de informações 
    adicionais de configuração e controle da requisição ao passo
    que o payload contém as informações em si transmitidas.
    '''
    headers = {‘header’: ‘header1’}
    payload = {data: 'data1'}
    
    '''
    Realização da requisição utilizando a biblioteca requests. O 
    método utilizado foi o método post, que faz o envio de dados 
    para uma api. O parâmetro url contém o link da api/endpoint, o
    parâmetro data contém os dados enviados e o parâmetro headers 
    contém as configurações adicionais definidas. A função 
    json.dumps serializa os dados do objeto payload a uma instância 
    de json que é o formato padrão utilizado para requisições HTTP.
    '''
    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    
    '''
    A requisição HTTP retorna um código de status que informa
    resultado (sucesso, erro, bad request, entre outros). Em caso de 
    sucesso, o status retornado é o 200. Após o sucesso da 
    requisição a resposta é extraída, desserializada e imprimida.
    '''
    if resp.status_code == 200:
        resp = json.loads(resp.content)
        print(resp.content)
````

- Importação das bibliotecas necessárias para a execução do código. A biblioteca requests permite a realização de requisições HTTP utilizando Python. O módulo json permite a serialização e desserialização de objetos Python no formato JSON.

- O JSON, JavaScript Object Notation, consiste em um formato para troca de dados entre sistemas.

- Definição da url da api e endpoint desejados para realização da requisição. Trata-se de uma api da ferramenta GitHub.

- Definição dos headers e payload da requisição HTTP. Em uma requisição HTTP os headers permitem a passagem de informações adicionais de configuração e controle da requisição ao passo que o payload contém as informações em si transmitidas.

- Realização da requisição utilizando a biblioteca requests. O método utilizado foi o método post, que faz o envio de dados  para uma api. O parâmetro url contém o link da api/endpoint, o parâmetro data contém os dados enviados e o parâmetro headers contém as configurações adicionais definidas. A função json.dumps serializa os dados do objeto payload a uma instância de json que é o formato padrão utilizado para requisições HTTP.

- A requisição HTTP retorna um código de status que informa resultado (sucesso, erro, bad request, entre outros). Em caso de sucesso, o status retornado é o 200. Após o sucesso da requisição a resposta é extraída, desserializada e imprimida.


## Questão 4

O enunciado dessa questão propõe a análise da estrutura de diretórios e explicação sobre cada pasta/arquivo apresentado, e implementação de um código simples com os seguintes passos:

- A partir do main.py realizar a chamada de uma função ‘ola_mundo()’ presente no arquivo src/ola_mundo.py que deve retornar uma string com uma mensagem qualquer.
- Utilizar o if __name__ == "__main__" para executar a função.
- Demonstrar como importar a função de outro arquivo.

-----------------------------------------------------------------------

Explicação:

- .env: Diretório contendo um ambiente virtual python. Esse ambiente permite a gestão de pacotes e versões em um ambiente isolado para desenvolvimento de aplicações.
- assets: Diretório contendo arquivos complementares ao projeto como: imagens, arquivos de configuarção, chaves, entre outros.
- src: Diretório contendo os códigos fonte da aplicação para melhor organização do projeto.
- logs: Diretório contendo arquivos de log de execução, debug e/ou erro.
- main.py: Arquivo principal da aplicação que realiza a chamada de funções e funcionamento geral da aplicação
- .gitignore: Arquivo de configuração do git contendo as extensões e pastas a serem ignorados do controle de versão
- requirements.txt: Arquivo de texto contendo os requerimentos instalados no ambiente virtual uma vez que, como boa prática, a pasta do ambiente virtual é adicionada ao .gitignore.
- README.me: Arquivo markdown utilizado para desenvolvimento da documentação do projeto.

Obs.: para o desenvolvimento dessa questão foram adicionados logs aos arquivos Python e foi instalado o pacote pandas para adição de dependências ao arquivo requirements.txt como exemplo.
