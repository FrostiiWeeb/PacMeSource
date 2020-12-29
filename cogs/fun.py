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
from discord.ext import commands, tasks
from itertools import cycle
import PIL
from PIL import Image,ImageFont,ImageDraw

class Fun(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(aliases=['tr', 'typeracer'])
	@commands.max_concurrency(1,per=commands.BucketType.channel, wait=False)
	async def type(self, ctx):
	    timeout = [18.0, 16.0, 21.0]
	    answers = ['"The greatest glory in living lies not in never falling, but in rising every time we fall."', '"The way to get started is to quit talking and begin doing."', '"Your time is limited, so don\'t waste it living someone else\'s life."', '"If life were predictable it would cease to be life, and be without flavor."', '"If you dont like the road your walking on, be thankful there\'s a road."', '"If there\'s a thing I\'ve learned in my life it\'s to not be afraid of the responsibility that comes with caring for other people."', '"Help someone, you earn a friend."', '"Your sacred space is where you can find yourself over and over again."', '"Good times & crazy make friends the best memories."', '"A best friend is someone who loves you when you forget to love yourself."', '"Discord.py is a API, you can make discord bot\'s, and makes best freinds impressed."', '"Cyrus is a bot developer, he always has advice."', '"Everybody is a genius. But if you judge a fish by its ability to climb a tree it will live its whole life believing that it is stupid."', '"Believing a rumor is for dummies, if you are smart, research the internet first."', '"Making a discord bot is hard, but you\'ll always make it at the end."', '"Your life has a reason, everybody\'s does. Don\'t feel down."', '"I love those random memories that make me smile no matter what\'s going on in my life right now."', '"Spelling is what we speak, what we type."', '"What you spell, what you speak."']
	    starttime = time.time()
	    amswer = random.choice(answers)
	    timer = random.choice(timeout)
	    embed = discord.Embed(colour=discord.Colour.blurple(), title="Typeracer!", description=f"You have {timer} to type:\n{answer}")
	    await ctx.send(embed=embed)
	
	    def is_correct(msg):
	        return msg.content.startswith('"') and msg.author!=ctx.me
	
	    try:
	        guess = await self.bot.wait_for('message', check=is_correct, timeout=timer)
	    except asyncio.TimeoutError:
	        embed1 = discord.Embed(colour=self.bot.colour, title="GG.", description="Ya dick head's took to long!")
	        return await ctx.send(embed=embed1)
	
	    if guess.content == answer:
	        fintime = time.time()
	        total = fintime - starttime
	        if total >= 8:
	        	embed3 = discord.Embed(colour=discord.Colour.green(), title="Ayyy", description=f"{guess.author} got it, and took:\n{round(total)} seconds.")
	        	await ctx.send(embed=embed3)
	        else:
	         	embed2 = discord.Embed(colour=discord.Colour.blurple(), title="LOOL", description="Imagine cheating..")
	         	return await ctx.send(embed=embed2)	     

def setup(bot):
	bot.add_cog(Fun(bot))