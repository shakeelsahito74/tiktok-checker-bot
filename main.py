import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Aapka Token
TOKEN = '8305746811:AAHVYOD4a48cGJ78PnP1LjsCkoO7zuSzIO4'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Assalam-o-Alaikum Shakeel Bhai! Aapka TikTok Checker Bot tayyar hai.\n\nKisi bhi account ko check karne ke liye likhen:\n/check [username]")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a username. Example: /check shakeel")
        return
    username = context.args[0]
    await update.message.reply_text(f"🔍 Checking TikTok Account: @{username}...\n\nStatus: Feature is being connected!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('check', check))
    application.run_polling()
