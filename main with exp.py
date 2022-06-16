import discord
from discord.ext import commands
import music

cogs = [music] #organize a collection of commands, listeners, and some state into one class.
#a Python class that subclasses commands

client = commands.Bot(command_prefix='?', intents = discord.Intents.all()) 
#initiate the bot
#intents= named groups of pre-defined WebSocket events, which the discord. py client will receive.

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTgxNDkyMjg1NDI0NDM1MjMw.G_K_yT.dFWTn3CbgG33kmfNNJYNLq_BWL7lo-R_XxSfig')


#Using @client/bot.commands() is when you are using a file that isn't being called in a cog or another folder.
#@commands.command() is when client/bot isn't defined also making it so in your async def parameter have to call client
#Example:
#@client.command()
#async def hi(ctx):
#  await ctx.send("Hey!")
#Or for cogs:
#@commands.command()
#async def hi(client,ctx):
#  await ctx.send("Hey")

#@client.command() is a command that can only be used in the main file (where client is defined)
#@commands.command() is can be used in both cogs and the main file.
