from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Palmeiras não tem mundial"
        self.grupos_ou_pessoas = ["Lembretes", "Promessas Acabadas"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for grupo in self.grupos_ou_pessoas:
            # Seleciona o grupo
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            # Seleciona o campo para enviar mensagem
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            # Seleciona o botão enviar
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
