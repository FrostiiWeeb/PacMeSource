import asyncio
import random
import time
import aiohttp
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.timeouts = [17.0, 19.0, 22.0]
        self.quotes = [
            "The greatest glory in living lies not in never falling, but in "
            "rising every time we fall.",
            "The way to get started is to quit talking and begin doing.",
            "Your time is limited, so don't waste it living someone else's "
            "life.",
            "If life were predictable it would cease to be life, and be "
            "without flavor.",
            "If you dont like the road your walking on, be thankful there's a "
            "road.",
            "If there's a thing I've learned in my life it's to not be afraid "
            "of the responsibility that comes with caring for other people.",
            "Help someone, you earn a friend.",
            "Your sacred space is where you can find yourself over and over "
            "again.",
            "Good times & crazy make friends the best memories.",
            "A best friend is someone who loves you when you forget to love "
            "yourself.",
            "Discord.py is a API, you can make discord bot's, and makes best "
            "freinds impressed.",
            "Everybody is a genius. But if you judge a fish by its ability to "
            "climb a tree it will live its whole life believing that it is "
            "stupid.",
            "Believing a rumor is for dummies, if you are smart, research the "
            "internet first.",
            "Making a discord bot is hard, but you'll always make it at the "
            "end.",
            "Your life has a reason, everybody's does. Don't feel down.",
            "I love those random memories that make me smile no matter what's "
            "going on in my life right now.",
            "Spelling is what we speak, what we type.",
            "What you spell, what you speak."
        ]

    @commands.command(aliases=['tr', 'typeracer'])
    @commands.max_concurrency(1, per=commands.BucketType.channel, wait=False)
    async def type(self, ctx):
        quote = f'"{random.choice(self.quotes)}"'
        timeout = random.choice(self.timeouts)
        embed = discord.Embed(
            title="Typeracer!",
            description=f'You have {timeout} to type:\n{quote}',
            colour=discord.Colour.blurple()
        )

        def is_correct(msg):
            # prevent all bots from partaking - prevents auto-cheating
            return (msg.content.startswith('"') and
                    msg.content.endswith('"') and
                    not msg.author.bot)

        await ctx.send(embed=embed)
        start = time.time()  # start timer once quote is sent
        embed = discord.Embed(title="LOOL",
                              description="Imagine cheating..",
                              colour=discord.Colour.blurple())

        try:
            guess = await self.bot.wait_for("message",
                                            check=is_correct,
                                            timeout=timeout)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="GG.",
                                  description="Ya dick head's took too long!",
                                  colour=self.bot.colour)
        else:
            if guess.content == quote:
                print("In")
                end = time.time()
                diff = end - start

                if diff >= 8:
                    print("In")
                    embed = discord.Embed(
                        title="Ayyy",
                        description=f"{guess.author} got it, and took:\n"
                                    f"{round(diff)} seconds.",
                        colour=discord.Colour.green()
                    )
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *, search):
	     BASE = "https://youtube.com/results"
	     p = {"search_query": search}
	     # Spoof a user agent header or the request will immediately fail
	     h = {"User-Agent": "Mozilla/5.0"}
	     async with aiohttp.ClientSession() as client:
	             async with client.get(BASE, params=p, headers=h) as resp:
	             	dom = await resp.text()
	             	found = re.findall(r'href"\/watch\?v=([a-zA-Z0-9_-]{11})', dom)
	             	return await ctx.send(f"https://youtu.be/{found[0]}")

def setup(bot):
    bot.add_cog(Fun(bot))
