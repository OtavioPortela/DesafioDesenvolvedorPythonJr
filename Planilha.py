import pandas as pd
import EnviaEmail

vendas = pd.read_excel('vendas.xlsx')

clientes = vendas[['Cliente']]

Coluna_Clientes = []
for i in range(1,21):
    linha = 'Cliente '+ str(i)
    Coluna_Clientes.append(linha)

print(vendas.loc[:,['Cliente', 'Valor-Pago']])

associados =[]
for i in range(0,20):
    associado = clientes.Cliente == Coluna_Clientes[i]
    associados.append(associado)

for valor in range(0, 20):
    print(vendas[associados[valor]])
    df = vendas[associados[valor]]


    dfsum = df['Valor-Pago'].sum()
    dfcont =df['Cliente'].count()
    print('Total vendido no ano de 2021: ', int(dfsum))
    print('numero de vendas no ano de 2021 foi: ', dfcont)
    Cliente = 'Cliente'+str(valor+1)
    enviar = EnviaEmail.enviar_email(Cliente, dfcont, dfsum)



#associados.append( clientes.Cliente == coluna_cliente[i] for i in range(1,20))