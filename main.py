import os
import aiohttp
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33309973
API_HASH = "3e4359da0ec8656b02e28beeca07a0ca"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
WEBHOOK_URL = "https://hook.eu1.make.com/co2ti6ci13jkt1hm75x2gn6dv1fetzva"

INPLAYGURU_CHAT_ID = 1757874218
STAGING3_CHAT_ID = -5514769696

async def main():
    while True:
        try:
            async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
                @client.on(events.NewMessage())
                async def handler(event):
                    if event.chat_id not in [INPLAYGURU_CHAT_ID, STAGING3_CHAT_ID]:
                        return
                    print(f"Message received from chat {event.chat_id}")
                    async with aiohttp.ClientSession() as session:
                        await session.post(WEBHOOK_URL, json={"text": event.raw_text})
                    print("Sent to Make.com!")

                print("Client started, listening...")
                await client.run_until_disconnected()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Reconnecting in 10 seconds...")
            await asyncio.sleep(10)

asyncio.run(main())
