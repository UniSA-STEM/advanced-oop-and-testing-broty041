'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, name):
        self.__name = name

    # Getters / Setters
    def get_name(self):
        return self.__name

    name = property(get_name)

    @abstractmethod
    def generate_report(self):
        pass


class DailyRoutines(Report):
    def __init__(self, name):
        super().__init__(name)

    def generate_report(self, zoo):
        """
        Generates a readable daily routine report.

        Iterates over zoo operations daily_routine dictionary. Each day
        maps to a list of tuples, each tuple is the staff member
         (object) and their task (object), calls .name property of each.
        """
        print("\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-\n"
              "-=-=- Welcome to the Daily Routine Report -=-=-"
              "\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")

        for day, routine in zoo.daily.items():
            if routine:
                routine_formatted = " || ".join(
                    f"{staff.name}, {task.name}"
                    for staff, task_list in routine
                    for task in (task_list if isinstance(task_list, list)
                                 else [task_list])
                )
            else:
                routine_formatted = ""

            print(f"{day}: {routine_formatted}")


    def __repr__(self):
        return f"{self.name}"



class AnimalsBySpecies(Report):
    def __init__(self, name):
        super().__init__(name)

    def generate_report(self, zoo):
        for o in zoo.animals

# list of anmials by species

# status of all enclosures


