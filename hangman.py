import discord
from discord.ext.commands import Bot 
from discord.ext import commands 
import time
import random

class Hangman:
	def __init__(self, bot):
		self.bot=bot
		
	@commands.command(aliases=["hang"],pass_context=True,)
	async def hangman(self,ctx,member: discord.Member=None):

		auth=ctx.message.author
		ch=ctx.message.channel
	
		await self.bot.say("Hello,time to play Hangman")
	
		time.sleep(1)
	
	
		words=["puzzle","bombed","hunter","jackal","jumped","gamble","hijack","hentai","lizard","secret"]
		time.sleep(0.5)
	
		word=random.choice(words)
		guesses=''
		turns=10
		god=''
	
		while turns > 0:
		
			failed=0
		
			for char in word:
			
			
		
				if char in guesses:
			
				
					god+=char
				else:
					god+=' _'
					failed+=1
			await self.bot.say((god))
			god=' '
				
			if (failed==0):
				await self.bot.say("You won")
				break
			
			await self.bot.say("Start guessing" + auth.mention)
		
			tr= await self.bot.wait_for_message(author=auth,channel=ch)
			guess=tr.content
		
			guesses+=guess
		
			if guess not in word:
			
				turns-=1
				t=str(turns)
				await self.bot.say("Wrong")
			
				await self.bot.say("You have " + t +" turns left")
			
				if (turns==0):
				
					await self.bot.say("You Lose")
					
						
				
		
	
		
def setup(bot):
	bot.add_cog(Hangman(bot))
