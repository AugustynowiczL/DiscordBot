# bot.py
import os
import random
import constants
import asyncio
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
import time

load_dotenv()


bot = Bot(command_prefix='?')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    dice = []
    for i in range(int(number_of_dice)):
        dice.append(str(random.randint(1,int(number_of_sides))))
    await ctx.send(', '.join(dice))

@bot.command(name = 'clear')
async def on_message(ctx, number):
    await ctx.channel.purge(limit = int(number))

@bot.command(name = 'checkid')
async def checkid(ctx, user_id):
    user = await bot.fetch_user(int(user_id))
    print(user)

@bot.command(name ='dm')
async def dm(ctx, user_id, number, message):
    user = await bot.fetch_user(int(user_id))
    message = message.replace('_', ' ')
    print (message)
    for i in range(int(number)):
        await user.send(message)
        print('Recieved')
        time.sleep(1)

@bot.command(name = 'skyrim')
async def cousin(ctx):
    await ctx.send(file=discord.File('cloud.jpg'))

#Adapted from Thomas Kelly's code on how to play sound in voice channel from:
#https://stackoverflow.com/a/53790124
@bot.command(name = 'error')
async def wet(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='C:/Users/Lukas/Desktop/Discord Bot/ffmpeg-20200831-4a11a6f-win64-static/ffmpeg-20200831-4a11a6f-win64-static/bin/ffmpeg.exe', source="error.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    # Delete command after the audio is done playing.
    await ctx.message.delete()

@bot.command(name = 'murloc')
async def wet(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='C:/Users/Lukas/Desktop/Discord Bot/ffmpeg-20200831-4a11a6f-win64-static/ffmpeg-20200831-4a11a6f-win64-static/bin/ffmpeg.exe', source="murloc.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    # Delete command after the audio is done playing.
    await ctx.message.delete()

@bot.command(name = 'peon')
async def wet(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='C:/Users/Lukas/Desktop/Discord Bot/ffmpeg-20200831-4a11a6f-win64-static/ffmpeg-20200831-4a11a6f-win64-static/bin/ffmpeg.exe', source="peon.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    # Delete command after the audio is done playing.
    await ctx.message.delete()

bot.run(constants.TOKEN)



