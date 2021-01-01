import traceback
import sys
import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(invoke_without_command=True)
	async def help(self, ctx):
		pages = 2
		cur_page = 1
		main = discord.Embed(colour = 0x95a5a6, title = "Help", description=f'```<> ← Required argument.\n[] ← Optional argument.\n+ Use {ctx.prefix}help [Category | Group] for help module help.```')
		main.add_field(name="> Default", value="source - stats", inline=False)
		main.add_field(name="> Config", value="prefix", inline=False)
		main.add_field(name="> Covid-19", value="covid", inline = False)
		main.add_field(name="> Fun", value="typeracer", inline=False)
		main.set_footer(text=f"Page {cur_page}/{pages}")
		main1 = discord.Embed(colour = 0x95a5a6, title = "Help", description=f'```<> ← Required argument.\n[] ← Optional argument.\n+ Use {ctx.prefix}help [Category | Group] for help module help.```')
		main1.add_field(name="> Developer", value="screenshot - uptime - changelog", inline=False)
		main1.add_field(name="> Utility", value="whois - serverinfo - perms", inline=False)
		main1.add_field(name="> Moderation", value = "ban - unban - kick - clear - warn - mute - unmute - giveaway", inline=False)
		main1.add_field(name="> Owner", value="load - reload - unload - restart", inline=False)
		main1.set_footer(text=f"Page 2/{pages}")
		message = await ctx.send(embed=main)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")
		await message.add_reaction('⏹️')
		
		def check(reaction, user):
		       return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️", '⏹️']
		
		while True:
		           try:
		           	reaction, user = await self.bot.wait_for("reaction_add", timeout=60.5, check=check)
		           	
		           	if str(reaction.emoji) == "▶️" and cur_page != pages:
		           	   cur_page += 1
		           	   await message.edit(embed=main1)
		           	
		           	elif str(reaction.emoji) == "◀️":
		           		await message.edit(embed=main)
		           	
		           	elif str(reaction.emoji) ==  '⏹️':
		           		await message.delete()
		           		break
		           		return
		           	
		           	else:
		           		pass
		           except asyncio.TimeoutError:
		           			if not message:
		           				break
		           				return
		           			else:
		           				await message.delete()
		           				break
		           				return
	
	@help.command()
	async def Default(self, ctx):
		defaultc = discord.Embed(colour = 0x95a5a6, title = "Default category")
		defaultc.add_field(name="-----", value=f"```{ctx.prefix}[source|src]``` - Get the source for the bot.", inline=False)
		defaultc.add_field(name="-----", value=f"```{ctx.prefix}[about]``` - The about page for the bot.", inline=False)			
		await ctx.send(embed=defaultc)
		
	@help.command()
	async def Config(self, ctx):
		configc = discord.Embed(colour = 0x95a5a6, title = "Config category")
		configc.add_field(name="-----", value=f"```{ctx.prefix}[prefix] <New Prefix>``` - Change the bot\'s prefix, not per user.", inline = False)
		await ctx.send(embed=configc)
		
	@help.command()
	async def Covid(self, ctx):
		covidc = discord.Embed(colour = 0x95a5a6, title = "Covid-19 category")
		covidc.add_field(name="-----", value=f"```{ctx.prefix}[covid] <country>``` - Get the covid-69 stats of a country.", inline=False)	
		await ctx.send(embed=covidc)
		
	@help.command(aliases=['dev', 'Dev'])
	async def Developer(self, ctx):
		devc = discord.Embed(colour = 0x95a5a6, title = "Developer category")
		devc.add_field(name="-----", value=f"```{ctx.prefix}[uptime]``` - Get the uptime for the bot.",inline=False)
		devc.add_field(name="-----", value=f"```{ctx.prefix}[screenshot|ss] <url>``` - Get a screenshot of a website.", inline=False)
		devc.add_field(name="-----", value=f"```{ctx.prefix}[changelog|cl]``` - The bot changelog.", inline=False)
		await ctx.send(embed=devc)

	@help.command(aliases=['Mod', 'mod'])
	async def Moderation(self, ctx):
		modc = discord.Embed(colour = 0x95a5a6, title = "Moderation category")
		modc.add_field(name="-----", value=f"```{ctx.prefix}[ban|b] <member or member ID> [reason]``` - Ban a member from the guild.", inline=False)
		modc.add_field(name="-----", value=f"```{ctx.prefix}[unban|ub] <Member ID>``` - Unban a user from the guild.", inline=False)
		modc.add_field(name="-----", value=f"```{ctx.prefix}[kick|k] <member or member ID> [reason]``` - Kick a member within the guild.", inline=False)
		modc.add_field(name="-----", value=f"```{ctx.prefix}[clear|c] [amount]``` - Clear a specific amount of msgs.", inline=False)
		mod = discord.Embed(colour = 0x95a5a6, title = "Moderation category", inline=False)
		mod.add_field(name="-----", value=f"```{ctx.prefix}[mute|m] <member> [reason]``` - Mute a member.", inline=False)
		mod.add_field(name="-----", value=f"```{ctx.prefix}[unmute|um] <member>``` - Unmute a member in the guild.", inline=False)
		mod.add_field(name="-----", value=f"```{ctx.prefix}[warn|w] <member> [reason]``` - Warn a member.", inline=False)
		mod.add_field(name="----", value=f"```{ctx.prefix}[giveaway|g] <seconds> <prize>```- Start a giveaway!", inline=False)
		msge = await ctx.send(embed=modc)
		await msge.add_reaction("◀️")
		await msge.add_reaction("▶️")
		
		def check(reaction, user):
		       return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
		
		while True:
		           try:
		           	reaction, user = await self.bot.wait_for("reaction_add", timeout=60.5, check=check)
		           	
		           	if str(reaction.emoji) == "▶️":
		           	   await msge.edit(embed=mod)
		           	
		           	elif str(reaction.emoji) == "◀️":
		           		await msge.edit(embed=modc)
		           except asyncio.TimeoutError:
		           	break
		           	return
		           	
	"""Start here"""

	@help.command(aliases=['Own', 'own'])
	async def Owner(self, ctx):
		ownc = discord.Embed(colour = 0x95a5a6, title = "Owner category")
		ownc.add_field(name="-----", value=f"```{ctx.prefix}[load] <cog>``` - Load a cog!", inline=False)	
		ownc.add_field(name="-----", value=f"```{ctx.prefix}[unload] <cog>``` - Unload a cog!", inline=False)			
		ownc.add_field(name="-----", value=f"```{ctx.prefix}[reload] <cog>``` - Reload a cog!", inline=False)	
		ownc.add_field(name="-----", value=f"```{ctx.prefix}[restart|r]``` - Restart the bot.", inline=False)
		await ctx.send(embed=ownc)		
		
	@help.command()
	async def Fun(self, ctx):
		func = discord.Embed(colour = 0x95a5a6, title = "Fun category")
		func.add_field(name="-----", value=f"```{ctx.prefix}[typeracer|tr]``` - Start a game of typeracer!", inline=False)				
		await ctx.send(embed=func)
	
	@help.command(aliases=['Util', 'util'])
	async def Utility(self, ctx):
				utilc = discord.Embed(colour = 0x95a5a6, title = "Utility category")
				utilc.add_field(name="-----", value=f"```{ctx.prefix}[userinfo|ui] [member or member ID]``` - Get the info of a user!", inline=False)
				utilc.add_field(name="-----", value=f"```{ctx.prefix}[userinfo|ui] [member or member ID]``` - Get the info of the server!", inline=False)
				utilc.add_field(name="-----", value=f"```{ctx.prefix}perms [member]``` - Get the permissions of a member!", inline=False)
				await ctx.send(embed=utilc)
				
				
def setup(bot):
	bot.add_cog(Help(bot))
