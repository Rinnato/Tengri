import telebot

# Токен бота, который можно получить через BotFather
TOKEN = ''

# Список товаров с их ценами
PRODUCTS = {
    'Товар 1': 100,
    'Товар 2': 200,
    'Товар 3': 300,
    'Товар 4': 400,
    'Товар 5': 500,
    'Товар 6': 600,
    'Товар 7': 700,
    'Товар 8': 800,
    'Товар 9': 900,
    'Товар 10': 1000
}

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот для продажи товаров. Доступные товары:\n\n' + '\n'.join([f'{name}: {price} тнг.' for name, price in PRODUCTS.items()]))

# Обработчик команды /buy
@bot.message_handler(commands=['buy'])
def process_buy_command(message):
    bot.reply_to(message, 'Введите название товара, который вы хотите купить:')

# Обработчик сообщения с названием товара
@bot.message_handler(func=lambda message: True)
def process_product_name(message):
    product_name = message.text
    if product_name in PRODUCTS:
        price = PRODUCTS[product_name]
        bot.reply_to(message, f'Цена товара "{product_name}" - {price} тнг. Для покупки введите команду /pay_{product_name.lower()}.')
    else:
        bot.reply_to(message, f'Извините, товар "{product_name}" не найден.')

# Обработчики команд оплаты для каждого товара
for product_name in PRODUCTS:
    @bot.message_handler(commands=[f'pay_{product_name.lower()}'])
    def process_pay_command(message):
        price = PRODUCTS[product_name]
        bot.reply_to(message, f'Оплатите {price} тнг. на счет 1234567890. После оплаты напишите мне сообщение об этом.')
    
# Запускаем бота
bot.polling()
