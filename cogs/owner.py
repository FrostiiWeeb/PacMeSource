import discord
import asyncio
import json
import traceback
from discord.ext import commands

# adding command_attrs= kwarg allows all commands being added now and
# in the future to be automatically and implicitly hidden
class Owner(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot):
        self.bot = bot

    async def _error_wrap(self, ctx, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            formatted = traceback.format_exception(type(e), e, e.__traceback__)
            joined = ("").join(formatted)
            await ctx.send(f'**`ERROR:`** {joined}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        await self._error_wrap(ctx, self.bot.load_extension, cog)

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        await self._error_wrap(ctx, self.bot.unload_extension, cog)

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        await self._error_wrap(ctx, self.bot.reload_extension, cog)
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user} was banned from {guild.name}\n{guild.id}')

def setup(bot):
    bot.add_cog(Owner(bot)) 
