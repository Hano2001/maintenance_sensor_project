from discord.ext import commands
import sqlite3

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
            cursor.execute("""CREATE TABLE IF NOT EXISTS SENSORS(ID INTEGER PRIMARY KEY, NAME VARCHAR(255), TEMP REAL DEFAULT 25, VIBRATION REAL DEFAULT 2.0, PRESSURE REAL DEFAULT 6.0)""")
            await ctx.send("Table created")
            db_connection.commit()
        except Exception as e:
            await ctx.send("Something went wrong: ", e)
        db_connection.close()


    @commands.command()
    async def addsensor(self, ctx, arg):
        
        db_connection = sqlite3.connect("./storage/database.db")
        cursor = db_connection.cursor()
        query = f"INSERT INTO SENSORS(NAME) VALUES('{arg}')"
        cursor.execute(query)
        new_sensor_query = f"SELECT NAME FROM SENSORS WHERE NAME = '{arg}'"
        cursor.execute(new_sensor_query)
        res = cursor.fetchall()
        try:       
            assert res[0][0] == arg
            await ctx.send(f"Sensor {arg} added!")
            db_connection.commit()
        except AssertionError as e:
                print("Error in assert statement")
        
        except Exception as e:
            await ctx.send(f"Something went wrong, could add unit: {e}")
        db_connection.close()


    @commands.command()
    async def deletesensor(self,ctx:commands.Context, arg):
            db_connection = sqlite3.connect("./storage/database.db")
            cursor = db_connection.cursor()
            sensor_id = arg
            sensor_id_query = f"SELECT ID FROM SENSORS WHERE ID = {sensor_id}"
            cursor.execute(sensor_id_query)
            res = cursor.fetchall()
            
            
            try:
                assert res != []
                delete_query = (f"DELETE FROM SENSORS WHERE ID = {sensor_id}")
                cursor.execute(delete_query)
                db_connection.commit()
                await ctx.send("Sensor deleted!")
            except AssertionError:
                print("You entered an invalid ID")
                    
            except:
                await ctx.send("Something went wrong, sensor not deleted correctly")
            
            db_connection.close()



async def setup(bot:commands.Bot):
   await bot.add_cog(Admin(bot))


