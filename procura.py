import requests
from bs4 import BeautifulSoup
import urllib.request
import re


def search(link):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # print(soup)
    return soup


def tiny_url(url):
    api_url = 'https://tinyurl.com/api-create.php?url='
    tinyurl = urllib.request.urlopen(api_url + url).read()
    return tinyurl.decode('utf-8')


def retorna_materias(link, tag_bloco, tag_titulo, tag_preco=None, tag_link=None, tag_horario=None, research=None):
    if tag_preco == None:
        pagina = requests.get(link)
    else:
        pagina = requests.get(link + research)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    arquivo = open('resultado.txt', 'w')
    site = link.replace("www.", "").replace(".br", "").replace("/", "").replace('//', '')
    site = re.search(r'https:(.*?).com', site).group(1).upper()
    arquivo.write(
        f'\nNotícias de {site}\n')
    contador = 0
    for materia in soup.select(tag_bloco):
        try:
            texto = materia.select_one(tag_titulo).text
            link = materia.select_one('a').get('href')
            if tag_preco:
                preco = materia.select_one(tag_preco).text

            # verifica se existe a tag de horario da materia
            if tag_horario:
                horario = materia.select_one(tag_horario)
                horario = horario.text.replace("há", "")
            else:
                horario = ''
        except Exception as e:
            texto = ''

        # verifica se a pesquisa é especifica
        if tag_preco:
            contador += 1
            # print(texto, preco, link, sep=' -_- ')
            arquivo.write(f'{preco} - {texto[0:60]}... {tiny_url("https://www.buscape.com.br" + link)}\n\n')
        elif research:
            if research.upper() in texto.upper():
                # arquivo.write(f'{horario} - {texto.strip()} \n\n')
                arquivo.write(f'{horario} - {texto.strip()}{texto[0:60].strip()}...  {tiny_url(link)}\n\n')
                contador += 1

        # exibe a pesquisa total
        else:
            # arquivo.write(f'{horario} - {texto.strip()} {tiny_url(link)}\n\n')
            if not horario == None:
                arquivo.write(f'{horario} - {texto.strip()} {tiny_url(link)}\n\n')
                contador += 1

    arquivo.write(f'\nEncontrado {contador} materias no site {site}')
    arquivo.close()
    return True


if __name__ == '__main__':
    # tecmundo
    valor = None
    # retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card--medium',
    #                  tag_titulo='.tec--card__title__link', tag_horario='.z-flex-1', research=valor)

    # retorna_materias(link='https://www.edivaldobrito.com.br/', tag_bloco='.ultp-block-item',
    #                  tag_titulo='.ultp-block-title', tag_preco=None, tag_horario='.ultp-block-date',research=None)
    retorna_materias(link='https://www.diolinux.com.br/', tag_bloco='.entry-preview',
                     tag_titulo='.entry-title', tag_preco=None, tag_horario='.meta-date', research=None)