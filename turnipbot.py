#turnipbot.py
import os
import discord
import turnipqueue
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	turnipqueue.startup()
	
##Host commands
@bot.command(name='buy', help='Lets users know what the price your turnips are being bought for, and sets up a queue')
async def buy_create(ctx):
	args = str(ctx.message.content.lower()).split()
	if len(args) != 3:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a buy command is `.buy [Bell Price] [Town Name]`. Please try again with the needed information!")
	else:
		response = turnipqueue.buy_queue(ctx)
		buy_channel = bot.get_channel(int(os.getenv('BUY_CHANNEL')))
		await buy_channel.send(response[0])
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send(response[1])
		
@bot.command(name='sell', help='Lets users know what the price your turnips are being sold for, and sets up a queue')
async def sell_create(ctx):
	args = str(ctx.message.content.lower()).split()
	if len(args) != 3:
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder: the formatting for a sell command is `.sell [Bell Price] [Town Name]`. Please try again with the needed information!")
	else:
		response = turnipqueue.sell_queue(ctx)
		sell_channel = bot.get_channel(int(os.getenv('SELL_CHANNEL')))
		await sell_channel.send(response[0])
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send(response[1])

@bot.command(name='dodo', help='Opens the queue with your Dodo code')
async def queue_open(ctx):
	if str(ctx.message.channel.type) == 'private':
		response = turnipqueue.open_queue(ctx)
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Your queue is opened! Feel free to leave the switch running, just keep an eye out for errors to ensure a smooth process. Type `.close` when you're finished, or `.next` to force the Dodo code to be sent to the next person in queue.")
	else: #code put in public channel
		await ctx.author.create_dm()
		await ctx.author.dm_channel.send("Hey, just a reminder that you should only send your Dodo code through a direct message. We see that you sent it through the public command chat, opening the island for everyone. We suggest that you close and reopen your island and try again. The queue has not been officially opened for now, so don't worry!")
		
@bot.command(name='close', help='Closes your current queue, if one is opened')
async def queue_close(ctx):
	response = turnipqueue.close_queue(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("Your queue has been closed. Feel free to close your island. Thank you for your time!")
	#send notifictions to users in queue

@bot.command(name='next', help='Forces the dodo code to the next person in queue')
async def next_queue(ctx):
	turnipqueue.next_queue(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("Dodo code sent to next user")
	
@bot.command(name='count', help='Returns the count in your current queue')
async def count_queue(ctx):
	count = turnipqueue.count_queue(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("The current number of users in queue is: `" + count+"`")

##Visitor commands
@bot.command(name='join', help='Joins a specific queue')
async def join_queue(ctx):
	turnipqueue.visitor_join(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("You've joined the queue! We'll let you know if there are any issues.")
	
@bot.command(name='leave', help='Leaves the currnet queue, and if it is your turn, lets the next person in.')
async def leave_queue(ctx):
	turnipqueue.visitor_leave(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("Thank you for waiting, see you again soon.")
	
@bot.command(name='numq', help="Returns the position in queue of the user.")
async def queue_position(ctx):
	position = turnipqueue.visitor_count(ctx)
	await ctx.author.create_dm()
	await ctx.author.dm_channel.send("Your position is `" + position + "` in line")
	
bot.run(TOKEN)