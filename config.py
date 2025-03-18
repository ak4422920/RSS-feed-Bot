from telegram import Bot

# Configuration
BOT_TOKEN = "76092"
CHAT_ID = "-1002247400551"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
