import discord
from discord.ext import commands
#from data import sensor_data
import modules
import sqlite3
import classes

population = [
    {"name": 'Main Compressor Intake', "temp": 42.5, "vibration": 1.2, "pressure" :101.3 },
    {"name": 'Turbine Exhaust Fan', "temp": 78.1, "vibration": 3.8, "pressure" :98.7 },
    {"name": 'Hydraulic Pump Unit', "temp": 55.4, "vibration": 6, "pressure" :210.5 }
    ]
class Admin(commands.Cog):
    @commands.command()
    async def populate(self, ctx):
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        #cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(ID INTEGER PRIMARY KEY, NAME VARCHAR(255), TEMP REAL, VIBRATION REAL, PRESSURE REAL)""")
        try:
            
            for pop in population:
                name = pop['name']
                temp = pop['temp']
                vibration = pop['vibration']
                pressure = pop['pressure']
                query = f"INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('{name}',{temp},{vibration},{pressure})"

                cursor.execute(query)
            db_connection.commit()
            await ctx.send("Database populated")
        except Exception as e:
            await ctx.send(f"Something went wrong, database not populated: {e}")
            await ctx.send(query)
        db_connection.close()
    @commands.command()

    async def tables(self,ctx):
        try:
            db_connection = sqlite3.connect("./storage/database.db")
            cursor = db_connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(ID INTEGER PRIMARY KEY, NAME VARCHAR(255), TEMP REAL, VIBRATION REAL, PRESSURE REAL)""")
            await ctx.send("Table created")
        except Exception as e:
            await ctx.send("Something went wrong: ", e)
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
   await bot.add_cog(Admin(bot))


# cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(ID INTEGER PRIMARY KEY, NAME VARCHAR(255), TEMP REAL, VIBRATION REAL, PRESSURE REAL)""")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Main Compressor Intake',42.5,1.2,101.3)")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Turbine Exhaust Fan',78.1,3.8,98.7)")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Hydraulic Pump Unit',55.4,6,210.5)")


