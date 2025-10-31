'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
import animal

class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []


    def get_animals(self):
        return self.__animals

    def print_animals(self):
        print('--- Zoo Animals ---')
        if len(self.__animals) > 0:
            for a in self.get_animals():
                print(f"{a}\n")
        else:
            print("Matt Damon would be disappointed, you need animals in "
                  "your zoo!")

    def add_animal(self, name):
        self.__animals.append(name)

    def remove_animal(self, name):
        self.__animals.remove(name)

    def add_enclosure(self, name):
        self.__enclosures.append(name)

    def remove_enclosure(self, name):
        self.__enclosures.remove(name)

    def assign_animal(self, enclosure, animal):
        enclosure.add_occupant(animal)

# assign_animal
# unassign_animal
#
# move_animal
#     validation = does it have any pending cases that check box cant be moved


# add_staff
# remove_staff
#

#
#
# daily_routines
#       list of routines = taking a staff and one of their tasks and storing it

#

#

#
#
# def enclosure_breach
#
#
# def sanitation_protocol
#
#
#
# def visitor_overboard