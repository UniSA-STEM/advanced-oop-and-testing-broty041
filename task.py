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
    def __init__(self, name, description, roles=None, assigned_enclosure=None, animal=None):
        self.__name = name
        self.__description = description
        self.__assigned_enclosure = assigned_enclosure
        self.__roles = roles
        self.__animal = animal

    # Getters / setters
    def get_name(self):
        return self.__name

    def get_roles(self):
        return self.__roles

    def get_assigned_enclosure(self):
        return self.__assigned_enclosure

    def get_animal(self):
        return self.__animal

    name = property(get_name)
    roles = property(get_roles)
    enclosure = property(get_assigned_enclosure)
    animal = property(get_animal)


    @abstractmethod
    def perform_action(self):
        pass

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__name}"


class Feed(Task):
    def __init__(self, name, description, roles=None, assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles, assigned_enclosure, animal)

    def perform_action(self):
        self.enclosure.feed_animals()






class Surgery(Task):
    def __init__(self, name, description, roles, assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles, assigned_enclosure, animal)



    def get_health_record(self):
        return self.__health_record


    def perform_action(self):


        if self.animal.requires_surgery():
            print(f"Surgery is performed on {self.animal.name} the "
                  f"{self.animal.species} and is successful.")
        else:
            print(f"{self.animal.name} the {self.animal.species} does not "
                  f"need surgery. Please confirm with Veterinarian.")


class HealthCheck(Task):
    def __init__(self, name, description, roles, assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles, assigned_enclosure, animal)




    def perform_action(self):
        self.animal.check_health()