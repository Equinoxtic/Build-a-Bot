from logging import info
import os
import discord
import random

from random import randrange
from discord import channel
from discord import colour
from discord import user
from discord.embeds import Embed
from discord import client

TOKEN = 'token-goes-here'

client = discord.Client()


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message}: ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'testing-ground' or message.channel.name == 'chat':

        if message.content.startswith('!sample'):
            newEmbed = discord.Embed(
                title="Title",
                description="Description",
                colour=discord.colour.Color.blue()
            )
            newEmbed.set_thumbnail(
                url="url-goes-here"
            )
            newEmbed.set_image(
                url="url-goes-here"
            )
            newEmbed.set_author(
                name="name-goes-here",
                url="url-goes-here",
                icon_url="url-goes-here"
            )
            newEmbed.set_footer(
                text="Text",
                icon_url="url-goes-here"
            )
            await message.channel.send(newEmbed)

client.run(TOKEN)