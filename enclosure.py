'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:
    def __init__(self, size, environment, enclosure_class, max_occupancy, enclosure_status):
        self.__size = size
        self.__environment = environment
        self.__cleanliness = 10
        self.__enclosure_class = enclosure_class
        self.__max_occupancy = max_occupancy
        self.__enclosure_status = enclosure_status
        self.__occupants = []


    def get_occupants(self):
        return self.__occupants


    def add_occupant(self, name):
        self.__occupants.append(name)

    def remove_occupant(self, name):
        self.__occupants.remove(name)






