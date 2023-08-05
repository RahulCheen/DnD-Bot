import discord
from discord.ext import commands
import os
import config
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   application_id=config.APP_ID)

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
