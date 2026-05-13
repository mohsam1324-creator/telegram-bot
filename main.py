from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8991838215:AAHIIUQaDMus20JSqksCedUaiCldOvxOONk"

GROUP_ID = -5140884340
CHANNEL_ID = -1003725592982

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا بيك 👋\nارسل سؤالك وسيتم ارساله بشكل مجهول")

async def handle_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg and msg.text:
        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=f"المجهول يگول:\n\n{msg.text}"
        )

        await context.bot.send_message(
            chat_id=msg.chat_id,
            text="انتظر من نفرغ نرد عليك"
        )

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg and msg.reply_to_message and msg.text:
        original = msg.reply_to_message.text
        reply = msg.text

        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"المجهول يكول:\n{original}\n\nالجواب:\n{reply}"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user))
app.add_handler(MessageHandler(filters.TEXT, handle_reply))

print("Bot is running...")
app.run_polling()