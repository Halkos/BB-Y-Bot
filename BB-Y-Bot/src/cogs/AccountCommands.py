import json

from discord.ext import commands

from Account import Account


class AccountCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        account = Account(member, member.id)
        with open('/Users/florianbriquet/Documents/BB-Y-Bot/BB-Y-Bot/misc/account.json', 'r') as f:
            users_account = json.load(f)

        await self.update_data(users_account, member)

        with open('/Users/florianbriquet/Documents/BB-Y-Bot/BB-Y-Bot/misc/account.json', 'w') as f:
            json.dump(users_account, indent=4)

        await ctx.send(f"Bienvenu {ctx.message.author.mention}")
        await ctx.send(
            f"Nouveau compte créé pour l'utilisateur : {ctx.message.author} avec l'id : {ctx.message.author.id}")
        await ctx.send(f"Le compte possède {account.balance} Zemid")

    async def update_data(self, users, user):
        if users.get(str(user.id)) is None:
            print('test')
            users[str(user.id)] = {}
            users[str(user.id)]["Account_owner"] = str(user)
            users[str(user.id)]["Balance"] = 15

    async def add_money(self, users, user, money):
        users[str(user.id)]["Balance"] += money

    async def get_balance(self, ctx, users, user):
        await ctx.send(users[str(user.id)]["Balance"])

    @commands.command()
    async def seeBalance(self, ctx):
        with open('/Users/florianbriquet/Documents/BB-Y-Bot/BB-Y-Bot/misc/account.json', 'r') as f:
            users_account = json.load(f)

        await self.update_data(users_account, ctx.message.author)
        await self.get_balance(ctx, users_account, ctx.message.author)
        await self.add_money(users_account, ctx.message.author, 10)
        await self.get_balance(ctx, users_account, ctx.message.author)

        with open('/Users/florianbriquet/Documents/BB-Y-Bot/BB-Y-Bot/misc/account.json', 'w') as f:
            json.dump(users_account, f, indent=4)


def setup(bot):
    bot.add_cog(AccountCommands(bot))
