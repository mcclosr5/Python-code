class Time(object):
    def __init__(self, h=0, m=0, s=0):
    	self.hour = h
    	self.minute = m
    	self.second = s
    def __str__(self):
    	return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

    @classmethod
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        days, hour = divmod(hour, 24)
        return cls(hour, minute, second)