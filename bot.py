# We import our modules.

import json
import os
from datetime import datetime
from itertools import cycle
import discord
import logging
from discord.ext import commands, tasks
from pathlib import Path
from discord.ext.commands import Bot
import inspect

# Shows the current working directory.

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----\nBot Type: commands.Bot\n-----")

# Define our default prefix.

default_prefix = "!*"

f = "./prefixes.json"
mr = 'r'

# Gets the prefix for the bot.

def get_prefix(bot, ctx):
    with open(f, mr) as fl:
        prefixes = json.load(fl)

    return prefixes.get(str(ctx.guild.id), default_prefix)

# Makes a class for the colours.

class Colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

# Defining a few things.

class HelpCommand(commands.MinimalHelpCommand):
	async def send_pages(self):
	       destination = self.get_destination()
	       for page in self.paginator.pages:
	           emby = discord.Embed(description=page, colour=discord.Colour.light_grey())
	           await destination.send(embed=emby)
	async def send_command_help(self, command):
	           	embed = discord.Embed(title=self.get_command_signature(command))
	           	destination = self.get_destination()
	           	embed = discord.Embed(title=self.get_command_signature(command), colour=discord.Colour.light_grey())
	           	embed.add_field(name="Description:", value=command.help)
	           	alias = command.aliases
	           	if alias:
	           		embed.add_field(name="Aliases:", value=", ".join(alias), inline=False)
	           	await destination.send(embed=embed)
	async def on_help_command_error(self, error):
	       embed = discord.Embed(title="Error", description=error, colour=discord.Colour.light_grey())
	       destination = self.get_destination()
	       await destiation.send(embed=embed)

logging.basicConfig(level=logging.INFO)
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
class Bot(Bot):
	def __init__(self, command_prefix, **kwargs):
		super().__init__(command_prefix, **kwargs)
		self.config_token = secret_file['token']
		self.launch_time = datetime.utcnow()
		self.help_command = HelpCommand()
		self.owner_ids = {746807014658801704, 668906205799907348}
		self.version = "1.9.0"
		self.colour = discord.Colour.red()
		self.maintenence = False
		self.maint = False
		self.colors = Colors
		self.colours = self.colors
		self.log_channel = self.get_channel(789892435190349859)
		self.loop.create_task(handle_display())
		self.load_extension('jishaku')

		
	async def on_ready(self):
		log_channel = self.get_channel(789892435190349859)
		
		if log_channel:
		          embed = discord.Embed(
		          title=f"{self.user.name} is online!",
		          colour=discord.Colour.blurple()
		          )
		          embed.set_footer(text="Howdy' how ya'll doin'?",icon_url=self.user.avatar_url)
		          
		          await log_channel.send(embed=embed)

# The bot activities


activities = cycle(["Commands: !*help",
                    "{length} servers! | !*help",
                    "PacMan"])
display_messages = (
    ("Bot is now online!", ""),
    ("Logged in as:", "{bot.user}"),
    ("ID:", "{bot.user.id}"),
    ("Working on:", "{length} servers!"),
    ("My prefix is:", default_prefix),
    ("Discord.py version:", discord.__version__)
)


async def handle_display():
    await bot.wait_until_ready()
    # DEV: there were 30 spaces originally
    width, _ = os.get_terminal_size()
    border = "=" * width
    output = border.center(width)
    kwargs = {
        "bot": bot,
        "length": len(bot.guilds),
        "discord": discord
    }

    for group in display_messages:
        for i, message in enumerate(group):
            message = message.format(**kwargs)
            centered = message.center(width)
            end = "\n" if i == 0 else "\n\n"
            output += centered + end
    output += border.center(width)
    print(output)




@tasks.loop(minutes=2)
async def change_status():
    length = len(bot.guilds)
    name = str.format(next(activities), length=length)

    await self.change_presence(activity=discord.Game(name=name))

    
@tasks.loop(minutes=2)
async def change_nick(self, ctx):
	for guild in bot.guilds:
		await guild.me.edit(nick=f"[\"{ctx.prefix}\"] PacMe")


@change_nick.before_loop
async def before_change_status(self):
    await bot.wait_until_ready()

@change_status.before_loop
async def before_change_status(self):
    await bot.wait_until_ready()

change_status.start()
change_nick.start()

# running the bot.

if __name__ == '__main__':
	bot = Bot(command_prefix=get_prefix, intents=discord.Intents.all(), case_insensitive=True, fetch_offline_memberd=True)
	for file in os.listdir(cwd+"/cogs"):
		if file.endswith(".py") and not file.startswith('_'):
			os.environ["JISHAKU_NO_UNDERSCORE"] = "False"
			os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
			os.environ["JISHAKU_HIDE"] = "False"
			bot.load_extension(f"cogs.{file[:-3]}")
	bot.run(bot.config_token)