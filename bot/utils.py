import inspect
import logging
import glob
import re
from pathlib import Path
import functools
from telethon import events

from pymongo import MongoClient
from bot import DATABASE_URL

from bot import bot
from bot import Config

# starting MongoClient
client = MongoClient()
client = MongoClient(DATABASE_URL)
db = client["BotClient"]

bothandler = Config.HANDLER
def bot_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        bot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd

def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = Config.OWNER_ID
            if event.sender_id == moms:
                await func(event)
            else:
                pass

        return wrapper

    return decorator

def start_bot(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        import bot.utils
        path = Path(f"bot/plugins/{shortname}.py")
        name = "bot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Bot...")
        print("Bot Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path
        import bot.utils
        path = Path(f"bot/plugins/{shortname}.py")
        name = "bot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot_cmd = bot_cmd
        mod.bot = bot
        mod.Config = Config
        mod.god_only = god_only()
        mod.sudo_only = sudo_only()
        mod eor = eor
        mod.edit_or_reply = eor
        spec.loader.exec_module(mod)
        sys.modules["bot.plugins" + shortname] = mod
        print("Bot Has imported " + shortname)
