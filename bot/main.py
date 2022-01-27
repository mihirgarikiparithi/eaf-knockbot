import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')


# cog manager
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


@bot.command(aliases=["r"])
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} reloaded")


@bot.command(aliases=["hr"])
@commands.is_owner()
async def hot_reload(ctx):
    for _file in os.listdir(f'./cogs'):
        if _file.endswith(".py") and file.startswith('cog'):
            bot.reload_extension(f"cogs.{_file[:-3]}")
    await ctx.send('Hot Reload complete', delete_after=5)


# loading in cogs
for file in os.listdir("./cogs"):
    if file.endswith(".py") and file.startswith('cog'):
        bot.load_extension(f"cogs.{file[:-3]}")


# Running bot (blocking)
with open('token.clone', 'r') as f:
    token = f.read()
bot.run(token)
