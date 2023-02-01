import discord
from discord.ext import commands
import youtube_dl
import asyncio
from discord import FFmpegPCMAudio

class music(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
    

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
            

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        voice_state = member.guild.voice_client # Get the member in the channel
        if voice_state is not None and len(voice_state.channel.members) == 1: # If bot is alone
           await voice_state.disconnect() # Disconnect
        
    @commands.command()
    async def startq(self,ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except Exception:
            pass
        if not ctx.author.voice or not ctx.author.voice.channel:
            embed = discord.Embed(description='You should be connected to a voice channel to use the `play` command.', color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        vc = ctx.guild.voice_client
        vc.play(discord.FFmpegPCMAudio('/Users/sinembilgeguler/Desktop/long_break.mp3'))

    @commands.command(name= 'p_start')
    async def timer(self,ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except Exception:
            pass
        if not ctx.author.voice or not ctx.author.voice.channel:
            embed = discord.Embed(description='You should be connected to a voice channel to use the `p_start` command.', color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        await ctx.send("you can start studying now!")
        await ctx.send("Timer: 15")
        cmd = self.client.get_command('startq')
        await cmd(ctx)
        await asyncio.sleep(9)
        await ctx.send("You can now give a break!")
        cmd = self.client.get_command('startq')
        await cmd(ctx)
        await ctx.send("Timer: 5")
        await asyncio.sleep(3)
        await ctx.send("The break is over!")
        cmd = self.client.get_command('startq')
        await cmd(ctx)
        await ctx.send("Restart the pomodoro?")
        msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
        if msg.content.lower() in ("y", "yes"):
            await self.timer.invoke(ctx)
        else:
            await ctx.send("Bye!")

        
def setup(client):
    client.add_cog(music(client))

