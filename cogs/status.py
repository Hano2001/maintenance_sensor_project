import discord
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hello Cog")

async def setup(bot:commands.Bot):
    await bot.add_cog(Status(bot))