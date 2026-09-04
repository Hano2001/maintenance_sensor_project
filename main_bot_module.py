import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

filename = "sensors.json"
with open(filename) as jfile:
    sensor_data = json.load(jfile)

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="#", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True


@bot.command()
async def sensors(ctx:commands.Context):
    for sensor in sensor_data:

        await ctx.send(sensor)


bot.run(token)