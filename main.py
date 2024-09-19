import os  # importing os module for environment variables
from dotenv import load_dotenv
import telebot  # importing necessary functions which offer many ways to listen for incoming messages
import hashlib

SUPPORTED_DOCUMENT_TYPES = ('.jpg', '.jpeg')  # the supported files that the bot hash their path
WELCOME_COMMANDS = ['start', 'hello', 'restart']

HASH_ALGORITHM = "md5"

BAD_MSG_TYPE = "ERROR"
CORRECT_MSG_TYPE = "SUCCESS"

DEFAULT_CHUNK_SIZE = 24

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=WELCOME_COMMANDS)
def send_welcome(message):
    """
    hello message
    """
    text = f"Hi, it's your bot,\nIf you want me to calculate the hash of your image ({' or '.join(SUPPORTED_DOCUMENT_TYPES)} only), send your path please :)\n*for restart write /restart*"
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def send_help(message):
    """
    help message
    """
    text = f"The bot calculate hash of given photo by *{HASH_ALGORITHM} algorithm* which is one of the following extensions: {', '.join(SUPPORTED_DOCUMENT_TYPES)}.\nThe bot support these to files.\nAt any point you can write of the next commands in order to return to the initial message:\n/start /hello /restart."
    bot.reply_to(message, text)


@bot.message_handler(content_types=['photo'])
def handle_file_msg(message):
    """
    the function receive photo to hash, and starting the process
    :param message: client's photo to hash
    """
    try:
        # get file info
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_extension = os.path.splitext(file_info.file_path)[1].lower()

        if file_extension not in SUPPORTED_DOCUMENT_TYPES:
            raise ValueError(
                f"Such photo is not supported. Only {', '.join(SUPPORTED_DOCUMENT_TYPES)} files are allowed.")

        # Download the file
        file_data = bot.download_file(file_info.file_path)

        # hash the file and return to the client
        file_hashed = compute_file_hash(file_data, HASH_ALGORITHM, DEFAULT_CHUNK_SIZE)
        text = f"{CORRECT_MSG_TYPE}: your file hashed by {HASH_ALGORITHM} algorithm: {file_hashed}"
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    except ValueError as e:
        bot.reply_to(message, f"{BAD_MSG_TYPE}: {e}")
    except Exception as e:
        bot.reply_to(message, f"{BAD_MSG_TYPE}: {e}")


def compute_file_hash(file_buff, algorithm, chunk_size):
    """
    Compute the hash of a file by split to chunk.
    :param chunk_size: num of bytes to read each time
    :param file_buff: buffer of the file
    :param algorithm: hash algorithm
    :return: hashed file
    """
    hash_func = hashlib.new(algorithm)
    start = 0
    while start < len(file_buff):
        chunk = file_buff[start:start + chunk_size]
        hash_func.update(chunk)
        start += chunk_size
    return hash_func.hexdigest()


@bot.message_handler(content_types=['text', 'document', 'audio', 'video', 'voice', 'sticker', 'location', 'contact'])
def handle_wrong_input(message):
    """
    default function for any not supported client's message
    :param message: may be type of: text, document, audio, video, voice, sticker, location, contact
    """
    try:
        raise ValueError(
            f"Such {message.content_type} is not supported,\nOnly {' or '.join(SUPPORTED_DOCUMENT_TYPES)} files")
    except ValueError as e:
        bot.reply_to(message, f"{BAD_MSG_TYPE}: {e}")  # return ERROR message


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()