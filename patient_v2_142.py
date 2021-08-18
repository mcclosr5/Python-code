#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = ', '.join(meds)

    def add_medication(medication):
        self.meds = self.meds.append(medication)

    def __str__(self):
        return 'Name: {}\nAge: {}\nMedications: {}\nDoctor: {}'.format(self.name, self.age, self.meds, self.doctor)
