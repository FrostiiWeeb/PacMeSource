from discord.ext import commands


class Owner(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return self.bot.is_owner(ctx.author)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user} was banned from {guild.name}\n{guild.id}')

    @commands.command(aliases=["load", "unload", "reload"])
    async def manipulate(self, ctx, *, cog: str):
        manipulate_extension = getattr(
            self.bot,
            f"{ctx.invoked_with}_extension",
            None
        )

        if ctx.invoked_with == "manipulate" or manipulate_extension is None:
            return
        manipulate_extension(cog)


def setup(bot):
    bot.add_cog(Owner(bot))
