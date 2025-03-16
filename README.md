<h1 align="center" style="color: red;"><b>InfoSnatch</b></h1>


██ ███    ██ ███████  ██████  ███████ ███    ██  █████  ████████  ██████ ██   ██ 
██ ████   ██ ██      ██    ██ ██      ████   ██ ██   ██    ██    ██      ██   ██ 
██ ██ ██  ██ █████   ██    ██ ███████ ██ ██  ██ ███████    ██    ██      ███████ 
██ ██  ██ ██ ██      ██    ██      ██ ██  ██ ██ ██   ██    ██    ██      ██   ██ 
██ ██   ████ ██       ██████  ███████ ██   ████ ██   ██    ██     ██████ ██   ██ 
                                                                                 
                                                                                 



# InfoSnatch

InfoSnatch is a powerful tool designed to gather real-time information about users, including their IP address, live location, device details, and even capture an image from their camera (with permission).

## Features
- ✅ **IP Address Tracking** - Retrieves the public IP of the user.
- ✅ **Live Geolocation** - Fetches approximate location using IP-based geolocation.
- ✅ **Device Information** - Captures browser and OS details.
- ✅ **Camera Access** - Captures an image from the user's webcam.

## Installation
```bash
git clone https://github.com/yourusername/InfoSnatch.git
cd InfoSnatch
pip install -r requirements.txt
```

## Create a .env file and add your Telegram Bot Token and Chat ID
```bash
TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

## Run the application
```bash
python app.py
```

## 📌 Usage
- ✅ Deploy the Flask server.
- ✅ Send the HTML link to the target.
- ✅ When they open the page, their IP, location, user info, and camera capture will be sent to Telegram.

## ⚠️ Disclaimer
This project is intended for educational and ethical hacking purposes only. The author does not take responsibility for any misuse. Always get consent before collecting any data.
