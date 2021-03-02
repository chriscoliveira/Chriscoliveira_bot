# -*- coding: utf-8 -*-
import telepot
import os
from classes import Funcoes
import procura

name = ''
mensagem = f'{"#" * 30}\nOlá {name}!\nuse os comandos:\n{"#" * 30}\n' \
           f'\n/noticias_tecmundo\n/noticias_tudocelular\n/noticias_olhar_digital\n/noticias_uol\n' \
           f'/noticias_techtudo\n/noticias_pesquisa\n\n/linux_edivaldobrito\n/linux_diolinux\n/buscape'


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

        if command == 'Hi':
            message = f'Hello {name}, how are you?'
            bot.sendMessage(chat_id, message)

        if "noticias_pesquisa" in command:

            if param == None:
                bot.sendMessage(chat_id, " " + 'É necessario passar um parametro de busca nos sites.')
            else:
                bot.sendMessage(chat_id, 'Buscando Noticias contendo: ' + str(param))
                # tecmundo
                procura.retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card',
                                         tag_titulo='.tec--card__title', tag_preco=None, tag_horario='.z-flex-1',
                                         research=param)
                inf = open("resultado.txt", 'r')
                bot.sendMessage(chat_id, " " + str(inf.read()))

                # tudocelular
                procura.retorna_materias(link='https://www.tudocelular.com/', tag_bloco='.newlist_normal',
                                         tag_titulo='.title_new', tag_preco=None, tag_horario='em', research=param)
                inf = open("resultado.txt", 'r')
                bot.sendMessage(chat_id, " " + str(inf.read()))

                # olhardigital
                procura.retorna_materias(link='https://olhardigital.com.br/', tag_bloco='article',
                                         tag_titulo='.title', tag_preco=None, tag_horario=None, research=param)
                inf = open("resultado.txt", 'r')
                bot.sendMessage(chat_id, " " + str(inf.read()))

                # uol
                procura.retorna_materias(link='https://noticias.uol.com.br/', tag_bloco='.thumbnails-item',
                                         tag_titulo='.thumb-title', tag_preco=None, tag_horario=None, research=param)
                inf = open("resultado.txt", 'r')
                bot.sendMessage(chat_id, " " + str(inf.read()))

                # uol
                procura.retorna_materias(link='https://www.techtudo.com.br/', tag_bloco='.feed-post',
                                         tag_titulo='.feed-post-body', tag_preco=None, tag_horario=None,
                                         research=param)
                inf = open("resultado.txt", 'r')
                bot.sendMessage(chat_id, " " + str(inf.read()))

        if "noticias_tecmundo" in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))

            # tecmundo
            procura.retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card',
                                     tag_titulo='.tec--card__title', tag_preco=None, tag_horario='.z-flex-1',
                                     research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if "noticias_tudocelular" in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            # tudocelular
            procura.retorna_materias(link='https://www.tudocelular.com/', tag_bloco='.newlist_normal',
                                     tag_titulo='.title_new', tag_preco=None, tag_horario='em', research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if "noticias_olhar_digital" in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            # olhardigital
            procura.retorna_materias(link='https://olhardigital.com.br/', tag_bloco='article',
                                     tag_titulo='.title', tag_preco=None, tag_horario=None, research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if "noticias_uol" in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            # uol
            procura.retorna_materias(link='https://noticias.uol.com.br/', tag_bloco='.thumbnails-item',
                                     tag_titulo='.thumb-title', tag_preco=None, tag_horario=None, research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if "noticias_techtudo" in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            # techtudo
            procura.retorna_materias(link='https://www.techtudo.com.br/', tag_bloco='.feed-post',
                                     tag_titulo='.feed-post-body', tag_preco=None, tag_horario=None, research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if 'linux_edivaldobrito' in command:
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            procura.retorna_materias(link='https://www.edivaldobrito.com.br/', tag_bloco='.ultp-block-item',
                                     tag_titulo='.ultp-block-title', tag_preco=None,  # tag_horario='.ultp-block-date',
                                     research=None)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))
        if 'linux_diolinux' in command:

            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            procura.retorna_materias(link='https://www.diolinux.com.br/', tag_bloco='.entry-preview',
                                     tag_titulo='.entry-title', tag_preco=None, tag_horario='.meta-date',
                                     research=None)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        if "buscape" in command:
            
            bot.sendMessage(chat_id, f'Buscando {command} com: ' + str(param))
            procura.retorna_materias(link='https://www.buscape.com.br/search?q=', tag_bloco='.cardBody',
                                     tag_titulo='.name', tag_preco='.customValue', research=param)
            inf = open("resultado.txt", 'r')
            bot.sendMessage(chat_id, " " + str(inf.read()))

        bot.sendMessage(chat_id, mensagem)

    except Exception as e:
        bot.sendMessage(chat_id, f'There was an error!!! {e}')


def sendMessage(chat, message):
    bot.sendMessage(chat, message)


# token_telegram = os.environ["TELEGRAM_TOKEN"]
token_telegram = '1605537242:AAHPejbQwYhe031m6XiGtL5cw4TFLFHmjVY' #token chriscoliveira_teste_bot
# token_telegram = '1680792124:AAEd98zadjQ0HEpZhZ97-d-rQdPk02Jjtz8' #token chriscoliveira_bot
bot = telepot.Bot(token_telegram)
bot.message_loop(handleCommad)

try:
    print(f'press CTRL + C to cancel\nBot Chris')

    while True:
        pass

except KeyboardInterrupt:
    print('\nBye')
