import ephem, datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("958204140:AAHA21y19NDgyyzTYNJH4WsqQ9mfvY1X-3c", request_kwargs=PROXY)
    dp = mybot.dispatcher

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()



def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    if user_text == 'Mercury':
        mercury = ephem.Mercury(datetime.date.today())
        constellation = ephem.constellation(mercury)
        update.message.reply_text(f'Меркурий находится в созвездии {constellation}')
    elif user_text == 'Venus':
        venus = ephem.Venus(datetime.date.today())
        constellation = ephem.constellation(venus)
        update.message.reply_text(f'Венера находится в созвездии {constellation}')
    elif user_text == 'Mars':
        mars = ephem.Mars(datetime.date.today())
        constellation = ephem.constellation(mars)
        update.message.reply_text(f'Марс находится в созвездии {constellation}')
    elif user_text == 'Jupiter':
        jupiter = ephem.Jupiter(datetime.date.today())
        constellation = ephem.constellation(jupiter)
        update.message.reply_text(f'Юпитер находится в созвездии {constellation}')
    elif user_text == 'Saturn':
        saturn = ephem.Saturn(datetime.date.today())
        constellation = ephem.constellation(saturn)
        update.message.reply_text(f'Сатурн находится в созвездии {constellation}')
    elif user_text == 'Uranus':
        uranus = ephem.Uranus(datetime.date.today())
        constellation = ephem.constellation(uranus)
        update.message.reply_text(f'Уран находится в созвездии {constellation}')
    elif user_text == 'Neptune':
        neptune = ephem.Neptune(datetime.date.today())
        constellation = ephem.constellation(neptune)
        update.message.reply_text(f'Нептун находится в созвездии {constellation}')   
    elif user_text=='Pluto':
        update.message.reply_text('Плутон уже не планета')
    elif user_text == 'Earth':
        update.message.reply_text('Мы находимся на Земле')        
    else:
        update.message.reply_text('Введите название планеты')
    

main()