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

db_connection = sqlite3.connect("./storage/database.db")
cursor = db_connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(NAME VARCHAR(255), TEMP REAL, VIBRATION REAL, PRESSURE REAL)""")
cursor.execute("INSERT INTO SENSORS VALUES ('Main Compressor Intake',42.5,1.2,101.3 )")

print("Data Inserted in the table: ")
cursor.execute("SELECT * FROM SENSORS")
for row in cursor.fetchall():
    print(row)

# Commit changes and close connection
db_connection.commit()
db_connection.close()

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