import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTgxNDkyMjg1NDI0NDM1MjMw.G_K_yT.dFWTn3CbgG33kmfNNJYNLq_BWL7lo-R_XxSfig')