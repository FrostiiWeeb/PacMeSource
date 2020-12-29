import discord
from discord.ext import commands


class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.system_channel:
            embed = discord.Embed(title='PacMe', color=discord.Colour.blurple())
            embed.add_field(name="What's up everyone? I am **PacMe**.", value='\nTry typing `!*help` to get started.', inline=False)
            embed.set_footer(text='Thanks for adding PacMe to your server!')

            await guild.system_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnGuildJoin(bot))
