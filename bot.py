import discord
from discord.utils import get
import asyncio
from asyncio import sleep
from asyncio import gather
import random
import datetime
import platform
from discord.ext.commands import ConversionError
import json
from json import dump, load
import os
from discord import Member
import time
import io
import sqlite3
import sys
from io import BytesIO
import contextlib
import inspect
from datetime import datetime
import aiohttp
import dotenv 
from dotenv import load_dotenv
from discord import Activity, ActivityType
from discord import Member
from discord.ext import commands
from pretty_help import PrettyHelp

intents = discord.Intents.default()

intents.members = True



with open("prefixes.json") as f:
    prefixes = json.load(f)
default_prefix = "!*"

def prefix(bot, message):
    id = message.guild.id
    return prefixes.get(id, default_prefix)

color = discord.Color.red()
bot = commands.Bot(command_prefix = prefix, intents = intents, fetch_offline_members = True, case_insensitive=True, help_command=PrettyHelp(color=color, active=30))
bot.launch_time = datetime.utcnow()

async def status():
	while True:
		await bot.wait_until_ready()
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers | !*help."))
		await sleep(5)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Commands: !*help"))
		await sleep(5)
		await bot.change_presence(activity=discord.Game(name="On discord.py!"))
		await sleep(5)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"PacMan"))		
@bot.event
async def on_ready():
    print ('                              ================================================')
    print ('                                            Bot is now online!')
    print ('')
    print ('                                            Logged in as:')
    print ('                                            {0.user}'.format(bot))
    print('')
    print ('                                            ID:')
    print (f'                                            {bot.user.id}')
    print ('')
    print ('                                            Working on:')
    print (f'                                            {len(bot.guilds)} servers!')
    print('')
    print ('                                            My prefix is:')
    print (f'                                            !*')
    print('')
    print('')
    print ('                              ================================================')
    bot.loop.create_task(status())
    class colors:
    	default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, new_prefix=''):
	    prefixes[ctx.message.guild.id] = new_prefix
	    with open("prefixes.json", "w") as f:
	        	json.dump(prefixes, f)
	        	embed = discord.Embed(
	        	colour = discord.Colour.blurple(),
	        	title = " ",
	        	description = f"Hey {ctx.author.name}! I see you changed the prefix to {new_prefix}."
	        	)
	        	await ctx.send(embed=embed)

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"
        	    						    						
        	    						     						
bot.load_extension('jishaku')   	    	    
	   	                                 
for filename in os.listdir('./cogs'):
  if filename.endswith('.py') and not filename.startswith('_'):
    bot.load_extension(f'cogs.{filename[:-3]}')

    
load_dotenv()
token = os.getenv('DISCORD_TOKEN')            
bot.run(token)
