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
from typing import Union

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.muted_perms = discord.Permissions(send_messages=False, speak=False)

    async def _get_mute_role(self, guild_id: int):
        # automate the retrieval and (if necessary) instantiation of the
        # muted role
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if not mute_role:
            mute_role = await guild.create_role(name="Muted", permissions=self.muted_perms)
        return mute_role

    async def _do_giveaway(self, ctx: commands.Context, seconds: int, prize: str):
        # handle giveaway logic separately to run within a task
        winner = None
        giveawayembed = discord.Embed(
            title="🎉 __New Giveaway!__ 🎉",
            colour=discord.Color.green(),
            description="React To :tada: To Enter The Giveaway!"
            )

        giveawayembed.add_field(name="Prize", value=prize, inline=False)
        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
        giveawayembed.add_field(name="Ends in", value=f"{seconds}s")
        giveawayembed.set_thumbnail(url=ctx.author.avatar_url)

        msg = await ctx.send(embed=giveawayembed)
        await msg.add_reaction("🎉")
        await asyncio.sleep(seconds)

        msg = await msg.channel.fetch_message(msg.id)

        for reaction in msg.reactions:
            if str(reaction.emoji) == "🎉":
                users = await reaction.users().flatten()
                users.remove(client.user)
                winner = random.choice(users)
                # no need to continue iterating, 
                break

        embed = discord.Embed(
            title="Giveaway ended!",
            colour = discord.Colour.green(),
            description=f"Prize: {prize}\nWinner: {winner}")
        await msg.edit(embed=embed)    
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: Union[discord.Member, int], *, reason="Reason not provided."):
        # the formatting was bothering, able to be reverted - this is
        # the only snippet that is converted
        embed = discord.Embed(
            colour = discord.Colour.blurple(),
            title = f"__New Ban__"
        )
        embed.add_field(name="**Banned by:**", value=f"{ctx.author}", inline=False)
        emebd.add_field(name="**Reason:**", value=f"{reason}", inline=False)
        embed.add_field(name="**Member kicked:**", value=f"{member}", inline=False)

        if isinstance(member, discord.Member):
            await member.send(embed=embed)
            await member.ban(reason=reason)
        else:
            await ctx.guild.ban(discord.Object(member))
        await ctx.send(embed=embed)

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member_id: int):
        user = self.bot.get_user(member_id)
        title = f"Unbanned {user}"

        if user is None:
            title = f"Unbanned user with ID {member_id}"
        embed = discord.Embed(
        colour = discord.Colour.red(),
        title = title
        )

        await ctx.guild.unban(discord.Object(member_id))
        await ctx.send(embed=embed)

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Reason not provided."):
        embed = discord.Embed(
        colour = discord.Colour.blurple(),
        title = f"__New Kick__"
        )
        embed.add_field(name="**Kicked by:**", value=f"{ctx.author}", inline=False)
        emebd.add_field(name="**Reason:**", value=f"{reason}", inline=False)
        embed.add_field(name="**Member kicked:**", value=f"{member}", inline=False)
        
        await member.kick(reason=reason)
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['c'])
    async def clear(self, ctx, amount: int = 2):
        embed = discord.Embed(
        colour = discord.Colour.green(),
        title = "\u2800",
        description = "Cleared {amount} messages!"  
        )

        await ctx.channel.purge(limit=amount)
        await asyncio.sleep(1)
        await ctx.send(embed=embed)
            
    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason="Not Provided."):
        embed = discord.Embed(
        colour = discord.Colour.blue(),
        title = f"__New Mute__"
        )       
        embed.add_field(name=f"!", value = f"{member} Was muted.\nReason:{reason}", inline = False)
        role = await self._get_mute_role(ctx.guild.id)

        await member.add_roles(role)
        await ctx.send(embed=embed)

    @commands.command(aliases=['demute', 'um']) 
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        role = await self._get_mute_role(ctx.guild.id)
        embed = discord.Embed(
        colour = discord.Colour.blue(),
        ttle = f"__Unmute__"
        )
        embed.add_field(name=f"!", value = f"{member} Was muted.\nReason:{reason}", inline=False)

        await member.remove_roles(role)
        await ctx.send(embed=embed)

    @commands.command(aliases=['w'])
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, member: discord.Member, *, arg):
        channel = discord.utils.get(ctx.guild.text_channels, name='warn-logs')

        if channel is None:
            channel = await guild.create_text_channel('warn-logs')
        embed = discord.Embed(color = discord.Color.blue())
        embed.set_author(name='Warning')
        embed.add_field(name='!', value=f'{member} has been warned!', inline=False)
        embed.add_field(name='!', value=f'{member} has been warned because: {arg}', inline=False)
        
        await member.send(embed=embed)        
        await channel.send(embed=embed)

    @commands.command(aliases=['g'])
    @commands.has_permissions(administrator=True)
    @commands.is_owner()
    async def giveaway(self, ctx, seconds: int, *, prize):
        self.bot.loop.create_task(self._do_giveaway(ctx, seconds, prize))
                                                                        
def setup(bot):
    bot.add_cog(Moderation(bot))
