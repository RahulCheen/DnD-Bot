import discord
from discord.ext import commands
import os
import json
import asyncio

config = json.load(open('config.json'))
TOKEN = config["TOKEN"]
APP_ID = config["APP+ID"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   application_id=str(APP_ID))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message[0] == '!':
        return

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
