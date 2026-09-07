import discord
from discord.ext import commands
from data import sensor_data
import modules

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def sensors(self, ctx:commands.Context):
       
        for sensor in sensor_data:

            await ctx.send(sensor)


    @commands.command()
    async def check(self,ctx:commands.Context, arg):
        for sensor in sensor_data:
            await ctx.send({"id" : sensor["id"], "name" : sensor["name"], arg:sensor[arg]})


    @commands.command()
    async def deletesensor(self,ctx:commands.Context, arg):
        for sensor in sensor_data:
            if sensor.get("id") == arg:
                name = sensor["name"]
                sensor_data.remove(sensor)
                await ctx.send(f"Sensor {name} was succesfully removed!")
                break;

    @commands.command()
    async def status(self,ctx:commands.Context,arg = ""):
        for sensor in sensor_data:
            if arg == "":
                status = modules.field_status_check(sensor)
                await ctx.send(sensor)   
                await ctx.send(status if status != [] else "Status OK")   
            else:
                if sensor.get("id") == arg:
                    status = modules.field_status_check(sensor)
                    await ctx.send(status if status != [] else "Status OK")


async def setup(bot:commands.Bot):
    await bot.add_cog(Status(bot))