import json
import os
from datetime import datetime
from itertools import cycle

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

default_prefix = "!*"

f = "./prefixes.json"
mr = 'r'
mw = 'w'

def get_prefix(bot, ctx):
	with open(f, mr) as fl:
		prefixes = json.load(fl)
		
	return prefixes.get(str(ctx.guild.id), default_prefix)

color = discord.Colour.green()
bot = commands.Bot(command_prefix = get_prefix, fetch_offline_members = True, case_insensitive=True, intents=discord.Intents.all())
bot.remove_command('help')
bot.launch_time = datetime.utcnow()

bot.owner_ids = {746807014658801704, 668906205799907348}

bot.version = "1.1.0"

bot.colour = discord.Colour.red()

status = cycle(['Commands: !*help', f'{len(bot.guilds)} servers! | !*help', 'PacMan'])		
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    change_status.start()
    print ('                              ================================================')
    print ('                                            Bot is now online!')
    print ('')
    print ('                                            Logged in as:')
    print ('                                            {0.user}'.format(bot))
    print('')
    print ('                                            ID:')
    print (f'                                            {bot.user.id}')
    print ('')
    print ('                                            Working on:')
    print (f'                                            {len(bot.guilds)} servers!')
    print('')
    print ('                                            My prefix is:')
    print (f'                                            !*')
    print('')
    print('                                            Version:')
    print(f"                                             {discord.__version__}")
    print ('                              ================================================')  
    log_channel = bot.get_channel(789892435190349859)
    embed = discord.Embed(
    colour = discord.Colour.blurple(),
    title = f"{bot.user.name} Is online!")
    embed.set_footer(text="Howdy' how ya'll doin'?", icon_url=bot.user.avatar_url)
    await log_channel.send(embed=embed)
    class colors:
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

@tasks.loop(seconds=10)
async def change_status():
	  await bot.change_presence(activity=discord.Game(next(status)))
	        	
@bot.command(aliases=["src"])
async def source(ctx):
	embed = discord.Embed(colour = discord.Colour.blurple(), title = "Heres the source!", description="[Here!](https://github.com/FrostiiWeeb/PacMeSource/)")
	embed.add_field(name="Leave a star, if u use my code!", value="Enjoy!")
	await ctx.send(embed=embed)

@bot.command(aliases=['r'])
@commands.is_owner()
async def restart(ctx):
	log_channel = bot.get_channel(789892435190349859)        	   
	embed = discord.Embed(
	colour = discord.Colour.blurple(),
	title = f"{bot.user.name} Restarting!"
	)    
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.set_footer(text="Howdy! Ill be restarting in a few seconds.", icon_url=bot.user.avatar_url)	  
	await log_channel.send(embed=embed)
	await ctx.send(embed=embed)
	await ctx.bot.logout()

@bot.command(aliases=['cl'])
async def changelog(ctx):
	embed = discord.Embed(
	colour = bot.colour,
	title = "**Changelog:**",
	description=f"```Added type racer command.```\n```Added Fun Cog.```"
	)
	await ctx.send(embed=embed)

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"
        	    						    						
        	    						     						
bot.load_extension('jishaku')   	    	    
	   	                                 
for filename in os.listdir('./cogs'):
  if filename.endswith('.py') and not filename.startswith('_'):
    bot.load_extension(f'cogs.{filename[:-3]}')

    
load_dotenv()
token = os.getenv('DISCORD_TOKEN')      
bot.run(token)
