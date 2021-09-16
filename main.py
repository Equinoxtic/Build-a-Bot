import os
import discord
import random

from random import randrange
from discord import channel
from discord import colour
from discord import user
from discord.embeds import Embed
from discord import client

client = discord.Client()

@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message}: ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'channel-goes-here':

        # Write some code here

client.run() # Run Bot token here