# -*- coding: utf-8 -*-
import telepot
import os
from classes import Funcoes
from procura import *

name = ''
mensagem = f'\n{"#" * 30}\nOlá {name}!\nuse os comandos:\n{"#" * 30}\n' \
           f'\n/noticias_tecmundo\n/noticias_tudocelular\n/noticias_olhar_digital\n/noticias_uol\n' \
           f'/noticias_techtudo\n/noticias_pesquisa\n\n/linux_edivaldobrito\n/linux_diolinux\n/buscape\n'


def handleCommad(content):
    try:
        chat_id = content['chat']['id']
        name = content['chat']['first_name']
        try:
            command, *param = content['text'].split()
        except:
            command = content['text']
            param = None
        final = ' '
        param = final.join(param)

        bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
        if "noticias_tecmundo" in command:
            result = retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card',
                                      tag_titulo='.tec--card__title', tag_preco=None, tag_horario='.z-flex-1',
                                      research=param)
        elif "noticias_tudocelular" in command:
            result = retorna_materias(link='https://www.tudocelular.com/', tag_bloco='.newlist_normal',
                                      tag_titulo='.title_new', tag_preco=None, tag_horario='em', research=param)
        elif "noticias_olhar_digital" in command:
            result = retorna_materias(link='https://olhardigital.com.br/', tag_bloco='article',
                                      tag_titulo='.title', tag_preco=None, tag_horario=None, research=param)
        elif "noticias_uol" in command:
            result = retorna_materias(link='https://noticias.uol.com.br/', tag_bloco='.thumbnails-item',
                                      tag_titulo='.thumb-title', tag_preco=None, tag_horario=None, research=param)
        elif "noticias_techtudo" in command:
            result = retorna_materias(link='https://www.techtudo.com.br/', tag_bloco='.feed-post',
                                      tag_titulo='.feed-post-body', tag_preco=None, tag_horario=None, research=param)
        elif 'linux_edivaldobrito' in command:
            result = retorna_materias(link='https://www.edivaldobrito.com.br/', tag_bloco='.ultp-block-item',
                                      tag_titulo='.ultp-block-title', tag_preco=None,  # tag_horario='.ultp-block-date',
                                      research=None)
        elif 'linux_diolinux' in command:
            result = retorna_materias(link='https://www.diolinux.com.br/', tag_bloco='.entry-preview',
                                      tag_titulo='.entry-title', tag_preco=None, tag_horario='.meta-date',
                                      research=None)
        elif "buscape" in command:
            result = retorna_materias(link='https://www.buscape.com.br/search?q=', tag_bloco='.cardBody',
                                      tag_titulo='.name', tag_preco='.customValue', research=param)
        else:
            bot.sendMessage(chat_id, "Opção inválida!")
            result = False

        if result:
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        bot.sendMessage(chat_id, mensagem)

    except Exception as e:
        bot.sendMessage(chat_id, f'ohPorra!!! {e}')


def sendMessage(chat, message):
    bot.sendMessage(chat, message)


# token_telegram = os.environ["TELEGRAM_TOKEN"]
token_telegram = '1605537242:AAHPejbQwYhe031m6XiGtL5cw4TFLFHmjVY'  # token chriscoliveira_teste_bot
# token_telegram = '1680792124:AAEd98zadjQ0HEpZhZ97-d-rQdPk02Jjtz8' #token chriscoliveira_bot
bot = telepot.Bot(token_telegram)
bot.message_loop(handleCommad)

try:
    print(f'press CTRL + C to cancel\nBot Chris')

    while True:
        pass

except KeyboardInterrupt:
    print('\nBye')
