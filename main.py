#import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#URL alvo para scrapping
url_target = 'https://www.imdb.com/pt/chart/top/?ref_=hm_nv_menu'

#Objeto options para funções extras
obj_options = Options()
obj_options.add_argument('window-size=1280,720')

#Define o navegador para abrir com o Firefox
#navegador = webdriver.Firefox(options = obj_options)
navegador = webdriver.Firefox()

#Carrega o navegador utilizando o selenium
navegador.get(url_target)

#Espera a pagina ser criada do lado do cliente para pegarmos o código html
sleep(1)

#Guarda conteudo html da pagina alvo
html_target = navegador.page_source

#Faz o driver esperar por 1 segundo
wait = WebDriverWait(navegador, 1)


#XPATH da div em que os box de cada filme estao agrupados:
#/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul


#XPATH da primeira div do primeiro box:
#/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]


#XPATH do numero de posicao do primeiro filme:
#/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/div[1]/div
#conteudo: <div class="ipc-signpost__text" role="presentation">#1</div>


#XPATH do titulo do primeiro filme:
#//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/ul/div/a
#absoluto:/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/ul/div/a
#contudo: <a href="/pt/title/tt0111161/?ref_=chttp_t_1" class="ipc-title-link-wrapper" tabindex="0"><h3 class="ipc-title__text">Um Sonho de Liberdade</h3></a>
#clicando no titulo do filme para acessar sua pagina
sleep(1)
#button_info = navegador.find_element(By.XPATH, "//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/ul/div/a")
button_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/ul/div/a')))
button_info.click()


#XPATH do botao de mais informações sobre o filme:
#/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[3]/button
#conteudo: <button data-testid="title-summary-prompt-button-info-icon" class="ipc-icon-button li-info-icon ipc-icon-button--base ipc-icon-button--onAccent2" title="Veja mais informações sobre Um Sonho de Liberdade" tabindex="0" aria-label="Veja mais informações sobre Um Sonho de Liberdade" aria-disabled="false"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--info" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M11 7h2v2h-2zm0 4h2v6h-2zm1-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg></button>
#clicando no botao de button_info
#sleep(1)
#button_info = navegador.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[3]/button")
#button_info.click()
'''
#Utiliza o beautifulsoup para pegar as informações
site = BeautifulSoup(html_target, 'html.parser')

print(site.prettify()) 
'''