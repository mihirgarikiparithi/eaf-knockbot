import discord
from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot Online...")

    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Activity(name="with your heart")
        await self.bot.change_presence(activity=game)
        print(f'Bot Ready with ping of: {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}ms')


def setup(client):
    client.add_cog(Startup(client))

