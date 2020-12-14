import discord
import asyncio
import json
from discord.ext import commands

class Owner(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def load(self, ctx, *, cog: str):
	            try:
	            	self.bot.load_extension(cog)
	            except Exception as e:
	            	await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
	            else:
	            	await ctx.send('**`SUCCESS`**')
	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, *, cog: str):
	           	try:
	           		self.bot.unload_extension(cog)
	           	except Exception as e:
	           			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
	           	else:
	           			await ctx.send('**`SUCCESS`**')

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def reload(self, ctx, *, cog: str):
	           try:
	           	self.bot.unload_extension(cog)
	           	self.bot.load_extension(cog)
	           except Exception as e:
	           	await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
	           else:
	           	await ctx.send('**`SUCCESS`**')
	
	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		
		print(f'{user} was banned from {guild.name}\n{guild.id}')
        	        	        	        	        	        	
def setup(bot):
	bot.add_cog(Owner(bot))	
