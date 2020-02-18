import discord
import os
from discord.ext import commands

from Utils import Utils

bot = commands.Bot(command_prefix='y!')


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello World')


@bot.command()
async def yoda(ctx, user=None):
    if user == None:
        await ctx.send('Mauvaise utilisation de la commande. Syntaxe correcte : y!yoda @user')
    else:
        await ctx.send(f'Je suis la voix de la raison, respecter mes décissions tu dois {user}')


@bot.command()
async def clear(ctx, amount=None):
    amount = Utils.try_convert(amount, int)
    check_amount = lambda x: amount if isinstance(amount, int) else (2 if amount == "type" else -1)
    if check_amount(amount) == -1:
        await ctx.send("La valeur que vous avez entrée n'est pas valable !")
    else:
        await ctx.channel.purge(limit=check_amount(amount))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('Njc3ODI0MDE0ODQ0MDM1MDc0.Xkn_jQ.b6iZbT93V-liESsCMI_aqePlXSw')
