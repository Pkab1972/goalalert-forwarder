import asyncio
import os
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID", "33309973"))
API_HASH = os.environ.get("API_HASH", "3e4359da0ec8656b02e28beeca07a0ca")
SESSION_STRING = os.environ.get("SESSION_STRING", "")
SOURCE_CHAT = os.environ.get("SOURCE_CHAT", "")
TARGET_CHAT = os.environ.get("TARGET_CHAT", "Staging2")

app = Client("forwarder", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.chat(SOURCE_CHAT))
async def forward(client, message):
    await message.forward(TARGET_CHAT)

print("Userbot running...")
app.run()
