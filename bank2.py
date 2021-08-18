#!/usr/bin/env python


class Account(object):
    # A class variable
    irate = 10.0
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        # self.irate = 2.0
    
    def apply_interest(self):
        self.balance += self.balance * self.irate / 100

    def __str__(self):
        return '{:s} : {:2f}'.format(self.name, self.balance)
