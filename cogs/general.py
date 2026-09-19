import discord
from discord.ext import commands
#from data import sensor_data
import modules
import sqlite3
import classes

class General(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def sensors(self, ctx:commands.Context):
        print("Trying to check sensors")
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM SENSORS")
        db_connection.commit()
        for row in cursor.fetchall():
                print(row)
                await ctx.send(row)

        db_connection.close()

    @commands.command()
    async def status(self,ctx:commands.Context,arg = ""):
        print("Trying to check status")
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        search_query =  "SELECT * FROM SENSORS" if arg == "" else f"SELECT * FROM SENSORS WHERE ID = {arg}"
        
        cursor.execute(search_query)
        res = cursor.fetchall()
        db_connection.commit()
        for sensor in res:
            res_sensor = classes.Sensor(sensor[0],sensor[1],sensor[2], sensor[3], sensor[4])
            sensor_status = res_sensor.field_status_check()
            await ctx.send(f"Status for sensor {sensor[0]} ({sensor[1]})")
            for status in sensor_status:
                await ctx.send(status)
        db_connection.close()


    @commands.command()
    async def checktable(self,ctx):
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print("Fetching tables...")
        print(cursor.fetchall())
        db_connection.close()
    
         
    
async def setup(bot:commands.Bot):
    await bot.add_cog(General(bot))