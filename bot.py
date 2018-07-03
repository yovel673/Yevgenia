#Yevgenia bot by Baba Ganush and volteezer
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime

bot = commands.Bot(command_prefix = "!")
bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(game = discord.Game(name = "Shotek!"))
	print("Ready when you are!")
	print("i am runnig on " + bot.user.name)
	print("with the ID " + bot.user.id)
	
@bot.event
async def on_message(message):
	now = datetime.datetime.now()
	date = ("{}:{}:{} {}/{}/{}".format(str(now.hour), str(now.minute), str(now.second), str(now.day),str(now.month), str(now.year)))
	author = message.author
	content = message.content
	print("{} said : ' {} ' at {}".format(author, content, date))
	await bot.process_commands(message)
	#now.year, now.month, now.day, now.hour, now.minute, now.second
	
@bot.command(pass_context = True)	
async def ping(ctx):
	await bot.say(":ping_pong: Good morning everybody!")
	print("User has pinged")
	
@bot.command(pass_context = True)
async def help():
	await bot.say("This is yevgnia bot 0.1v alpha!")
	
@bot.command(pass_context = True)
async def release_date():
	await bot.say("Full version is expected at the end of july")
	
@bot.command(pass_context = True)
async def credits():
	await bot.say("The developer of the bot is baba ganush")
	
@bot.command(pass_context = True)
async def ganush():
	await bot.say("B-Ba-Bab-Baba GANUSH")
	
@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
	await bot.say("The username is: {}".format(user.name))
	await bot.say("The user ID is: {}".format(user.id))
	await bot.say("The users status is: {}".format(user.status))
	await bot.say("The users highest role is: {}".format(user.top_role))
	await bot.say("The user joined at: {}".format(user.joined_at))
  
@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)

	
	
bot.run("NDYzNzI1NDA0NDgyNDM3MTIw.Dh0leg.0ph59wCXYsnHR73vQkE1IaqkPRU")