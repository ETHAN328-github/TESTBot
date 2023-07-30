import discord
from discord.ext import commands
import json
import os
import random








with open('setting.json', 'r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='[', intents = intents)
client = discord.Client(intents = intents)



@bot.event
async def on_ready():
    print(">>Bot is online<<")













@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded{extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded{extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded{extension} done.')









#嵌入訊息
@bot.command()
async def em(ctx):
        embed=discord.Embed(title="佳奈小蘇打清潔劑", url="https://ichigoproduction.com/news/index00700000.html", description="如果和她一樣愛舔小蘇打 請支持佳奈小蘇打清潔劑", color=0x93343d)
        embed.set_thumbnail(url="https://truth.bahamut.com.tw/s01/202304/126982cc1cac6cd121166ec836e43928.JPG")
        embed.add_field(name="#我推的孩子", value="", inline=False)
        embed.add_field(name="#有馬佳奈", value="", inline=False)
        embed.add_field(name="#愛舔小蘇打粉的天才童星", value="", inline=False)
        await ctx.send(embed=embed)


#報延遲
@bot.command()
async def ping(ctx):
        await ctx.send(f'{round(bot.latency*1000)}(ms)')









#隨機圖片
@bot.command()
async def 圖片(ctx):
       random_pic = random.choice(jdata['pic'])
       pic = discord.File(random_pic)
       await ctx.send(file = pic)

#網址圖片
@bot.command()
async def web(ctx):
       random_pic = random.choice(jdata['url_pic'])
       await ctx.send(random_pic)


@bot.command()
async def  __init__(self, bot):
    self.bot = bot



@bot.command()
async def on_message(self, msg):
    keyword = ['a', 'b', 'c', 'd']
    if msg.content in keyword and msg.auther != self.bot.user: 
      await msg.channel.send('hi')







for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
         bot.load_extension(f'cmds.{filename[:-3]}')


if __name__=="__main__":
    bot.run(jdata['TOKEN'])