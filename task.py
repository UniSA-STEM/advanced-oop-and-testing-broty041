'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, name, description):
        self.__name = name
        self.__description = description





class Feed(Task):
    def __init__(self, name, description):
        super().__init__(name, description)

    def action(self, enclosure):
        enclosure.feed_animals()







