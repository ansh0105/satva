import os
import sys
import asyncio
satva_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])
sys.path.insert(0, satva_dir_path)

from genai_layer import generate_response
from nlp_pipeline.content_analysis import content_analyzer
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('ansh_creds', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    sender_name = sender.username if sender.username else sender.first_name
    message = event.message.message

    if message.startswith("SATVA"):
        await event.respond("Thank you for your message. We are currently analyzing its content to ensure your safety and provide a detailed response.This process usually takes about a minute. Please hold on, and we will get back to you shortly with the results")
        
        spam_stat, sen_stat, ner_stat, url_stat = content_analyzer(message)
        genai_msg = generate_response(sender_name, message, spam_stat, sen_stat, ner_stat, url_stat)

        await event.respond(genai_msg)
    else:
        await event.respond("""Your message does not start with 'SATVA'.\nTo file a complaint, please use the following format:\n\nSATVA: [Your complaint details here]\n\n""")

async def main():
    while True:
        try:
            print("Starting client...")
            await client.start()  
            print("Client started.")
            await client.run_until_disconnected()  
        except (OSError, asyncio.TimeoutError) as e:
            print(f"Connection issue: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)  
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

client.loop.run_until_complete(main())

