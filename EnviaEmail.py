import smtplib
import email.message
import Segredos

def enviar_email(Cliente, vendas, faturamento):
    corpo_email = f"""
    <h2>Sumario {Cliente}</h2>
    <h4>Número de vendas no ano de 2021 foi:  {vendas}</h4>
    <h4>Total vendido no ano de 2021: R${faturamento:.2f}</h4>
    """

    msg = email.message.Message()
    msg['Subject'] = "Desafio VoceQPad analise de arquivo excel"
    msg['From'] = Segredos.Email
    msg['To'] = 'xxxxxxxxxxxxxxx'#retirada de email
    password = Segredos.Senha #Senha gerada pelo google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


