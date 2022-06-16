import discord
from discord.ext import commands
import youtube_dl #It handles anything yooutube related 
import asyncio
from discord import FFmpegPCMAudio
#All commands must now take a self parameter to allow usage of instance
#attributes that can be used to maintain state
class music(commands.Cog):
    def __init__(self, client): 
        self.client = client
#If we are going to derive an object from a class, __init__ must be the first method of the class.
# Properties of objects derived from Class are assigned to objects with this method.

##self
#The self keyword is a concept that comes with the __init__ method and allows us to access the objects that we have derived from the class.
#calling the properties of the class with self


#async/await handles the Prromises. Promises represent an unfinished and ongoing process.
# A Promise can have three states; pending, resolved, and rejected
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None: #If the person is not in the voice channel
            await ctx.send("You are not in a voice channel")
        voice_channel = ctx.author.voice.channel #Variable declearing the voice channel
        if ctx.voice_client is None:#If the bot is not in a voice channel
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel) #If it is connected go to the voice channel
    #move to moving the info to another 
   

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command() #play is the command
    async def play(self,ctx,url):
        #ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streaemd 1 -reconnect_delay_max 5 ',
                          'options': '-vn'}#FFMPEG handles the youtube straeaming in discord 
    #Those are the typical FFMPEG options that are written on discord portal
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client #declearing the voice chat

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegPCMAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            #vc.play(FFmpegPCMAudio(source))
            




    @commands.command(name= 'p_start')
    async def timer(self,ctx):
        await ctx.send("Timer: 15")
        await ctx.invoke(self.client.get_command('play'))
        play('https://www.youtube.com/watch?v=NAHRpEqgcL')
        await asyncio.sleep(9)
        await ctx.send("You can now give a break!")
        await ctx.send("Timer: 5")
        await asyncio.sleep(3)
        await ctx.send("The break is over!")
        await ctx.send("Restart the pomodoro")


   # @client.command()
   # async def sing(ctx):
    #    user = ctx.author.voice
    #if user is not None:
     #   channel = ctx.author.voice.channel
    #    voice = await channel.connect()
    #    voice.play(discord.FFmpegPCMAudio(executable="C:/Path_Program/ffmpeg.exe", source=r"C:\Users\sinembilgeguler\Desktop\long_break.mp3"))
    #else:
     #   await ctx.send("Beep beep! (Be in a voice channel please!)")


    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send('Pause')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Resume')

        
#bot = Bot()
def setup(client): #define client 
    client.add_cog(music(client)) #adds cog to the client

