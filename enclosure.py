'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal


class Enclosure:
    def __init__(self, name, size, environment, enclosure_class, enclosure_status):
        self.__name = name
        self.__size = size
        self.__environment = environment
        self.__cleanliness = 10
        self.__enclosure_class = enclosure_class
        self.__enclosure_status = enclosure_status
        self.__occupants = []
        self.__feed_available = False

    # Getters and setters
    def get_occupants(self):
        return self.__occupants

    def get_name(self):
        return self.__name

    def get_enclosure_class(self):
        return self.__enclosure_class

    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, cleanliness):
        self.__cleanliness = cleanliness

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_environment(self):
        return self.__environment

    def get_feed_available(self):
        return self.__feed_available

    def set_feed_available(self, status):
        self.__feed_available = status

    def get_enclosure_status(self):
        return self.__enclosure_status

    def set_enclosure_status(self, status):
        self.__enclosure_status = status



    name = property(get_name)
    enclosure_class = property(get_enclosure_class)
    size = property(get_size, set_size)
    clean = property(get_cleanliness, set_cleanliness)
    occupants = property(get_occupants)
    environment = property(get_environment)
    feed = property(get_feed_available, set_feed_available)
    status = property(get_enclosure_status, set_enclosure_status)


    # Validation Methods
    def can_accept_animal(self, animal):
        accept_animal = True

        if len(self.occupants) == self.size:
            print(f"{self.name} is at max occupancy. "
                  f"Unable to house more animals.")
            accept_animal = False

        if self.get_cleanliness() < 5:
            print(f"{self.name} is too dirty to accept {animal.name}")
            accept_animal = False

        if animal.animal_class != self.enclosure_class:
            print(f"{animal.animal_class}s cannot be housed in {self.enclosure_class} enclosures.")
            accept_animal = False

        if animal.environment != self.environment:
            print(f"{animal.name} cannot survive in {self.name}'s "
                  f"{self.environment.lower()} environment.")
            accept_animal = False

        return accept_animal


    # Enclosure management

    def feed_animals(self):
        allow_feed_animals = True

        if self.feed:
            print(f"Animals already have food.")
            allow_feed_animals = False

        if allow_feed_animals and self.clean < 5:
            print("Cannot feed animals, enclosure is too dirty.")
            allow_feed_animals = False

        if allow_feed_animals:
            self.feed = True
            self.clean -= 3
            print(f"Animals fed. Enclosure is a little messier "
                  f"after feeding time.")
            return True
        return False



    def list_enc_animals(self):
        print(f'--- {self.name} Occupants ---')
        if len(self.occupants) > 0:
            for a in self.occupants:
                print(f"{a}"
                      f"\n--------------------")
        else:
            print("Matt Damon would be disappointed, you need animals in "
                  "your zoo!")


    def find_animal(self, animal):
        """
        Find an animal with either a string or object as a parameter.
        """
        find_ref = animal.name if isinstance(animal, Animal) else animal
        for a in self.__occupants:
            if a.name == find_ref:
                return a
        return None



    def add_occupant(self, animal):
        """Perform validation and assign an animal."""

        allow_assign_animal = True

        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_assign_animal = False

        # If the enclosure houses multiple animal_class, iterate over them
        # and see if they match.
        if allow_assign_animal and not self.can_accept_animal(animal):
            allow_assign_animal = False

        if allow_assign_animal and self.find_animal(animal):
            print(f"Animal already assigned to {self.name}")
            allow_assign_animal = False


        if allow_assign_animal:
            self.__occupants.append(animal)
            print(f"{animal.name} assigned to {self.name}.")
            if self.status is "Empty":
                self.status = "Occupied"
            return True
        return False


    def remove_occupant(self, animal):
        """Perform validation and unassign animal."""
        allow_unassign_animal = True

        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_unassign_animal = False

        if allow_unassign_animal:
            self.__occupants.remove(animal)
            print(f"{animal.name} unassigned from {self.name}. "
                  f"Now in holding pen.")
            return True
        return False

    def unassign_all_animals(self):
        print(f"Unassigning all animals in {self.name}:")
        for o in self.occupants.copy():
            self.remove_occupant(o)



    def __str__(self):
        return f"{self.__name}"


    def __repr__(self):
        return f"{self.__name}"




