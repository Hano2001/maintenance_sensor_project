import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
import modules

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
async def check(ctx:commands.Context, arg):
    for sensor in sensor_data:
       
        await ctx.send({"id" : sensor["id"], "name" : sensor["name"], arg:sensor[arg]})


@bot.command()
async def deletesensor(ctx:commands.Context, arg):
    for sensor in sensor_data:
        if sensor.get("id") == arg:
            name = sensor["name"]
            sensor_data.remove(sensor)
            await ctx.send(f"Sensor {name} was succesfully removed!")
            break;

@bot.command()
async def status(ctx:commands.Context,arg = ""):
    for sensor in sensor_data:
        if arg == "":
            status = modules.field_status_check(sensor)
            await ctx.send(sensor)   
            await ctx.send(status if status != [] else "Status OK")   
        else:
            if sensor.get("id") == arg:
                status = modules.field_status_check(sensor)
                await ctx.send(status if status != [] else "Status OK")




bot.run(token)