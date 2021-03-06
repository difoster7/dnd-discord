# Using enhanced-discord.py
# https://github.com/iDevision/enhanced-discord.py
# API: https://enhanced-dpy.readthedocs.io/en/latest/api.html

# Client in the API refers to the bot/the code

import discord
from discord.ext import commands
import logging
from Settlement import Settlement

logging.basicConfig(level=logging.INFO)

bot = commands.Bot("!", intents=discord.Intents(members=True, messages=True), slash_commands=True, slash_command_guilds=[927635655989805076])

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
async def new_settlement(
        ctx: commands.Context, name: str = commands.Option(description='The name of the settlement')):
    # This command adds creates a new settlement
    settlement1 = Settlement(name)
    print(settlement1)
    await ctx.send(settlement1)

@bot.command()
async def role_test(ctx: commands.Context):
    # Are you a tester?
    is_tester = False
    caller = ctx.author
    for role in caller.roles:
        if role.name == 'tester':
            is_tester = True
    if is_tester:
        await ctx.send(str(ctx.author) + ' has the tester role!')
    else:
        await ctx.send(str(ctx.author) + ' does not have the tester role.')




# @bot.command()
# async def kill(ctx: commands.Context):
#     # This kills the bot
#     await ctx.send("Goodbye")
#     exit(0)


# intents = discord.Intents.all()
#
# bot = commands.Bot(command_prefix='>', intents=intents)
#
# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


with open('botID') as f:
    _ID = f.readline()

bot.run(_ID)