# TeleBot

This Telegram bot was developed as part of a technical assessment for an interview. It is built in Python and designed to communicate with clients, hashing a `.jpg` or `.jpeg` file sent by the client using the **MD5 algorithm**.

### Bot Features:
- **File Hashing:** When the client sends a valid `.jpg` or `.jpeg` file, the bot calculates its hash using the MD5 algorithm and returns a success message.
- **Error Handling:** If the client sends an invalid message (such as text, voice, or unsupported file types like `.mp3`, `.pdf`, `.docx`), the bot responds with an appropriate error message.

### Message Types:
1. **ERROR:** When an invalid message is sent, the bot responds with a specific error message.
2. **SUCCESS:** When a valid `.jpg` or `.jpeg` file is sent, the bot returns a success message along with the file's MD5 hash.

### as a docker:
```
sudo docker run -d maorbarshishat/telebot_maor:2.0
```

### as a python command:
 ```
    git clone https://github.com/MaorBarshishat/telebot.git
    cd telebot/
    pip install -r requirements.txt
    python3 main.py
```
