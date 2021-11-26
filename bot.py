
import telebot
import re

TOKEN='2070933471:AAHdHQDGFZZHPZd3BLcQ-CwLPRFylTrgwiI'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Привет, если нужна помощь, приши help?")
@bot.message_handler(func=lambda m:True)
def answer_messages(message):
    message_text=message.text.lower()
    if re.search(r'[^.]*атак.+шахмат.',message_text, re.I):
        bot.reply_to(message,'С развитием шахматной мысли понятие атаки переосмысливалось. Вильгельм Стейниц рассматривал атаку как средство реализации достигнутого преимущества. Она должна была завершать другие наступательные действия — инициативу, позиционное давление, ограничение подвижности неприятельских фигур. Отсюда концепция Стейница: имеющий преимущество обязан атаковать. Тот же, кто защищается, не имеет такого права, так как его позиция ещё более ухудшится.\nhttps://chess-boom.online/taktika-i-strategiya-shahmat/')
    elif re.search(r'[^.]*защит.+шахмат.',message_text, re.I):
        bot.reply_to(message,'Защита в шахматах и шахматной композиции отражение наступающих действий соперника.\nhttps://chess-boom.online/sovremennaya-zashhita/')
    elif re.search(r'[^.]*гроб.',message_text, re.I):
        bot.reply_to(message,'АХАХХААХ https://chessmatenok.ru/ataka-groba-v-shahmatah/')
    elif re.search(r'[^.]*франц.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/frantsuzskaya-zashhita/')
    elif re.search(r'[^.]*сицил.',message_text, re.I):
        bot.reply_to(message,'https://chess-boom.online/sitsilianskaya-zashhita/')
    elif re.search(r'[^.]*сканд.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/skandinavskaya-zashhita/')
    elif re.search(r'[^.]*англ.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/anglijskoe-nachalo-v-shahmatah/')
    elif re.search(r'[^.]*лондон.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/londonskaya-sistema/')
    elif re.search(r'[^.]*каро.',message_text, re.I):
        bot.reply_to(message,'https://chess-boom.online/zashhita-karo-kann/')
    elif re.search(r'[^.]*нимцов.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/v-rabote-zashhita-nimtsovicha/')
    elif re.search(r'[^.]*итал.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/italyanskaya-partiya-v-shahmatah/')
    elif re.search(r'[^.]*испан.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/ispanskaya-partiya/')
    elif re.search(r'[^.]*шотл.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/shotlandskaya-partiya/')
    elif re.search(r'[^.]*ферзь.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/prinyatyj-ferzevyj-gambit/')
    elif re.search(r'[^.]*староинд.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/staroindijskaya-zashhita/')
    elif re.search(r'[^.]*волж.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/volzhskij-gambit/')
    elif re.search(r'[^.]*славян.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/slavyanskaya-zashhita/')
    elif re.search(r'[^.]*русск.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/russkaya-partiya-v-shahmatah/')
    elif re.search(r'[^.]*Эванс.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/gambit-evansa/')
    elif re.search(r'[^.]*Голланд.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/gollandskaya-zashhita/')
    elif re.search(r'[^.]*Каталонск.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/katalonskoe-nachalo/')
    elif re.search(r'[^.]*королевский.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/korolevskij-gambit-v-shahmatah/')
    elif re.search(r'[^.]*берлинская.',message_text, re.I):
        bot.reply_to(message,'https://chessmatenok.ru/berlinskaya-zashhita-v-shahmatah/')

    elif message_text=='help':
        bot.reply_to(message, 'Вот, чем я могу помочь:\n1)Атака в шахматах;\n2)Защита в шахматах;\n3)Метод Гроба;\n4)Французская защита;\n5)Сицилианская защита;\n6)Скандинавская защита;\n7)Английское начало;\n8)Лондонское начало;\n9)Защита Каро-Канн;\n10)Дебют Нимцовича;\n11)Итальянская партия;\n12)Испанская партия;\n13)Шотландская партия;\n14)Ферзевый гамбит;\n15) Староиндийская защита;\n16)Волжский гамбит;\n17)Славянская защита;\n18)Русская партия;\n19)Гамбит Эванса;\n20)Голландская защита;\n21)Каталонское начало ;\n22)Королевский гамбит;\n23)Берлинская защита')
    else :
        bot.reply_to(message,'Я вас не понял.')

bot.polling()


#aiogramm()!
