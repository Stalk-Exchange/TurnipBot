#turnipbot.py
import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("Bot Started")
	
@bot.command(name='buy', help='Lets users know what the price your turnips are being bought for, and sets up a queue')
async def sell_start(ctx):
	args = str(ctx.message.content.lower()).split()
	if len(args) != 4:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a buy command is `.buy [Bell Price] [Town Name] [Dodo Code]`. Please try again with the needed information!")
	elif not str(args[1]).isdigit() or len(args[3]) != 5:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a buy command is `.buy [Bell Price] [Town Name] [Dodo Code]`. Please try again with the needed information!")
	else:
		response = "Nook's Cranny is buying turnips for `" + args[1] + " Bells` on " + args[2] +"! Join the queue with `.join [queue_id]`"
		buy_channel = bot.get_channel(int(os.getenv('BUY_CHANNEL')))
		await buy_channel.send(response)
		
@bot.command(name='sell', help='Lets users know what the price your turnips are being sold for, and sets up a queue')
async def sell_start(ctx):
	args = str(ctx.message.content.lower()).split()
	if len(args) != 4:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a sell command is `.sell [Bell Price] [Town Name] [Dodo Code]`. Please try again with the needed information!")
	elif not str(args[1]).isdigit() or len(args[3]) != 5:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a sell command is `.sell [Bell Price] [Town Name] [Dodo Code]`. Please try again with the needed information!")
	else:
		response = "Joan is selling turnips for `" + args[1] + " Bells` on " + args[2] +"! Join the queue with `.join [queue_id]`"
		sell_channel = bot.get_channel(int(os.getenv('SELL_CHANNEL')))
		await sell_channel.send(response)
		


bot.run(TOKEN)