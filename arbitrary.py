import discord
from discord.ext.commands import Bot 
from discord.ext import commands 
import aiohttp
import json
from discord import Game
import random


class Arbitrary:
	def __init__(self, bot):
		self.bot=bot
		
	@commands.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
	async def eight_ball(self,context):
		possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
		]
		await self.bot.say(":8ball:| "+random.choice(possible_responses) + ", " + context.message.author.mention)
		


	@commands.command()
	async def square(self,number):
		squared_value = int(number) * int(number)
		await self.bot.say(str(number) + " squared is " + str(squared_value))
		
	async def on_ready(self):
		await self.bot.change_presence(game=Game(name="with humans"))
		print("Logged in as " + self.bot.user.name)


	
	


	@commands.command()
	async def bitcoin(self,aliases='btc'):
		url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
		async with aiohttp.self.bot.saySession() as session:  # Async HTTP request
			raw_response = await session.get(url)
			response = await raw_response.text()
			response = json.loads(response)
			await self.bot.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
				
		
	
		
def setup(bot):
	bot.add_cog(Arbitrary(bot))
