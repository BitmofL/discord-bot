#requirements.txt туда все библиотеки при хостинге eval pip install -r requirements.txt
#  Данный код является расширенной версией предыдущего кода.

#  Импортируются необходимые модули
import os

# Debug: ensure dependencies are installed in hosting venv
import importlib
import disnake
from disnake.ext import commands


#  Создается объект intents, который включает все разрешения для бота.
#  Создается экземпляр класса Bot с префиксом команд "!" и указанными разрешениями.
intents = disnake.Intents.all()  # Подключаем все разрешения
bot = commands.Bot(command_prefix=">", intents=intents, test_guilds=[793901633703903284])  # Вместо 1234567890 указать id сервера


# Определяется функция on_ready, которая будет вызываться, когда бот будет готов к использованию.
# В данном случае, она просто выводит сообщение "Bot is ready!" в консоль.
@bot.event
async def on_ready():
    print("Bot is ready!")


# При готовности бота, загружает расширения из папки "cogs"
try:
    for file in os.listdir(".venv/cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
except Exception as e:
    for file in os.listdir(".venv\cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")




# Запускается бот с помощью метода run, передавая ему токен для авторизации.
bot.run(os.getenv("DISCORD_TOKEN"))


#Опции verify, gender,games
