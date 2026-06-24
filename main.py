import os
import aiohttp
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33309973
API_HASH = "3e4359da0ec8656b02e28beeca07a0ca"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
WEBHOOK_URL = "https://hook.eu1.make.com/co2ti6ci13jkt1hm75x2gn6dv1fetzva"

INPLAYGURU_CHAT_ID = 1757874218  # private chat με InPlayGuru bot
STAGING3_CHAT_ID = -5514769696   # ακούμε και αυτό για manual tests

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=[INPLAYGURU_CHAT_ID, STAGING3_CHAT_ID]))
async def handler(event):
    print(f"Message received from chat {event.chat_id}")
    print(f"Text: {event.raw_text[:100]}")
    async with aiohttp.ClientSession() as session:
        await session.post(WEBHOOK_URL, data={"text": event.raw_text})
    print("Sent to Make.com!")

client.start()
client.run_until_disconnected()
