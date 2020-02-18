import discord
import json

class Account:

    def __init__(self, user: discord.User, id: discord.ClientUser.id):
        self.user = user
        self.id = id
        self.__balance = 0

        
    @property
    def balance(self):
        pass

    @balance.setter
    def balance(self, money):
        if isinstance(money, int):
            self.__balance += money
