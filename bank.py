#!/usr/bin/env python3

class Account(object):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def lodge(self, euros):
        self.balance += euros


    def withdraw(self, euros):
        self.balance -= euros

    def __str__(self):
        return '{:s} : {:2f}'.format(self.name, self.balance)

    