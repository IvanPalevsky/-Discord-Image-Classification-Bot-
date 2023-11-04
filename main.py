import discord
import os
from discord.ext import commands
from random import choice
import requests
from settings import TOKEN
from cl_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user} и я помогу вам следить за экологией!')
    await ctx.send("Чтобы держать мир в чистоте нужно соблюдать очень простые правила!")
    await ctx.send("Введите команду $garbage, чтобы увидеть картинки свалок и мусора.")

@bot.command()
async def nature(ctx):
    await ctx.send('Как спасти природу: 8 шагов, которые может сделать каждый:')
    await ctx.send('1.ЭКОНОМЬТЕ РЕСУРСЫ')
    await ctx.send('2.РАЗДЕЛЯЙТЕ МУСОР')
    await ctx.send('3.СДАВАЙТЕ ВТОРСЫРЬЁ')
    await ctx.send('4.ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ')
    await ctx.send('5.ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ')
    await ctx.send('6.ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ')
    await ctx.send('7.ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ')
    await ctx.send('8.ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА')

@bot.command()
async def garbage(ctx):
    with open('images1/garbage2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('"Введите команду $nature, чтобы получить информацию.')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck возвращает фото утки'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def chek(ctx):
    if ctx.message.attachments:
       for attachment in ctx.message.attachments:
           file_name = attachment.filename
           file_url = attachment.url
           image_path = (f'images1/{file_name}')
           await attachment.save(image_path)
           await ctx.send(get_class(model_path='model/keras_model.h5', labels_path='model/labels.txt', image_path = image_path)) 
           print('Картинка сохранилась') 
           os.remove(image_path)
           print('Картинка удалилась')
    else:
        await  ctx.send('Вы забыли загрузить картинку')



bot.run(TOKEN)