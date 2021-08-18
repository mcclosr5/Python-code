#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def add_medication(self, medication):
        #Add the medication to list med
        self.meds.append(medication)

    def __str__(self):
        return 'Name: {}\nAge: {}\nMedications: {}\nDoctor: {}'.format(self.name, self.age, ', '.join(self.meds), self.doctor)
