from . import *
from telethon import custom, events

@bot_cmd("start", is_args=False)
@god_only
async def _(event):
    await event.reply("<b><u>I'm Online</b></u>", parse_mode="HTML")
