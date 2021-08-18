#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def add_time(self, sport, time):
        if sport == 'cycle':
            self.cycle = time
        if sport == 'swim':
            self.swim = time
        if sport == 'run':
            self.run = time

    def get_time(self, sport):
        if sport == 'cycle':
            return self.cycle
        if sport == 'swim':
            return self.swim
        if sport == 'run':
            return self.run

    def __eq__(self, other):
        return self.run + self.cycle + self.swim == other.run + other.swim + other.cycle

    def __gt__(self, other):
        return self.run + self.cycle + self.swim > other.run + other.swim + other.cycle

    def __str__(self):
        l = []
        l.append("Name: {}".format(self.name))
        l.append("ID: {}".format(self.tid))
        l.append("Race time: {}".format(self.run + self.cycle + self.swim))
        return "\n".join(l)

class Triathlon(Triathlete):

    def __init__(self):
        self.d = {}

    def add(self, t1):
        self.d[t1.tid] = t1

    def lookup(self, t1):
        try:
            return self.d[t1]
        except:
            return None

    def remove(self, t1):
        del self.d[t1]
