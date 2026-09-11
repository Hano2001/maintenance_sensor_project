import discord
from discord.ext import commands
#from data import sensor_data
import modules
import sqlite3
import classes

class Status(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def sensors(self, ctx:commands.Context):
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM SENSORS")
        for row in cursor.fetchall():
                print(row)
                await ctx.send(row)

        db_connection.close()
    # @commands.command()
    # async def check(self,ctx:commands.Context, arg, arg2):
    #     for sensor in sensor_data:
    #         await ctx.send({"id" : sensor["id"], "name" : sensor["name"], arg:sensor[arg]})


    @commands.command()
    async def deletesensor(self,ctx:commands.Context, arg):
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        try:
             sensor_id = arg
             delete_query = (f"DELETE FROM SENSORS WHERE ID = {sensor_id}")
             cursor.execute(delete_query)
             db_connection.commit()
             await ctx.send("Sensor deleted!")
        except:
             await ctx.send("Something went wrong, sensor not deleted correctly")
        db_connection.close()

    @commands.command()
    async def status(self,ctx:commands.Context,arg = ""):
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        search_query =  "SELECT * FROM SENSORS" if arg == "" else f"SELECT * FROM SENSORS WHERE ID = {arg}"
        
        cursor.execute(search_query)
        res = cursor.fetchall()
        
        for sensor in res:
            res_sensor = classes.Sensor(sensor[0],sensor[1],sensor[2], sensor[3])
            sensor_status = res_sensor.field_status_check()
            await ctx.send(f"Status for sensor {sensor[0]} ({sensor[1]})")
            for status in sensor_status:
                await ctx.send(status)
        db_connection.close()

    
async def setup(bot:commands.Bot):
    await bot.add_cog(Status(bot))