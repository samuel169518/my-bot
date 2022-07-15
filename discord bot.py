import discord
import os
from discord.exe import commands
client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('bot is ready.')

@client.command()
async def mu(ctx):
    Vc = ctx.author.voice.channel
    Members = Vc.members
    for member in Members:
       await member.edit(mute = True)

@client.command()
async def unmu(ctx):
    Vc = ctx.author.voice.channel
    Members = Vc.members
    for member in Members:
        await member.edit(mute = False)
keyword = ["000", "pyautogui"]

@client.event
async def on_message(message):
    for i in range(len (keyword)):
        if keyword [i] in message.content:
            for J in range(10):
                await message.channel.send('')
    await client.process_commands(message)

    

client.run('')
