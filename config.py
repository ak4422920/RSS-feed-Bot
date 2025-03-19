from telegram import Bot

# Configuration
BOT_TOKEN = "7609220129:AAH"
CHAT_ID = "-1002250141502"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
