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
import sys
from io import BytesIO
import contextlib
import inspect
import re
from datetime import datetime
import aiohttp
import dotenv
from discord import Activity, ActivityType
from discord import Member
from discord.ext import commands

class Moderation(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")


	@commands.command(aliases=['b'])
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason="Reason not provided."):
	    await member.kick(reason=reason)
	    embed = discord.Embed(
	    colour = discord.Colour.blurple(),
	    title = f"__New Ban__"
	    )
	    embed.add_field(name="**Banned by:**", value=f"{ctx.author}", inline=False)
	    emebd.add_field(name="**Reason:**", value=f"{reason}", inline=False)
	    embed.add_field(name="**Member kicked:**", value=f"{member}", inline=False)
	    
	    chan = await member.create_dm()
	    
	    await chan.send(embed=embed)
	    await ctx.send(embed=embed)

	@commands.command(aliases=['ub'])
	@commands.has_permissions(ban_members=True)
	async def unban(self,ctx, *,member):
		banned_users = await ctx.guild.bans()
		member_name, member_disc = member.split('#')
		
		for banned_entry in banned_users:
			user = banned_entry.user
			
			if(user.name, user.discriminator)==(member_name,member_disc):
			
				await ctx.guild.unban(user)
				embed = discord.Embed(
				colour = discord.Colour.red(),
				title = "Unbanned {user}"
				)
				
				chan = await member.create_dm()
				
				await chan.send(embed=embed)
				await ctx.send(embed=embed)

	@commands.command(aliases=['k'])
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason="Reason not provided."):
	    await member.kick(reason=reason)
	    embed = discord.Embed(
	    colour = discord.Colour.blurple(),
	    title = f"__New Kick__"
	    )
	    embed.add_field(name="**Kicked by:**", value=f"{ctx.author}", inline=False)
	    emebd.add_field(name="**Reason:**", value=f"{reason}", inline=False)
	    embed.add_field(name="**Member kicked:**", value=f"{member}", inline=False)
	    
	    chan = await member.create_dm() 
	    
	    await chan.send(embed=embed)
	    await ctx.send(embed=embed)
	    
	@commands.command(aliases=['c'])
	async def clear(self, ctx, amount):
		    if amount is None:
		    	await ctx.channel.purge(limit=2)
		    	await asyncio.sleep(1)
		    	embed = discord.Embed(
		    	colour = discord.Colour.green(),
		    	title = "\u2800",
		    	description = "Cleared 2 messages!"	
		    	)
		    	await ctx.send(embed=embed)
		    else:
		    	await ctx.channel.purge(limit=amount)
		    	await asyncio.sleep(1)
		    	embed = discord.Embed(
		    	colour = discord.Colour.green(),
		    	title = "\u2800",
		    	description = "Cleared {amount} messages!"	
		    	)
		    	await ctx.send(embed=embed)
	    	
	@commands.command(aliases=['m'])
	@commands.has_permissions(kick_members=True)
	async def mute(self,ctx, member: discord.Member, *, reason="Not Provided."):
	    role = discord.utils.get(ctx.guild.roles, name="Muted")
	    guild = ctx.guild
	    if role not in guild.roles:
	        perms = discord.Permissions(send_messages=False, speak=False)
	        await guild.create_role(name="Muted", permissions=perms)
	        await member.add_roles(role)
	        embed = discord.Embed(
	        colour = discord.Colour.blue(),
	        title = f"__New Mute__"
	        )	    
	        embed.add_field(name=f"!", value = f"{member} Was muted.\nReason:{reason}", inline = False)
	        await ctx.send(embed=embed)
	    else:
	        await member.add_roles(role) 
	        embed = discord.Embed(
	        colour = discord.Colour.blue(),
	        title = f"__New Mute__"
	        )	    
	        embed.add_field(name=f"!", value = f"{member} Was muted.\nReason:{reason}", inline = False)
	        await ctx.send(embed=embed)	    

	@commands.command(aliases=['demute', 'um']) 
	@commands.has_permissions(kick_members=True)
	async def unmute(self,ctx, member: discord.Member):
		role = discord.utils.get(ctx.guild.roles, name="Muted")
		await member.remove_roles(role)
		embed = discord.Embed(
		colour = discord.Colour.blue(),
		ttle = f"__Unmute__"
		)	    
		embed.add_field(name=f"!", value = f"{member} Was muted.\nReason:{reason}", inline=False)
		await ctx.send(embed=embed)

	@commands.command(aliases=['w'])
	
	@commands.has_permissions(kick_members = True)
	
	async def warn(self,ctx, member : discord.Member, *, arg):
	
	    author = ctx.message.author
	    guild = ctx.guild
	    channel = get(guild.text_channels, name='warn-logs')
	    if channel is None:
	        channel = await guild.create_text_channel('warn-logs')
	
	
	
	    embed = discord.Embed(
	
	        color = discord.Color.blue()
	
	
	
	    )
	
	
	
	    embed.set_author(name='Warning')
	
	    embed.add_field(name='!', value=f'{member} has been warned!', inline=False)
	
	    embed.add_field(name='!', value=f'{member} has been warned because: {arg}', inline=False)
	    
	    chan = await member.create_dm()
	    
	    await channel.send(embed=embed)
	    await chan.send(embed=embed)	    

	@commands.command(aliases=['g'])
	@commands.has_permissions(administrator=True)
	@commands.is_owner()
	async def giveaway(self, ctx, time: int, *, prize):
	        giveawayembed = discord.Embed(
	            title="🎉 __New Giveaway!__ 🎉",
	            colour=discord.Color.green(),
	            description="React To :tada: To Enter The Giveaway!"
	            )
	
	        giveawayembed.add_field(name="Prize", value="{}".format(prize), inline=False)
	        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
	        giveawayembed.add_field(name="Ends in", value="{}s".format(time))
	        giveawayembed.set_thumbnail(url=ctx.author.avatar_url)
	
	        msg = await ctx.send(embed=giveawayembed)
	
	        await msg.add_reaction("🎉")
	
	        await asyncio.sleep(time)
	
	        msg = await msg.channel.fetch_message(msg.id)
	        winner = None
	        
	        for reaction in msg.reactions:
	            if reaction.emoji == "🎉":
	                users = await reaction.users().flatten()
	                users.remove(client.user)
	                winner = random.choice(users)
	
	        if winner is not None:
	            endembed = discord.Embed(
	                title="Giveaway ended!",
	                colour = discord.Colour.green(),
	                description="Prize: {}\nWinner: {}".format(prize, winner))
	
	            await msg.edit(embed=endembed)	    	    	    	    	    	    
	    	    	    	    	    	    	    	    	    
def setup(bot):
	bot.add_cog(Moderation(bot))
