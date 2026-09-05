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
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True


@bot.command()
async def sensors(ctx:commands.Context):
    for sensor in sensor_data:

        await ctx.send(sensor)


@bot.command()
async def vibration(ctx:commands.Context):
    for sensor in sensor_data:
        vib_level = float(sensor["vibration"])
        if vib_level > 10:
            status = "Critical"
        elif vib_level > 5:
            status = "Warning"
        else:
            status = "Ok"
        report = {"Name": sensor["name"],
                  "Vibration": vib_level,
                  "Status":status}
        await ctx.send(report)
bot.run(token)