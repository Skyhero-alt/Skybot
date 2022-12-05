import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from discord.ext import commands
from connect4 import *

load_dotenv()

activity=discord.Game(name="Connect4 for fun")

bot=commands.Bot(command_prefix=",", activity=activity, status=discord.Status.idle)


f=open("help.txt","r")
help=f.readlines()

def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    jd=json.loads(response.text)
    quote=jd[0]['q']
    return quote


@bot.event
async def on_ready():
    print('I am ready as {0.user}'.format(bot))

@bot.event
async def on_message(message):

    caseless_message=(message.content).lower()

    if message.author==bot.user:
        return

    if caseless_message.startswith("hey" or "hello") and message.author!=bot:
        await message.channel.send('Hello Sir')

    if caseless_message.startswith('inspire'):
        await message.channel.send(get_quote())

    if caseless_message.startswith('help'):
        await message.channel.send(str(help[0]))

    await bot.process_commands(message)

@bot.command()
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

games = []

@bot.command(aliases=['p'])
async def play(ctx,mem:discord.Member):
    if (mem !=bot.user):
        games.append(connect_4(ctx,bot,mem))
        await games[-1].connect4game()

bot.run(os.environ['token'])
