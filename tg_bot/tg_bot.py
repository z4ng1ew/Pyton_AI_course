import telebot
import random

bot = telebot.TeleBot("Токен")

animal_facts = [
    "Слоны умеют распознавать себя в зеркале.",
    "Осьминоги имеют три сердца.",
    "Коалы спят до 22 часов в сутки.",
    "Дельфины дают друг другу имена.",
    "Пингвины могут прыгать на высоту до 2 метров.",
    "Крокодилы не умеют высовывать язык.",
    "Жирафы могут чистить уши своим языком.",
    "Медведи могут бегать со скоростью до 60 км/ч.",
    "Совы не могут двигать глазами.",
    "Хамелеоны меняют цвет не только для маскировки, но и для общения."
]

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Привет! Я бот, который рассказывает интересные факты о животных. \nНапиши /facts, чтобы получить факты.")




@bot.message_handler(commands=["facts"])
def send_facts(m):
    facts = random.sample(animal_facts, 3)
    for fact in facts:
        bot.send_message(m.chat.id, f" {fact}")

bot.polling(none_stop=True, interval=0)