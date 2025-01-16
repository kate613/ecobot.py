import telebot 
import os
import random
import requests
    
bot = telebot.TeleBot("7545352283:AAFcn0BguQeqlbkM-T_A8GyVAnJxtYo7gFg")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['mem'])
def mem(message):
    '''Отправляет случайный мем из папки images'''
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Проблемы экологии на нашей планете, такие как изменение климата, загрязнение воздуха и воды, вырубка лесов и исчезновение видов, угрожают жизни людей и природы. Основной причиной является человеческая деятельность: промышленное производство, нерациональное использование ресурсов и массовое потребление. Исправить ситуацию можно, начав с простых действий: сокращение отходов, переход на возобновляемые источники энергии, восстановление лесов и бережное отношение к природе. Также важно усиливать экологическое образование и разрабатывать законы, защищающие окружающую среду. Вместе, объединив усилия, мы можем сохранить нашу планету для будущих поколений.")

@bot.message_handler(commands=['plnet3'])
def get_duck_image_url(message):
    url = 'https://www.youtube.com/watch?v=TuLosPeHPSo'
    bot.send_message(message.chat.id, f"Check out this: {url}")

@bot.message_handler(commands=['plnet1'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['planet'])
def planet(message):
    '''Отправляет случайный мем из папки images'''
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['planet'])
def send_planet(message):
    with open('images/Unknown.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
bot.polling()
