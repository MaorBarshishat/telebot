# telebot
a telegram bot for an interview

Telegram bot using python that communicates with client and hash a jpg/jpeg by *md5 algorithm* file that the client sent. 
The bot will return an error message when the client send invalid message, such as: text, voice or another type of file (.mp3, .pdf, .docx ..). 
Two kinds of messages from the bot:  1. *ERROR* - when the client send invalid message, the bot will return an appropriate error message.
                                     2. *SUCCESS* - when the client send valid message (jpg/jpeg file), the bot will return a success message with the file hashed.
