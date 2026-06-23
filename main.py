import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33309973
API_HASH = "3e4359da0ec8656b02e28beeca07a0ca"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
TARGET = -4361831458
SOURCE = 1757874218

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    print(f"InPlayGuru alert received!")
    await client.send_message(TARGET, event.raw_text)
    print(f"Sent to Staging2!")

client.start()
client.run_until_disconnected()
