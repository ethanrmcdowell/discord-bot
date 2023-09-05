import os

import discord
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GENCHANNEL = os.getenv('GENERAL_CHANNEL')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')


@tasks.loop(seconds=5)
async def min_message():
    channel = client.get_channel(int(GENCHANNEL))
    await channel.send("test")


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

    # min_message.start()

client.run(TOKEN)
