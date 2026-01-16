from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# 1. GÖREV: asistan.py dosyasındaki Assistant sınıfını import edin
# from ... import ...

# 2. GÖREV: 'bot_brain' adında bir Assistant nesnesi oluşturun (Örn: "ZeyBot")
# bot_brain = ...

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 3. GÖREV: bot_brain içindeki greet() metodunu çağırın ve gelen cevabı gönderin
    # cevap = ...
    # await update.message.reply_text(cevap)
    pass

if __name__ == '__main__':
    # 4. GÖREV: Kendi Token'ınızı girin
    TOKEN = "BURAYA_TOKEN_GELECEK"
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    
    print("Bot beyniyle bağlandı. Telegram'dan /start yazın!")
    app.run_polling()