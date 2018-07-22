import discord
from discord.ext.commands import Bot
from discord.ext import commands 
import random

urls=["https://i.gifer.com/ITIU.gif","https://media1.tenor.com/images/1968a5fec63b574a0c592f355c86d87b/tenor.gif","https://steamusercontent-a.akamaihd.net/ugc/683775440076628184/6355191EE3E72FC2EDB773E531F34759D11B5A70/","https://ci.memecdn.com/3995999.gif","https://media1.tenor.com/images/54e1add302b9b4a19435e941e290309e/tenor.gif?itemid=9920849"]
class Help:

	
	def __init__(self, bot):
		self.bot=bot
		self.bot.remove_command('help')
		
	
	
	@commands.command(aliases='h',pass_context=True)
	async def help(self,ctx):
	
	
		embed = discord.Embed(title="Godly-Bot", description="List of commands are:", color=0xeee657)
		embed.add_field(name="b!8ball", value="Answers a question in degrees of yes/no", inline=False)
		embed.add_field(name="b!bitcoin|btc", value="Shows the currentprice of Bitcoin(BTC)", inline=False)
		embed.add_field(name="b!hangman|hang", value="Guess a 6 lettered word", inline=False)
		embed.add_field(name="b!anime <anime name>",value="Search for an anime and get it's Synopsis",inline=False)
		embed.add_field(name="b!help|h",value="view the commands",inline=False)
		embed.add_field(name="b!info",value="show the info about the bot",inline=False)
		embed.set_thumbnail(url="https://botlist.co/images/placeholder/BotList-icon-color.jpg")
    
		await self.bot.say(embed=embed)





	
	@commands.command(pass_context=True)
	async def info(self,ctx):
	
		serv=ctx.message.server
		me=serv.get_member_named("godlydevil#4467")
		embed = discord.Embed(title="Godly-Bot", description="A bot made for Anime Party", color=0xeee657)
		# give info about you here 
		embed.add_field(name="Author", value=me.mention)
		embed.set_thumbnail(url="https://botlist.co/images/placeholder/BotList-icon-color.jpg")
		embed.add_field(name="Invite",value="https://discordapp.com/oauth2/authorize?bot_id=468722927689269251&scope=bot",inline=False)
   
		await self.bot.say(embed=embed)
	
	@commands.command(pass_context=True)
	async def rawr(self,ctx):
		self.urls=urls
		auth=ctx.message.author
		embed=discord.Embed(title='Rawr',description=auth.mention+' Rawred!',colour=0xFFFFFF)
		s=random.choice(urls)
		embed.set_image(url=s)
		await self.bot.say(embed=embed)
		
	
		
def setup(bot):
	bot.add_cog(Help(bot))
		
