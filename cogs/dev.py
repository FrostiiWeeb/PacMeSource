import discord
import os
import aiohttp
import io
from io import BytesIO
from discord.ext import commands

class Develepor(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
	@commands.command(aliases = ["ss"])
	@commands.is_owner()
	async def screenshot(self, ctx, url):
	        start = time.perf_counter()
	        
	        embed = discord.Embed(title = f"Screenshot of {url}", color = discord.Color.from_rgb(48,162,242))
	        async with aiohttp.botSession() as cs:
	            async with cs.get(f'https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{url}') as r:
	            	res = await r.read()
	            	embed.set_image(url="attachment://pp.png")
	            	end = time.perf_counter()
	            	embed.set_footer(text = f"Image fetched in {round((end - start) * 1000)} ms")
	            	await ctx.send(file=discord.File(io.BytesIO(res), filename="screenshot.png"), embed=embed)                                             	

	@commands.command(aliases=['ut'])
	async def uptime(self, ctx):
	    delta_uptime = datetime.utcnow() - self.bot.launch_time
	    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	    minutes, seconds = divmod(remainder, 60)
	    days, hours = divmod(hours, 24)
	    await ctx.send(f"{days}d, {hours}h, {minutes}m")
	    	   		   		   	
def setup(bot):
	bot.add_cog(Develepor(bot))
