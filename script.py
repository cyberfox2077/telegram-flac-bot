
import telebot
# pip install pyTelegramBotAPI -U
API_TOKEN="@BotFather token"
My_ID="Your ID"
name_bot="FLAC"
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Welcome Text") # welcome text
    print(message.from_user.id) #outputs ID to console

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text) # I hate /ping, so it replies you with your message :)

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    # Если удача:
    try:
        if message.audio.mime_type:
            if message.audio.mime_type=="audio/mpeg" or message.audio.mime_type=="audio/aac":
                print("MP3 File")
                bot.reply_to(message, "File is MP3. Ignored.")
            if message.audio.mime_type=="audio/x-wav" or message.audio.mime_type=="audio/wav" or message.audio.mime_type=="audio/wave" or message.audio.mime_type=="audio/ogg" or message.audio.mime_type=="audio/flac" or message.audio.mime_type=="audio/annodex"or message.audio.mime_type=="audio/x-flac":
                print("Lossless")
                print(message.audio.duration)
                bot.forward_message(My_ID, message.chat.id, message.message_id)
                bot.reply_to(message, "Success!")
            
        else:
            bot.reply_to(message, "Error text!")
    except Exception as e:
        bot.reply_to(message, e) # багрепорт
bot.polling()
