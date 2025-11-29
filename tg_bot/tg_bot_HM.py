import telebot

token = "ТОКЕН"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])


def start(message):
    bot.send_message(message.chat.id, "Привет! Меня зовут бот")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # ПРАВИЛЬНЫЙ СПОСОБ: объединяем текст в одну строку
    response = f"Привет! {message.text} Добро пожаловать!"
    bot.send_message(message.chat.id, response)


# Альтернативные варианты:
@bot.message_handler(content_types=['text'])
def get_text_messages_alternative(message):
    # Вариант 1: Конкатенация строк
    bot.send_message(message.chat.id, "Привет! " + message.text + " Добро пожаловать!")

    # Вариант 2: Форматирование с .format()
    # bot.send_message(message.chat.id, "Привет! {} Добро пожаловать!".format(message.text))


try:
    print("Бот запускается...")
    bot.polling(none_stop=True, interval=2, timeout=60)
except Exception as e:
    print(f"Ошибка: {e}")