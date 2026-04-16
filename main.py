from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

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

#Guarda conteudo html da pagina alvo
html_target = navegador.page_source

#Faz o driver esperar por x segundos(navegador, x)
wait = WebDriverWait(navegador, 10)





#NOTA: O código abaixo é um exemplo de como NÃO se deve fazer, pois ele tenta localizar os elementos antes mesmo de eles estarem presentes na página, o que pode levar a erros de "element not found".
#ERRADO > filmes_find_element = wait.until(EC.presence_of_all_elements_located(navegador.find_elements((By.XPATH, "//li[.//h3[contains(@class, 'ipc-title__text')]]"))))
#ERRADO > filmes_find_element_no_wait = navegador.find_elements(By.XPATH, "//li[.//h3[contains(@class, 'ipc-title__text')]]")




#### Definição da função para fechar o pop-up de informações ####
#### Tenta utilizar a tag aria-label, caso falhe, tenta clicar na área fora do pop-up (overlay) para fechá-lo. ####

def close_promptable():
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ipc-promptable-base__content')]")))
        print("Pop-up de informações aberto com sucesso.") 
    except TimeoutException:
        print("Erro: não foi possível abrir o pop-up de informações.")

    #DEPRECATED > Estrategia 1: botão com data-testid específico
    #Não vai funcionar pois a tag @data-testid não pertence ao botão de fechar, mas sim à div pai do pop-up(duhh).
    '''
    try:
        # Estrategia 1: botão com data-testid específico
        close_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//button[@data-testid='title-summary-prompt-close-button']")
            )
        )
        close_button.click()
        print("Botão fechado com data-testid.")
        return
    except TimeoutException:
        pass  # Continua para a próxima tentativa
    '''
    try:
        #Botão com tag aria-label="Fechar" ou "Close"
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Fechar prompt' or @aria-label='Close prompt']"))
        )
        close_btn.click()
        print("Popup fechado com aria-label.")
        return
    except TimeoutException:
        pass  # Continua para a próxima tentativa
    
    try:
        # Estratégia 4: clicar no fundo escuro (overlay) para fechar
        overlay = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='presentation' and contains(@class, 'ipc-promptable-base__backdrop')]")))
        overlay.click()
        print("Popup fechado clicando no overlay.")
    except TimeoutException:
        print("Erro: não foi possível fechar o pop-up.")




##### Iniciando o processo de scrapping #####

movie_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//div[@data-testid="chart-layout-main-column"]//li[contains(@class,"ipc-metadata-list-summary-item")]')
    )
)
print(f"Total de filmes encontrados: {len(movie_list)}")

for idx, movie in enumerate(movie_list):

    #Centraliza o filme na tela para garantir que o botão de informações esteja visível
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", movie)

    #Localiza o botão de informações usando um XPath relativo ao elemento do filme
    info_button = movie.find_element(By.XPATH, './/button[@data-testid="title-summary-prompt-button-info-icon"]')
    print(f"\nFilme atual: {movie.find_element(By.XPATH, './/h3[contains(@class, "ipc-title__text")]').text}")
    info_button.click()
    #
    #tratamento das funcoes
    #

    close_promptable()

print(f"Filmes na movie_list: {len(movie_list)}")


'''
#Utiliza o beautifulsoup para pegar as informações
site = BeautifulSoup(html_target, 'html.parser')

print(site.prettify()) 
'''