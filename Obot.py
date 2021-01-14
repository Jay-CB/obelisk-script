import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import time
import random
import os

os.system("clear")

client = discord.Client()

cooldown_str = ("**Vote Bot:** ","**Vote Server:** ","**Daily:** ","**Hunt:** ","**Gathering:** ","**Rob:** ","**Passive Mode:** ","**Dungeon:** ","**New Quest:** ")

user = []
admin_user = []
cooldowns = []
hunt_time = 0.0
gather_time = 0.0
macro_bool = False
h_toggle = True
g_toggle = True

@client.event
async def on_connect():
	print("[{}] -- Connected".format(datetime.now().strftime("%H:%M:%S")))

@client.event
async def on_disconnect():
	print("[{}] -- Disconnected".format(datetime.now().strftime("%H:%M:%S")))

@client.event
async def on_resumed():
	print("[{}] -- Resumed".format(datetime.now().strftime("%H:%M:%S")))

@client.event
async def on_ready():
	global user
	print("[{}] -- Ready".format(datetime.now().strftime("%H:%M:%S")))
	user = client.get_user(735090182893862954)
	admin_user = client.get_user(79633511456062141)
	if not loop.is_running():
		loop.start()

@client.event
async def on_message(message):
	global user
	global admin_user
	global cooldowns
	global macro_bool
	global h_toggle
	global g_toggle
	if user and message.author.id == user.id and message.channel.id == 795331394956034048:
		time.sleep(0.5)
		if message.embeds and message.embeds[0].description != discord.Embed.Empty:
			if (message.embeds[0].description).startswith("Please react this message"):
				macro_bool = True
				print("[{}] Macro Detection - Solving ".format(datetime.now().strftime("%H:%M:%S")),end="")
				emote_str = (message.embeds[0].description).replace("Please react this message with the following emoji to unlock the command: ","")
				time.sleep(6)
				await message.add_reaction(emote_str)
				time.sleep(1)
				macro_bool = False
				print("Solved")
			elif (message.embeds[0].description).startswith("**Vote Bot:**"):
				cooldowns = (message.embeds[0].description).split("\n")
				for i in range(len(cooldowns)):
					cooldowns[i] = cooldowns[i].replace(cooldown_str[i], "").replace("Ready", "0s")
					format_str = ""
					if "h" in cooldowns[i]:
						format_str += " %Hh"
					if "m" in cooldowns[i]:
						format_str += " %Mm"
					if "s" in cooldowns[i]:
						format_str += " %Ss"
					cooldowns[i] = datetime.strptime(cooldowns[i], format_str[1:])
					cooldowns[i] = datetime.now() + timedelta(seconds=cooldowns[i].second + 5, minutes=cooldowns[i].minute, hours=cooldowns[i].hour)

				print("""[{}] Cooldowns:
           Vote:	{}
           Daily:	{}
           Quest:	{}""".format(datetime.now().strftime("%H:%M:%S"),cooldowns[0].strftime("%H:%M:%S"),cooldowns[2].strftime("%H:%M:%S"),cooldowns[8].strftime("%H:%M:%S")))
	elif admin_user and message.author.id == admin_user.id:
		admin_message = (message.content).lower()
		print("[{}] Command Recieved - {}".format(datetime.now().strftime("%H:%M:%S"),admin_message))
		if admin_message == "stop loop":
			if loop.is_running():
				loop.stop()
			else:
				print("           Loop is not running")
		elif admin_message == "start loop":
			if not loop.is_running():
				loop.start()
			else:
				print("           Loop is running")
		elif admin_message == "ping":
			await admin_user.send("Pong")
		elif admin_message == "toggle h":
			h_toggle = not h_toggle
		elif admin_message == "toggle g":
			g_toggle = not g_toggle
	elif message.content == ".login":
		print("[{}] User Login - {}".format(datetime.now().strftime("%H:%M:%S"),message.author.name))
		admin_user = message.author
		await admin_user.send("Welcome Boss")

@tasks.loop(seconds=3)
async def loop():
	global user
	global hunt_time
	global gather_time
	global macro_bool
	now = time.time()
	if macro_bool == True:
		print(".. ",end="")
	elif not cooldowns:
		await user.send(".cd")
	elif now > hunt_time + random.randrange(65,70) and h_toggle:
		await user.send(".h")
		hunt_time = time.time()
	elif now > gather_time + random.randrange(125,130) and g_toggle:
		await user.send(".g")
		gather_time = time.time()
	elif datetime.now() > cooldowns[8]:
		await user.send(".q new")
		cooldowns[8] = datetime.now() + timedelta(minutes=5, hours=6)
		print("[{}] New Quest".format(datetime.now().strftime("%H:%M:%S")))
	elif datetime.now() > cooldowns[2]:
		await user.send(".daily")
		cooldowns[2] = datetime.now()+ timedelta(minutes=5, hours=24)
		print("[{}] Daily".format(datetime.now().strftime("%H:%M:%S")))

@loop.before_loop
async def before_loop():
	print("[{}] -- Loop Start".format(datetime.now().strftime("%H:%M:%S")))
	await client.wait_until_ready()

@loop.after_loop
async def after_loop():
	print("[{}] -- Loop Stop".format(datetime.now().strftime("%H:%M:%S")))

client.run("")