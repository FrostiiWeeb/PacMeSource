import platform
import discord
from discord.ext import commands
from collections import OrderedDict, deque, Counter

class Bot(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(aliases=['info', 'botinfo', 'statz', 'about', 'binfo'])
	async def stats(self, ctx):
	       pythonVersion = platform.python_version()
	       dpyVersion = discord.__version__
	       serverCount = len(self.bot.guilds)
	       memberCount = len(list(self.bot.users))
	       channel_types = Counter(isinstance(c, discord.TextChannel) for c in self.bot.get_all_channels())
	       text = channel_types[True]
	       totalCommands = len(list(self.bot.commands))
	       
	       embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=0xff003d, timestamp=ctx.message.created_at)
	       embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/784122061219954708/185db23b7bf5827147a9eaee6e40c1d3.png?size=1024')
	       
	       embed.add_field(name='**Bot Version:**', value=f"```{self.bot.version}```", inline=False)
	       embed.add_field(name='**Python Version:**', value=f"```{pythonVersion}```", inline=False)
	       embed.add_field(name='**Discord.Py Version:**', value=f"```{dpyVersion}```", inline=False)
	       embed.add_field(name="**Total Cogs:**", value=f"```{len(self.bot.cogs)}```")
	       embed.add_field(name="**Total Commamds:**", value=f"```{totalCommands}")
	       embed.add_field(name="**Total Channels:**", value=f"```{text}```", inline=False)
	       embed.add_field(name='**Total Guilds:**', value=f"```{serverCount}```", inline=False)
	       embed.add_field(name='**Total Users:**', value=f"```{memberCount}```", inline=False)
	       embed.add_field(name='**Bot Developers:**', value="```FrostiiWeeb#0400, Cyrus#8315```", inline=False)
	       
	       embed.set_footer(text=f"{self.bot.user.name}")
	       embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
	       
	       await ctx.send(embed=embed)
	       
def setup(bot):
	bot.add_cog(Bot(bot))