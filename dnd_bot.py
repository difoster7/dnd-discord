# bot implementation

import discord
from discord.ext import commands


# class DndBotClient(discord.Client):

class DndBotClient(commands.Bot):
    async def on_ready(self):
        print(f"logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Welcome {member.mention} to {guild.name}:"
            await guild.system_channel.send(to_send)



if __name__ == "__main__":
    # dnd_bot = DndBotClient("!", intents=discord.Intents(members=True, messages=True), slash_commands=True, slash_command_guilds=[927635655989805076])
    dnd_bot = DndBotClient("!", intents=discord.Intents(guilds=True, members=True), slash_commands=True, slash_command_guilds=[927635655989805076])

    @dnd_bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send("Pong!")

    with open('botID') as f:
        _ID = f.readline()

    dnd_bot.run(_ID)
