from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class BOT:
    def __init__(self, link):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.link = link
        return print('Conexão bem sucedida')
        

    def IniciarSistema(self):
        self.navegador.get(self.link)
        sleep(5)

        try:
            bot = self.navegador.find_element(By.XPATH, '//*[@id="start"]')
            bot.click()
        except Exception as e:
            print(f'Erro na instancia: {e}')




    def ClicarBotao(self):
        try:
            bot = self.navegador.find_element(By.XPATH, '//*[@id="clickarena"]')
            bot.click()
        except Exception as e:
            print(f'Erro na instancia: {e}')

    def EncerrarSistema(self):
        try:
            self.navegador.quit()
            print("Sistema encerrado.")
        except Exception as e:
            print(f'Erro ao encerrar o sistema: {e}')

    
if __name__ == '__main__':
    p1 = BOT("https://www.arealme.com/click-speed-test/pt/")
    p1.IniciarSistema()
    try:
        while True:
            p1.ClicarBotao()
    except KeyboardInterrupt:  # Permite encerrar com Ctrl+C
        print("Interrupção detectada. Encerrando o sistema...")
        p1.EncerrarSistema()