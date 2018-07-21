import discord
from discord.ext.commands import Bot 
from discord.ext import commands
import requests
from bs4 import BeautifulSoup 


class MAL:
	def __init__(self, bot):
		self.bot=bot
		
	@commands.command()
	async def anime(self,arg1,*args):
	
	
		p="https://myanimelist.net/anime.php?q="
		
		title=arg1
	
		for arg in args:
			title+="%20"
			title+=arg
		s=p+title
	
		page=requests.get(s)
		soup=BeautifulSoup(page.text,'html.parser')
		res=soup.find('td',attrs={'class':'borderClass bgColor0'})
		var_link=res.find('a')['href']
		v=var_link
	
		page=requests.get(var_link)
		soup=BeautifulSoup(page.text,'html.parser')
		result=soup.find('span',attrs={'itemprop':'description'}).text
		res_2=soup.find('div',attrs={'style':'text-align: center;'})
		res_3=soup.find('span',attrs={'itemprop':'name'}).text
		res_4=soup.find('div',attrs={'class':"fl-l score"}).text
		imag=res_2.find('img')['src']
		embed=discord.Embed(title=res_3,description=result,colour=0xFFFFFF)
	
		embed.set_image(url=imag)
		embed.add_field(name="Score:",value=res_4)
		embed.add_field(name="Link to site",value=v)
		embed.set_footer(text="Sourced from MyAnimeList(MAL)", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9kgrRYpaVc53JFQ6iDuPN5eDMuTDFVr05ChTAg52_nEYMh1it")
	
		embed.set_thumbnail(url="https://botlist.co/images/placeholder/BotList-icon-color.jpg")
	
		await self.bot.say(embed=embed)
		
def setup(bot):
	bot.add_cog(MAL(bot))
