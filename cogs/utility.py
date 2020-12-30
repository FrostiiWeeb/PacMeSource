import discord
import datetime
import random
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
    	embed.add_field(name="Joined", value=member.joined_at.strftime(date_format))
    	embed.add_field(name="Registered", value=member.created_at.strftime(date_format))
    	if len(member.roles) > 1:
    	       role_string = ' '.join([r.mention for r in member.roles][1:])
    	       embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)
    	       perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    	       embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    	       embed.set_footer(text='ID: ' + str(member.id))
    	       return await ctx.send(embed=embed)
        
def setup(bot):
	bot.add_cog(Utility(bot))