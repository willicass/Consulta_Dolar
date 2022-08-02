import smtplib
import email.message
from credenciais import login, senha, mail, caminho
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep


def enviar_email():
    # Criar um e-mail
    corpo_email = f"Referente ao dia {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    msg = email.message.Message()
    msg['Subject'] = f'Cotação do Dolar {ValorDollar[0][0:6]}'
    msg['From'] = login
    msg['To'] = mail
    password = senha
    msg.add_header('Cibtebt-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credential for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email enviado')


ValorDollar = list()

chrome_options = ChromeOptions()
driver = webdriver.Chrome(caminho, 
    options=chrome_options)
sleep(1)
driver.get('https://economia.uol.com.br/cotacoes/cambio')
sleep(1)
print('Carregando informacoes do Site')
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located ((By.XPATH, '/html/body/div[8]/div/div[2]/button')))
sleep(1)
driver.find_element(by=By.XPATH, 
value='/html/body/div[8]/div/div[2]/button').click()
sleep(1)
print(f'Alocando informacoes')
ValorDollar.append(driver.find_element(by=By.XPATH, 
value='/html/body/div[6]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/span[2]').text)
driver.close()
enviar_email()
