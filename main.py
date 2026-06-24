import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33309973
API_HASH = "3e4359da0ec8656b02e28beeca07a0ca"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
TARGET = "https://hook.eu1.make.com/co2ti6ci13jkt1hm75x2gn6dv1fetzva"
SOURCE = -5514769696

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    print(f"InPlayGuru alert received!")
    import aiohttp
    async with aiohttp.ClientSession() as session:
        await session.post(TARGET, data={"text": event.raw_text})
    print(f"Sent to Make.com!")

client.start()
client.run_until_disconnected()
