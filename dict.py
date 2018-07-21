import discord
from discord.ext.commands import Bot
from discord.ext import commands




dic= {"itai!" : "it hurts!",
"chan" : "honorifics used in Japan, but most weebs don't know how to use them correctly",
"nya" : "meow",
"wan" : "woof",
"senpai" : "a senior colleague (Ie. A high school junior is a sophmore's senpai)",
"otaku" : "someone obsessed with something. Weebs often think it's specific to anime fans, but there's military otaku, robot otaku, train otaku, etc.",
"manga" : "comics",
"anime" : "cartoons (but if you ever call anime cartoons in front of a weeaboo, they'll go on for hours about how it's not cartoons. They are.)",
"shoujo" : "literally 'girl', but refers to a genre of anime/manga directed towards a female audience. Typically romantic and cheesy. ",
"shounen" : "literally 'boy', but refers to manga/anime directed towards a male audience. Typically about fighting. DBZ is a classic example.",
"hentai" : "literally pervert, but also refers to pornographic anime. ",
"ecchi" : "perverted stuff, such as panty shots, unrealistically back-breaking boobs and jiggle physics. However, this does not include actual sex.",
"doujinshi" : "an amateur's manga that isn't widely popular; often refers to fan-made manga.",
"yuri" : "girl love, lesbian stuff. Features: lots of boobs. I just figured that a majority of Imgur would appreciate that.",
"yaoi" : "boy love, gay stuff. My personal favorite genre for reasons. Lots of meat scepters.",
"mahou" : "magic",
"kuma" : "bear",
"usagi" : "bunny",
"seiyuu" : "voice actor/actress",
"bishoujo" : "cute young girl",
"bishounen" : "slender young man",
"loli" : "an underage girl, often described as cute and innocent",
"shota" : "an underaged boy, also called cute ",
"lolicon" : "short for lolita complex, refers to art about lolis, usually pornographic. Can also be used to describe people who are into that shit.",
"shotacon" : "same as lolicon, but with young boys.",
"moe" : "used to describe aspects of shoujo, but often just used as another word for cute.",
"megane" : "glasses, also refers to glasses characters.",
"seinen" : "mature men",
"josei" : "mature women",
"tsundere" : "someone who expresses their love through violence/aggressive words. Often in denial of romantic feelings. Usually paired with the word 'baka.'",
"yandere" : "someone who loves their romantic interest so much that they are willing to kill anyone who gets close to them, and sometimes even themselves or the romantic interest.",
"hikikomori" : "a NEET (Not in Education, Emplyment, or Training)",
"waifu" : "not real (it's wife)",
"husbando" : "also not real (you get the picture)",
"onee-san" : "big sister",
"onii-chan" : "big brother",
"imouto" : "little sister",
"otouto" : "little brother",
"otou-san" : "father",
"okaa-san" : "mother ",
"oji-san" : "literally uncle, but can refer to older guys in general", 
"oba-san" : "literally aunt, but can refer to older women in general ",
"yatta!" : "hooray!/I did it! ",
"shinigami" : "death god ",
"2chan" : "the 4chan of Japan",
"romaji" : "Japanese words in roman text (Ie. all the words on this list)",
"arigatou" : "thank you ",
"sumimasen" : "excuse me/sorry", 
"gomenasai" : "sorry", 
"suki" : "I like you", 
"daisuki" : "I really like you ",
"hontou?" : "really?",
"oishii" : "delicious",
"kawaii":"Cute"}	
class Dictionary:

	 
	
	
	
	def __init__(self, bot):
		self.bot=bot
		
	@commands.command()
	async def dict(self,term):
		
		self.dic=dic
		if term in dic:
			embed=discord.Embed(title=" dictionary",description=dic.get(term))
			embed.set_thumbnail(url="https://botlist.co/images/placeholder/BotList-icon-color.jpg")
			await self.bot.say(embed=embed)
			
		else:
			embed=discord.Embed(title=" dictionary",description="Not found.That is not a  word")
			embed.set_thumbnail(url="https://botlist.co/images/placeholder/BotList-icon-color.jpg")
			await self.bot.say(embed=embed)
		
			
		
def setup(bot):
	bot.add_cog(Dictionary(bot))
