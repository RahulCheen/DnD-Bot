import discord
from discord.ext import commands
import os
import config
import asyncio

TOKEN = config.TOKEN
APP_ID = config.APP_ID

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   application_id=APP_ID)

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
