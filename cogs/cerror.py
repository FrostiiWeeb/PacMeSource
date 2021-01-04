import sys
import traceback

import discord
from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.errors = {
            commands.MissingRequiredArgument: "Missing required argument(s): "
                                              "{error.param}",
            commands.MissingPermissions: "Missing permission(s):\n{error.param}",
            commands.CommandNotFound: "The command you provided is invalid.",
            commands.NotOwner: "You don't own this bot.",
            commands.NSFWChannelRequired: "{ctx.command} is required to be "
                                          "invoked in a NSFW channel.",
            commands.MaxConcurrencyReached: "{ctx.command} is already being "
                                            "used, please wait.",
            commands.DisabledCommand: "{ctx.command} has been disabled, please wait until it's enabled."
        }

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        description: str = None

        if isinstance(error, tuple(self.errors.keys())):
            reinvokable = (isinstance(error, commands.MissingPermissions) and
                           await self.bot.is_owner(ctx.author))

            if reinvokable:
                return await ctx.reinvoke()
            description = str.format(self.errors[type(error)],
                                     ctx=ctx,
                                     error=error)
        else:
            formatted = traceback.format_exception(
                type(error),
                error,
                error.__traceback__
            )
            description = ("").join(formatted)
            print(description, file=sys.stderr)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description=f"❌**{description}**",
            title="Error"
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


def setup(bot):
    bot.add_cog(Error(bot))
