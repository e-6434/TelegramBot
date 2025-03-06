import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "-"
CHANNEL_ID = -1002374360862  # آیدی عددی کانال

bot = telebot.TeleBot(TOKEN)

# مطمئن شو که message_id درست وارد شده باشه!
movies = {
    " فیلم تستی🎬":3,
    " عکس  تستی  ":2,
    " متن  تستی  ":5 
}

@bot.message_handler(commands=['start'])
def send_movie_list(message):
    markup = InlineKeyboardMarkup()
    for movie_name in movies.keys():
        markup.add(InlineKeyboardButton(movie_name, callback_data=movie_name))
    
    bot.send_message(message.chat.id, "🎬 لطفاً یک فیلم را انتخاب کنید:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in movies)
def forward_movie(call):
    movie_message_id = movies[call.data]
    try:
        bot.forward_message(call.message.chat.id, CHANNEL_ID, movie_message_id)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ خطایی رخ داد: {e}")

bot.polling()
