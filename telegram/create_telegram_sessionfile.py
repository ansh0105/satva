from telethon import TelegramClient

api_id = 'your_api_id'
api_hash = 'your_api_hash'
session_name = 'your_session_name'

client = TelegramClient(session_name, api_id, api_hash)
async def main():
    await client.start()
    print("Session file created successfully.")

with client:
    client.loop.run_until_complete(main())
