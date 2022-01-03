# Using enhanced-discord.py
# https://github.com/iDevision/enhanced-discord.py


import discord
from discord.ext import commands

bot = commands.Bot("!", intents=discord.Intents(guilds=True, messages=True), slash_commands=True, slash_command_guilds=[927635655989805076])

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command()
# You can use commands.Option to define descriptions for your options, and converters will still work fine.
async def ping(
    ctx: commands.Context, emoji: bool = commands.Option(description="whether to use an emoji when responding")
):
    # This command can be used with slash commands or message commands
    if emoji:
        await ctx.send("\U0001f3d3")
    else:
        await ctx.send("Pong!")


@bot.command(message_command=False)
async def only_slash(ctx: commands.Context):
    # This command can only be used with slash commands
    await ctx.send("Hello from slash commands!")


@bot.command(slash_command=False)
async def only_message(ctx: commands.Context):
    # This command can only be used with a message
    await ctx.send("Hello from message commands!")


@bot.command()
async def kill(ctx: commands.Context):
    await ctx.send("Good bye")
    exit(0)


# intents = discord.Intents.all()
#
# bot = commands.Bot(command_prefix='>', intents=intents)
#
# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')




bot.run('OTI3NjQzNTM2NDk1NjExOTE2.YdNNXQ.aF2ijAVPs5iMV_a64F7f1tdEZko')