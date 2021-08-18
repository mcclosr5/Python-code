#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def __str__(self):
        return 'Name: {}\nAge: {}\nMedications: {}\nDoctor: {}'.format(self.name, self.age, self.meds, self.doctor)

class Ward(Patient):

    def __init__(self):
        self.d = {}

    def add(self, p1):
        self.d[p1.name] = p1

    def lookup(self, p1):
        try:
            return self.d[p1]
        except:
            return None

    def remove(self, p1):
        del self.d[p1]

    def get_patients_by_medication(self, med):
    	if self.med not in patient_list:
    		del self.d[p1]
