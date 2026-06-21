import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33309973
API_HASH = "3e4359da0ec8656b02e28beeca07a0ca"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
SOURCE = "InplayGuruBot"
TARGET = -4361831458

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.forward_messages(TARGET, event.message)

client.start()
client.run_until_disconnected()
