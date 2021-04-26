from sys import argv
from bot import Config
from bot import bot
from bot import logging
from pathlib import Path
from sys import argv
import telethon.utils
from telethon import TelegramClient
from bot.utils import bot_cmd, start_bot
import glob


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.start(bot_token=Config.BOT_TOKEN)
    
path = "bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_bot(shortname.replace(".py", ""))

print("Your Bot is Ready.")
print("Try Sending /start")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
