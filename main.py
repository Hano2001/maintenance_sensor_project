import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
import asyncio
import modules

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    
    async with bot:
        await load_extensions()
        await bot.start(token)


@bot.event
async def on_ready():
    print("Bot logged in!")




asyncio.run(main())