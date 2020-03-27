def startup():
	print("Bot Started")
	
def buy_queue(ctx): #Returns 
	args = str(ctx.message.content.lower()).split()
	response = [0,0]
	response[0] = "Nook's Cranny is buying turnips for `" + args[1] + " Bells` on `" + args[2] +"`! Join the queue with `.join [queue_id]`"
	response[1] = "Please reply with your DoDo Code when you're ready to open your island! DM me the command `.dodo` with your dodo code to start!"
	return response
	
def sell_queue(ctx):
	args = str(ctx.message.content.lower()).split()
	response = [0,0]
	response[0] = "Joan is selling turnips for `" + args[1] + " Bells` on `" + args[2] +"`! Join the queue with `.join [queue_id]`"
	response[1] = "Please reply with your DoDo Code when you're ready to open your island! DM me the command `.dodo` with your dodo code to start!"
	return response
	
def open_queue(ctx):
	#put response in proper channel
	return "response"
	
def close_queue(ctx):
	#put response in proper channel
	return "response"
	
def next_queue(ctx):
	print("Next Queue")
	
def count_queue(ctx):
	return "position"
	
def visitor_join(ctx):
	print("Visitor join")
	
def visitor_leave(ctx):
	print("Visitor leave")
	
def visitor_count(ctx):
	return "count"