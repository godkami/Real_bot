import random
import asyncio
import aiohttp
import json
import discord
import time
import test
import requests
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands 
from bs4 import BeautifulSoup


startup_extensions = ["dict","MAL","hangman","arbitrary","help_info"]

BOT_PREFIX = ("b!")
TOKEN = "NDY4NzIyOTI3Njg5MjY5MjUx.DjL5Gw.4rsuVv1TdTFo1yh6uacm31O8Tjs"  # Get at discordapp.com/developers/applications/me

bot = Bot(command_prefix="BOT_PREFIX")
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))
	
	





async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current servers:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)


bot.loop.create_task(list_servers())

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)
