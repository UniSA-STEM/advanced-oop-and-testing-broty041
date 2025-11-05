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
    # Class Docstring
    """
    Enclosures are where animals exist within the zoo.

    Attributes
    ----------
    __name : str
        Enclosure name.
    __size : int
        Maximum number of animal occupants
    __environment : str
        The enclosures environment theme ('Savannah', 'Aquatic').
    __cleanliness : int
        Condition of enclosure (1–10 scale).
    __enclosure_class : str
        Biological class enclosure supports.
    __enclosure_status : str
        Whether the enclosure is 'Empty', 'Occupied'.
    __occupants : list
        List of enclosed animals.
    __feed_available : bool
        Indicates if theres food out for animals to eat.

    Methods
    -------
        can_accept_animal(animal):
            Validate if enclosure accepting animal.
        feed_animals():
            Feed all animals if conditions are met.
        list_enc_animals():
            Display list of current occupants.
        find_animal(animal):
            Locate animal by name or object.
        add_occupant(animal):
            Add an animal to enclosure.
        remove_occupant(animal):
            Remove an animal from enclosure.
        unassign_all_animals():
            Remove all animals from enclosure.
    """

    def __init__(self, name, size, environment, enclosure_class, enclosure_status):
        self.__name = name
        self.__size = size
        self.__environment = environment
        self.__cleanliness = 10
        self.__enclosure_class = enclosure_class
        self.__enclosure_status = enclosure_status
        self.__occupants = []
        self.__feed_available = False

    # --- Getters and Setters ---
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

    # --- Property Attributes ---
    name = property(get_name)
    enclosure_class = property(get_enclosure_class)
    size = property(get_size, set_size)
    clean = property(get_cleanliness, set_cleanliness)
    occupants = property(get_occupants)
    environment = property(get_environment)
    feed = property(get_feed_available, set_feed_available)
    status = property(get_enclosure_status, set_enclosure_status)

    # --- Validation Methods ---
    def can_accept_animal(self, animal):
        """
        Validate if animal can be accepted into enclosure.

            Parameters:
            animal (object): Animal to validate.

            Returns:
                bool: True if suitable, otherwise False.
        """

        accept_animal = True

        # Check enclosure capacity not full
        if len(self.occupants) == self.size:
            print(f"{self.name} is at max occupancy. "
                  f"Unable to house more animals.")
            accept_animal = False

        # Check if dirt clean enough for new animal
        if self.get_cleanliness() < 5:
            print(f"{self.name} is too dirty to accept {animal.name}")
            accept_animal = False

        # Check if enclosure can hold this animal class
        if animal.animal_class != self.enclosure_class:
            print(f"{animal.animal_class}s cannot be housed in {self.enclosure_class} enclosures.")
            accept_animal = False

        # Check environments match animal, ie no tropical birds with penguins
        if animal.environment != self.environment:
            print(f"{animal.name} cannot survive in {self.name}'s "
                  f"{self.environment.lower()} environment.")
            accept_animal = False

        return accept_animal

    # --- Enclosure management ---
    def feed_animals(self):
        """
        Feed animals if enclosure clean and not already fed. Feeding lowers
        cleanliness.

            Parameters:
                None

            Returns:
                bool: True if feeding successful, otherwise False.
        """

        allow_feed_animals = True

        # No duplicate feeds
        if self.feed:
            print(f"Animals already have food.")
            allow_feed_animals = False

        # No feed if dirty
        if allow_feed_animals and self.clean < 5:
            print("Cannot feed animals, enclosure is too dirty.")
            allow_feed_animals = False

        # Reduce cleanliness by 3 if fed.
        if allow_feed_animals:
            self.feed = True
            self.clean -= 3
            print(f"Animals fed. Enclosure is a little messier "
                  f"after feeding time.")
            return True
        return False

    def list_enc_animals(self):
        """
        List animals currently in enclosure.

            Parameters:
                None

            Returns:
                None. (Prints list of enclosure animals.)
        """

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

            Parameters:
                animal (object or str): Animal to find.

            Returns:
                object: Animal if found, otherwise None.
        """

        find_ref = animal.name if isinstance(animal, Animal) else animal
        for a in self.__occupants:
            if a.name == find_ref:
                return a
        return None

    def add_occupant(self, animal):
        """
        Perform validation and assign an animal.

            Parameters:
                animal (object): Animal to assign.

            Returns:
                bool: True if animal added successfully, otherwise False.
        """

        allow_assign_animal = True

        # Ensure passed object is an animal
        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_assign_animal = False

        # If the enclosure houses multiple animal_class, iterate over them
        # and see if they match.
        if allow_assign_animal and not self.can_accept_animal(animal):
            allow_assign_animal = False

        # No duplicate animals
        if allow_assign_animal and self.find_animal(animal):
            print(f"Animal already assigned to {self.name}")
            allow_assign_animal = False

        # Change status zoo to occupied if was empty
        if allow_assign_animal:
            self.__occupants.append(animal)
            print(f"{animal.name} assigned to {self.name}.")
            if self.status == "Empty":
                self.status = "Occupied"
            return True
        return False

    def remove_occupant(self, animal):
        """
        Perform validation and unassign animal.

            Parameters:
                animal (object): Animal to remove.

            Returns:
                bool: True if removal successful, otherwise False.
        """
        allow_unassign_animal = True

        # Ensure passed object is an animal
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
        """
        Unassign all animals from enclosure.

            Parameters:
                None

            Returns:
                None:
        """
        print(f"Unassigning all animals in {self.name}:")
        for o in self.occupants.copy():
            self.remove_occupant(o)


    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__name}"
