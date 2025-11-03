'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class HealthRecord(ABC):
    def __init__(self, name, description, record_type, date, severity_level, treatment_plan, notes):
        self.__name = name
        self.__description = description
        self.__record_type = record_type
        self.__date = date
        self.__severity_level = severity_level
        self.__treatment_plan = treatment_plan
        self.__notes = notes



# a health record impacts movable

# record_type
#     injury
#     illness
#     behavioural



def current_case
def case_history