# Desafio Desnvolvedor Python
Desafio feito por uma empresa para a vaga de desenvolvedor Python 

## Escopo do problema
Dado o conjunto de dados em anexo, sendo que cada linha representa um pedido realizado por um
usuário, é pedido que a seguinte tarefa seja realizada:

1. Extraia os dados e faça um sumário com o consolidado de número de vendas e valor de
vendas para cada cliente do ano de 2021.
2. Crie uma automação que envie um e-mail personalizado para cada cliente que contenha o
sumário do item 1. Todos os relatórios individuais devem ser enviados para xxxxxxxxxxxxxx

## Explicação da resolução 
O projeto foi feito utilizando 3 arquivos e 3 Bibliotecas externas.
O primeiro foi nomeado como Planilha.py onde ocorre as funções principais de nosso projeto neste
arquivo utilizo a biblioteca pandas para fazer a análise de um arquivo excel e separar ele em vários DataFrames
de acordo com o nome do Cliente no caso e numerado de 1 a 20.
Feito isso também utilizei algumas funções prontas do pandas como count e sum para somar o número de vendas e o valor total vendido no ano de 2021 
na coluna Valor-Pago.
Por fim com toda esta análise feita eu chamo a função EnviaEmail() que se encontra no arquivo EnviaEmail.py nesta função utilizo duas Bibliotecas especializadas em 
comunicação http do python com o gmail e uma arquivo que por questão de segurança não coloquei as credenciais certas por este ser um diretorio publico chamado Segredos.py
