from flask import Flask, request
import telebot

TOKEN = "-"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/payment_success', methods=['POST'])
def payment_success():
    data = request.json
    user_id = data.get('user_id')
    
    if user_id:
        bot.send_message(user_id, "پرداخت شما تأیید شد! در اینجا فیلم شما:")
        bot.send_document(user_id, open("movie.mp4", "rb"))  # فیلمی که می‌خواهی بفرستی
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
