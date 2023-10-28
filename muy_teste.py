from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython import embed
import pickle
import pyfiglet

flet = pyfiglet.Figlet(font='starwars')
print(flet.renderText("Selenium Bag of Words"))
print('v0.1')

# keyword_list = [
#         'matematica', 'matematica basica', 'matematica avancada',
#         'fisica',
#         'quimica',
#         'hidrostatica' 'hidrodinamica',
#     ]

keyword_list = [
    # 'doencas degenerativas',
    # 'artrite reumatoide',
    # 'business intelligence',
    'fumec',
    'ibmec',
]

def generate_url_list(kw_list):
    url_list=[]
    for kw in kw_list:
        url_list.append('http://google.com/search?q='+str(kw))
    return url_list


def fetch_first_page_results_body_text(url_list):
    sites = []
    firefox = webdriver.Firefox()
    for url in url_list:
        print('Now try: '+str(url))
        firefox.get(url)
        ## copied xpath for search input element

        # 1. acima - escolher uma forma de pegar os resultados da busca
        # 2. guardar textos e links de cada resultado para visita posterior
        # 3. iterar visitando e salvando todo o texto de todos os elementos de
        #   cada pagina dos resultados (por enquanto da primeira pagina)

        elems = firefox.find_elements(By.TAG_NAME,"a")
        lista_de_sites_primeira_pagina = []
        for elem in elems:
            link = elem.get_attribute("href")
            # print(link)
            try:
                if 'google' not in link:
                    lista_de_sites_primeira_pagina.append(link)
            except TypeError:
                print(f"Had a TypeError with {link}")

        print()
        print('We now have: '+str(len(lista_de_sites_primeira_pagina))+' link(s)')
        print()
        textos = []
        for s in lista_de_sites_primeira_pagina:
            firefox.get(s)
            texto = firefox.find_element(by=By.XPATH,value="/html/body").text
            # print(texto)
            textos.append(texto)
        sites.append(textos)

    firefox.close()
    return sites
## fe-show!

meus_sites = fetch_first_page_results_body_text(generate_url_list(keyword_list))

for s in meus_sites:
    print("#")
    print("# Site: ?")
    print("#")
    # print(s)

arquivo = open(input("Type in your filename for saving scraped data: "),'wb')
pickle.dump(meus_sites,arquivo)
arquivo.close()

embed()