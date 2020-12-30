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
		main = discord.Embed(colour = 0x95a5a6, title = "Help", description=f'```<> - Required argument.\n[] - Optional argument.\nUse {ctx.prefix}help [Category | Group] for help on that category.\n- my prefix is {ctx.prefix}.```')
		main.add_field(name="> Default Category", value="The Default Category.")
		main.add_field(name="> Config", value="Configuration commands.")
		main.add_field(name="> Covid-19", value="Covid-19 commands.")
		main.add_field(name="> Fun", value="Fun commands.")
		main.add_field(name="> Developer", value="Developer commands.")
		main.add_field(name="> Utility", value="Utility commsnds.")
		main.add_field(name="> Moderation", value = "Moderation commands.")
		main.add_field(name="> Owner", value="Owner commands.")
		await ctx.send(embed=main)
	
	@help.command()
	async def Default(self, ctx):
		defaultc = discord.Embed(colour = 0x95a5a6, title = "Default category")
		defaultc.add_field(name="source", value="```Description:\nThe github repo for the bot.\n------\nAliases:\nsrc\n------\nUsage:\n!*[source|src]\n------```")
		defaultc.add_field(name="stats", value="```Description:\nStats for the bot.\n------\nAliases:\nstatz, binfo, about\n------\nUsage:\n!*[stats|statz|binfo|about]\n------```")			
		await ctx.send(embed=defaultc)
		
	@help.command()
	async def Config(self, ctx):
		configc = discord.Embed(colour = 0x95a5a6, title = "Config category")
		configc.add_field(name="prefix", value="```Description:\nChange the prefix for the bot (not per user).\n------\nAliases:\nNone\n------\nUsage:\n!*prefix <prefix>\n------```")
		await ctx.send(embed=configc)
		
	@help.command()
	async def Covid(self, ctx):
		covidc = discord.Embed(colour = 0x95a5a6, title = "Covid-19 category")
		covidc.add_field(name="covid", value="```Description:\nGet the covid stats of a country.\n------\nAliases:\nNone\n------\nUsage:\n!*covid <country>\n------```")	
		await ctx.send(embed=covidc)
		
	@help.command(aliases=['dev', 'Dev'])
	async def Developer(self, ctx):
		devc = discord.Embed(colour = 0x95a5a6, title = "Developer category")
		devc.add_field(name="uptime", value="```Description:\nGet the uptime of the bot.\n------\nAliases:\nut\n------\nUsage:\n!*[uptime|ut]\n------```")
		devc.add_field(name="screenshot", value="```Description:\nGet the screenshot of a website.\n------\nAliases:\nss\n------\nUsage:\n!*[screenshot|ss] <website>\n------```")
		devc.add_field(name="ping", value="```Description:\nGet the ping of the bot.\n------\nAliases:\npg\n------\nUsage:\n!*[ping|pg]\n------```")
		devc.add_field(name="changelog", value="```Description:\nGet the changelog of the bot.\n------\nAliases:\ncl\n------\nUsage:\n!*[changelog|cl]\n------```")
		await ctx.send(embed=devc)

	@help.command(aliases=['Mod', 'mod'])
	async def Moderation(self, ctx):
		modc = discord.Embed(colour = 0x95a5a6, title = "Moderation category")
		modc.add_field(name="ban", value="```Description:\nBan the member ID you give or member mention.\n------\nAliases:\nb\n------\nUsage:\n!*[ban|b] <member|id> [reason]\n------```")
		modc.add_field(name="unban", value="```Description:\nUnban the member ID you give.\n------\nAliases:\nub\n------\nUsage:\n!*[unban|ub] <member id>\n------```")
		modc.add_field(name="kick", value="```Description:\nKick the member ID or member mention you give.\n------\nAliases:\nk\n------\nUsage:\n!*[kick|k] <member|id> [reason]\n------```")
		modc.add_field(name="clear", value="```Description:\nClear messages.\n------\nAliases:\nc\n------\nUsage:\n!*[clear|c] <amount>\n------```")
		modc.add_field(name="mute", value="```Description:\nMute the member you give.\n------\nAliases:\nm\n------\nUsage:\n!*[mute|m] <member> [reason]\n------```")
		modc.add_field(name="unmute", value="```Description:\nUnmute the member you give.\n------\nAliases:\ndemute, um\n------\nUsage:\n!*[unmute|demute|um] <member>\n------```")
		modc.add_field(name="warn", value="```Description:\nWarn the member you give.\n------\nAliases:\nw\n------\nUsage:\n!*[warn|w] <member> [reason]\n------```")
		modc.add_field(name="giveaway", value="```Description:\nStart a giveaway.\n------\nAliases:\ng\n------\nUsage:\n!*[giveaway|g] <seconds> <prize>\n------```")
		await ctx.send(embed=modc)

	@help.command(aliases=['Own', 'own'])
	async def Owner(self, ctx):
		ownc = discord.Embed(colour = 0x95a5a6, title = "Owner category")
		ownc.add_field(name="load", value="```Description:\nLoad specified category.\n------\nAliases:\nNone\n------\nUsage:\n!*[load] <cog>\n------```")	
		ownc.add_field(name="reload", value="```Description:\nReload specified category.\n------\nAliases:\nNone\n------\nUsage:\n!*[reload] <cog>\n------```")			
		ownc.add_field(name="unload", value="```Description:\nUnload specified category.\n------\nAliases:\nNone\n------\nUsage:\n!*[unload] <cog>\n------```")	
		ownc.add_field(name="restart", value="```Description:\nRestart the bot\n------\nAliases:\nr\n------\nUsage:\n!*[restart|r]\n------```")
		await ctx.send(embed=ownc)		
		
	@help.command()
	async def Fun(self, ctx):
		func = discord.Embed(colour = 0x95a5a6, title = "Fun category")
		func.add_field(name="typeracer", value="```Description:\nDo i really have to explain this? Also, you have to start with \" and end with \"\n------\nAliases:\ntr\n------\nUsage:\n!*[typeracer|tr]\n------```")	
		func.add_field(name="youtube", value="```Description:\nSearch youtube for a video!\n------\nAliases:\nyt\n------\nUsage:\n!*[youtube|yt] <Video name>\n------```")			
		await ctx.send(embed=func)
	
	@help.command(aliases=['Util', 'util'])
	async def Utility(self, ctx):
				utilc = discord.Embed(colour = 0x95a5a6, title = "Utility category")
				utilc.add_field(name="userinfo", value="```Description:\nDo i really have to?\n------\nAliases:\nui\n------\nUsage:\n!*[userinfo|ui] <Member ID or Member Mention>\n------```")
				utilc.add_field(name="perms", value="```Description:\nGet the perms of soemone.\n------\nAliases:\nNone\n------\nUsage:\n!*[perms] <Member ID or Member Mention>\n------```")
				await ctx.send(embed=utilc)
				
				
def setup(bot):
	bot.add_cog(Help(bot))