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
	    	title = "Error",
	    	description = f":x:**Missing required argument(s).**"
	    	)
	    	er.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	    	await ctx.send(embed=er)
	    if isinstance(error, commands.MissingPermissions):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error",
	    	description = f":x:**Missing permission(s).**"
	    	)
	    	er.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	    	await ctx.send(embed=er)
	    if isinstance(error, commands.CommandNotFound):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error",
	    	description = f":x:**The command you provided is invalid.**"
	    	)
	    	er.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	    	await ctx.send(embed=er)	  
	    if isinstance(error, commands.NotOwner):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error",
	    	description = ":x:**You don't own this bot.**"
	    	)	
	    	er.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)	
	    	await ctx.send(embed=er) 
	    if isinstance(error, commands.NSFWChannelRequired):
	    	er = discord.Embed(
	    	colour = discord.Colour.red(),
	    	title = "Error",
	    	description = ":x:**{ctx.command} Is required to be invoked in a NSFW channel."
	    	)
	    	er.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	    	await ctx.send(embed=er)

def setup(bot):
    bot.add_cog(Error(bot))
