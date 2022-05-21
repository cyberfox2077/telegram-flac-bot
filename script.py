import telebot
# pip install pyTelegramBotAPI -U

API_TOKEN = "@BotFather token"
My_ID = "Your ID"
name_bot = "FLAC"

MP3_FORMATS = ["audio/" + fmt for fmt in ["mpeg", "aac"]]
LOSELESS_FORMATS = ["audio/" + fmt for fmt in ["x-wav", "wav", "wave", "ogg", "flac", "annodex", "x-flac"]]

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome Text")  # welcome text
    print(message.from_user.id)  # outputs ID to console


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # I hate /ping, so it replies you with your message :)
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    # Если удача:
    try:
        if message.audio.mime_type:
            if message.audio.mime_type in MP3_FORMATS:
                print("MP3 File")
                bot.reply_to(message, "File is MP3. Ignored.")
            if message.audio.mime_type in LOSELESS_FORMATS:
                print("Lossless")
                print(message.audio.duration)
                bot.forward_message(My_ID, message.chat.id, message.message_id)
                bot.reply_to(message, "Success!")
        else:
            bot.reply_to(message, "Error text!")
    except Exception as e:
        bot.reply_to(message, e)  # багрепорт


if __name__ == "__main__":
    bot.polling()
