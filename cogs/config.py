from discord.ext import commands
import ast
import platform
import discord
from discord import Embed

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

class Owner(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user} was banned from {guild.name}\n{guild.id}')

    @commands.command(aliases=["load", "unload", "reload"])
    @commands.is_owner()
    async def manipulate(self, ctx, *, cog: str):
        manipulate_extension = getattr(
            self.bot,
            f"{ctx.invoked_with}_extension",
            None
        )

        if ctx.invoked_with == "manipulate" or manipulate_extension is None:
            return
        manipulate_extension(cog)
        embed = Embed(title=f"Succesfully {ctx.invoked_with}ed {cog}", description=f"{ctx.invoked_with}ed {cog}", colour=self.bot.colour)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['ev'])
    @commands.is_owner()
    async def eval(self, ctx, *, cmd):
    	fn_name = "_eval_expr"
    	
    	cmd = cmd.strip("` ")
    	cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
    	body = f"async def {fn_name}():\n{cmd}"
    	
    	parsed = ast.parse(body)
    	body = parsed.body[0].body
    	insert_returns(body)
    	env = {
    	'bot': ctx.bot,
    	'discord': discord,
    	'commands': commands,
    	'ctx': ctx,
    	'author': str(ctx.author),
    	'guild': str(ctx.guild),
    	'channel': str(ctx.channel),
    	'guilds': self.bot.guilds,
    	'version': self.bot.version,
    	'cogs': [c for c in self.bot.cogs],
    	'owners': self.bot.owners,
    	'owner_ids': self.bot.owner_ids,
    	'prefix': ctx.prefix,
    	'uptime': str(self.bot.launch_time),
    	'__import__': __import__,
    	'self': self
    	}
    	exec(compile(parsed, filename="<ast>", mode="exec"), env)
    	result = (await eval(f"{fn_name}()", env))
    	if self.bot.http.token in result:
    		await ctx.send(f"```python\n[token omitted]\n```")
    		return
    	else:
    		await ctx.send(f"```python\n{result}\n```")
    		return


def setup(bot):
    bot.add_cog(Owner(bot))
