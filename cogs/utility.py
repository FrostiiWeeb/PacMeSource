import discord


import datetime


import random


import json

import discord.ext


from discord.ext import commands


from typing import Union





class Utility(commands.Cog):


    def __init__(self, bot):


        self.bot = bot


    


    @commands.Cog.listener()


    async def on_ready(self):


        print(f"Utility Cog has been loaded\n----")


       


    @commands.command(aliases=['userinfo', 'ui'])


    async def whois(self, ctx, member: Union[discord.Member, int] = None):


    	if member == None:


    	    member = ctx.author


    	date_format = "%a, %d %b %Y %I:%M %p UTC"


    	embed = discord.Embed(colour = discord.Colour.blurple(), description=member.mention)


    	embed.set_author(name=str(member), icon_url=member.avatar_url)


    	embed.set_thumbnail(url=member.avatar_url)


    	embed.add_field(name="Joined", value=member.joined_at.strftime(date_format), inline=False)


    	embed.add_field(name="Registered", value=member.created_at.strftime(date_format), inline=False)


    	if len(member.roles) > 1:


    	       role_string = ' '.join([r.mention for r in member.roles][1:])


    	       embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)


    	       perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])


    	       embed.add_field(name="Nick", value=member.nick, inline=False)
    	       
    	       embed.add_field(name="Status", value=str(member.status), inline=False)


    	       embed.add_field(name="Bot?", value=member.bot, inline=False)


    	       if member.id in self.bot.owner_ids:


    	       	embed.add_field(name="Is bot owner?", value=f"True", inline=False)


    	       else:


    	       	embed.add_field(name="Is bot owner?", value="False", inline=False)


    	       embed.add_field(name="Guild permissions", value=perm_string, inline=False)


    	       embed.set_footer(text='ID: ' + str(member.id))


    	       return await ctx.send(embed=embed)


    


    @commands.command(aliases=['server'])


    async def serverinfo(self, ctx, guild: discord.Guild = None):


         if guild == None:


         	guild = ctx.guild


         embed = discord.Embed(title=f'', description="", colour=discord.Colour.blurple())


         embed.set_thumbnail(url=f"{guild.icon_url}")


         embed.add_field(name="Channel Count:", value=f"{len(guild.channels)}", inline=False)


         embed.add_field(name="Role Count:", value=f"{len(guild.roles)}", inline=False)


         embed.add_field(name="Booster Count:", value=f"{guild.premium_subscription_count}", inline=False)


         embed.add_field(name="Member Count:", value=f"{guild.member_count}", inline=False)


         embed.add_field(name="Server Created At:", value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)


         embed.add_field(name="Owner", value=f"{guild.owner}", inline=False)


         embed.set_author(name=f"{guild} | ID: {guild.id}", icon_url="")


         embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=f"{ctx.author.avatar_url}")


         return await ctx.send(embed=embed)	  


    


    @commands.command()


    @commands.is_owner()


    async def perms(self, ctx, member: Union[discord.Member, int] = None):


    	if member == None:


    		member = ctx.author


    	perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])       


    	embed = discord.Embed(colour=discord.Colour.blurple(), title=f"Perms of {member}") 


    	embed.add_field(name="Guild permissions", value=perm_string, inline=False)


    	return await ctx.send(embed=embed)

def setup(bot):


	bot.add_cog(Utility(bot))
