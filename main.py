import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sqlite3
import asyncio
import modules

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True

# db_connection = sqlite3.connect("./storage/database.db")
# cursor = db_connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(ID INTEGER PRIMARY KEY, NAME VARCHAR(255), TEMP REAL, VIBRATION REAL, PRESSURE REAL)""")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Main Compressor Intake',42.5,1.2,101.3)")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Turbine Exhaust Fan',78.1,3.8,98.7)")
# cursor.execute("INSERT INTO SENSORS(NAME, TEMP, VIBRATION, PRESSURE) VALUES('Hydraulic Pump Unit',55.4,6,210.5)")

# cursor.execute("SELECT name FROM pragma_table_info('SENSORS')")

# print(cursor.fetchall())

# # print("Data Inserted in the table: ")
# # cursor.execute("SELECT * FROM SENSORS")

# # Commit changes and close connection
# db_connection.commit()
# db_connection.close()

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