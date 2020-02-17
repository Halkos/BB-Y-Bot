import discord

class Account:

    def __init__(self, user : discord.User, id : discord.ClientUser.id):
        self.__user = user
        self.__id = id
        self.__balance = 0

    def addMoney(self, add):
        self._balance += add

    @property
    def balance(self):
        self.__balance += 10 #Used for testing only
        return self.__balance

    @balance.setter
    def balance(self, money):
        if isinstance(money, int):
            self.__balance += money
