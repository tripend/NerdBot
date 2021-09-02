import discord
import os

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    nerd1 = os.getenv('NERD1')
    nerd2 = os.getenv('NERD2')

    if  str(message.author.id) == nerd1 or str(message.author.id) == nerd2:
         await message.add_reaction('🇳')
         await message.add_reaction('🇪')
         await message.add_reaction('🇷')
         await message.add_reaction('🇩')

client.run(os.getenv('TOKEN'))        