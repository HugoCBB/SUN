from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class ZapBot:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.servico)


    def AcessarSite(self, link):
        self.driver.get(link)
        print("Aguardando QRCode")
        sleep(60)

    def EnviarMensagem(self, numero, mensagens):
        try:
            # Procurar contato
            url = f"https://web.whatsapp.com/send?phone={numero}"
            self.driver.get(url)
            sleep(5)

            # Mensagem
            mensagem = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
            mensagem.click()
            mensagem.send_keys(mensagens)
            mensagem.send_keys(Keys.RETURN)
            sleep(2)

        except KeyboardInterrupt:
            print("Sistema encerrado")


nome = "Hugo"
p1 = ZapBot()
p1.AcessarSite('https://web.whatsapp.com')
p1.EnviarMensagem('number', f'Ola {nome}, eu sou a SUN')
