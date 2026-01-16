from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from assistant import Assistant

bot_brain = Assistant("ZeyBot")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.greet())

# 1. GÖREV: 'status' fonksiyonunu yazın (/durum komutu için)
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # bot_brain.show_status() çağırıp mesaj gönderin
    pass

# 2. GÖREV: 'charge' fonksiyonunu yazın (/sarj komutu için)
async def charge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # bot_brain.charge() çağırıp mesaj gönderin
    pass

# 3. GÖREV: 'add_note' fonksiyonunu yazın (/not_al komutu için)
async def add_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kullanıcının yazdığı metni alalım
    user_text = " ".join(context.args) 
    # Eğer metin boş değilse bot_brain.add_note(user_text) çağırın
    pass

if __name__ == '__main__':
    app = ApplicationBuilder().token("TOKEN").build()
    
    app.add_handler(CommandHandler('start', start))
    # 4. GÖREV: Yeni komutları buraya kaydedin
    # app.add_handler(CommandHandler('durum', status))
    # ...
    
    app.run_polling()