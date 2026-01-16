from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from assistant import Assistant

bot_brain = Assistant("ZeyBot")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.greet())

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.show_status())

async def charge_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.charge())

async def add_note_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = " ".join(context.args)
    if user_text:
        await update.message.reply_text(bot_brain.add_note(user_text))
    else:
        await update.message.reply_text("❌ Not yazmadın!")

# --- ÖDEV GÖREVİ ---
# GÖREV: 'clear_mem_cmd' adında bir async fonksiyon oluşturun.
# Bu fonksiyon bot_brain.clear_memory() metodunu çağırmalı ve gelen cevabı reply etmeli.
async def clear_mem_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # BURAYA KODUNUZU YAZIN
    pass

if __name__ == '__main__':
    TOKEN = "TOKEN_BURAYA"
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('durum', status))
    app.add_handler(CommandHandler('sarj', charge_bot))
    app.add_handler(CommandHandler('not_al', add_note_cmd))
    
    # GÖREV: 'hafizayi_temizle' komutunu Handler olarak aşağıya ekleyin.
    # ...
    
    print("Bot ödev testine hazır!")
    app.run_polling()