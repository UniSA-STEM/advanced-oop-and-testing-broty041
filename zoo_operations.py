'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__daily_routines = {"Monday": [],
                                 "Tuesday": [],
                                 "Wednesday": [],
                                 "Thursday": [],
                                 "Friday": []}

    # Getters and setters
    def get_animals(self):
        return self.__animals

    def get_daily_routines(self):
        return self.__daily_routines

    daily = property(get_daily_routines)


    # Animal Management
    def find_animal(self, animal):
        """
        Find an animal with either a string or object as a parameter.
        """
        find_ref = animal.name if isinstance(animal, Animal) else animal
        for a in self.__animals:
            if a.name == find_ref:
                return a
        return None

    def list_zoo_animals(self):
        print('--- Zoo Animals ---')
        if len(self.__animals) > 0:
            for a in self.get_animals():
                print(f"{a}"
                      f"\n--------------------")
        else:
            print("Matt Damon would be disappointed, you need animals in "
                  "your zoo!")

    def add_animal(self, animal):
        """Perform validation and then add animal to the zoo."""

        allow_add_animal = True

        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_add_animal = False

        if allow_add_animal and self.find_animal(animal):
            print(f"{animal.name} already in holding pen. "
                  f"They require assignment to an enclosure.")
            allow_add_animal = False

        if allow_add_animal:
            self.__animals.append(animal)
            print(f"{animal.name} added to zoo holding pen, "
                  f"awaiting assignment to enclosure.")
            return True

        return False


    def remove_animal(self, animal, enclosure):
        """Perform validation and then remove animal from zoo."""
        allow_remove_animal = True

        if not self.find_animal(animal):
            print(f"Animal is not in {enclosure.name}")
            allow_remove_animal = False

        if allow_remove_animal and animal.movable is False:
            print("Animal is under treatment and cannot be moved.")
            allow_remove_animal = False

        if allow_remove_animal:
            self.__animals.remove(animal)
            print(f"{animal.name} removed from zoo holding pen.")
            return True
        return False

    def add_enclosure(self, animal):
        self.__enclosures.append(animal)

    def remove_enclosure(self, animal):
        self.__enclosures.remove(animal)

    def assign_animal(self, animal, enclosure):
        """Assign animal to an enclosure."""
        if animal.movable:
            enclosure.add_occupant(animal)
        else:
            print(f"{animal.name} is under treatment and cannot be moved.")

    def unassign_animal(self, animal, enclosure):
        """Perform validation and then unassign animal from an enclosure."""
        if animal.movable:
            enclosure.remove_occupant(animal)
        else:
            print(f"{animal.name} is under treatment and cannot be moved.")

    def move_animal(self, animal, enclosure_from, enclosure_to):
        """Perform validation then move animal between enclosures."""
        allow_move = True

        if not enclosure_to.is_animal_compatible(animal):
            allow_move = False

        if allow_move and not animal.movable:
            print("Animal is under treatment and cannot be moved.")
            allow_move = False

        if allow_move:
            print(f"Moving {animal.name} from {enclosure_from.name} to "
                  f"{enclosure_to.name}:")
            self.unassign_animal(animal, enclosure_from)
            self.assign_animal(animal, enclosure_to)
            return True
        return False


    def add_to_routine(self, staff, task, day):
        allow_add_to_routine = True

        if task not in staff.duties:
            print(f"This task is not in {staff.name}'s official list of duties.")
            allow_add_to_routine = False

        if allow_add_to_routine:
            self.daily[day].append((staff, task))
            return True
        return False



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
# extracuricular

# new arrivals quarantine
# def enclosure_breach
#
#
# def sanitation_protocol
#
#
#
# def visitor_overboard