import discord
import sys
from discord.ext import commands
from discord.ext.commands import ConversionError

class Error(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
	    if isinstance(error, commands.MissingRequiredArgument):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error!",
	    	description = f"Missing Argument! Fix that or you'll never get to run {ctx.command}!"
	    	)
	    	await ctx.send(embed=er)
	    if isinstance(error, commands.MissingPermissions):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error!",
	    	description = f"Missing Permissions, you can't run {ctx.command}!"
	    	)
	    	await ctx.send(embed=er)
	    if isinstance(error, commands.CommandNotFound):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error!",
	    	description = f"That isn't a valid command!"
	    	)
	    	await ctx.send(embed=er)	    		 

def setup(bot):
    bot.add_cog(Error(bot))
