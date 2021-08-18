#!/usr/bin/env python


class Account(object):
    # A class variable
    irate = 10.0
    next_account_number = 1
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = self.next_account_number 
        Account.next_account_number += 1

    
    def apply_interest(self):
        self.balance += self.balance * self.irate / 100

    def __str__(self):
        return '{:s} : {:d} : {:2f}'.format(self.name, self.account_number, self.balance)
