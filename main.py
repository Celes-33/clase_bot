import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('@bot/memes'))
    with open(f'@bot/memes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    img_name = random.choice(os.listdir('@bot/animales'))
    with open(f'@bot/animales/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 

@bot.command()
async def enamorada(ctx):
    img_name = random.choice(os.listdir('@bot/enamorada'))
    with open(f'@bot/enamorada/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 

bot.run("Token")