from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я ваш бот. Чем могу помочь?')

def main():
    # Вставь свой токен, который ты получил от BotFather
    token = "7960493937:AAFkQF9z10HyPxW9IV815-oGwqHP7MuVmZM"

    # Создаем объект Application для новой версии библиотеки
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
