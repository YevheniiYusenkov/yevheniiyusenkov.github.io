from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8561724432:AAGfizNMzJ-g9VIpuABXeOUakj8IMtY0IRw"
WEBAPP_URL = "https://yevheniiyusenkov.github.io/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = ReplyKeyboardMarkup(
        [[KeyboardButton("🚀 Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )
    await update.message.reply_text("Нажми кнопку для запуска приложения:", reply_markup=kb)

# сюда прилетит tg.sendData(...) из мини-аппа
async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"Получил из приложения: {data}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data))
    app.run_polling()

if __name__ == "__main__":
    main()
