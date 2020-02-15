import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='y!')


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello World')


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def yoda(ctx, user=None):
    if user == None:
        await ctx.send('Mauvaise utilisation de la commande. Syntaxe correcte : y!yoda @user')
    else:
        await ctx.send(f'Je suis la voix de la raison, respecter mes décissions tu dois {user}')


bot.run('Njc3ODI0MDE0ODQ0MDM1MDc0.XkhnYw.vZlvtPv4InhRvDEvQuzt3f1VuIw');
