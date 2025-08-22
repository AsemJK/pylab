import os
from discord import Client,Message,Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DICORD_TOKEN')
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def on_message(message:Message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


