'''
File: animal.py
Description: The abstract class from which all animals inherit.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    # Class Docstring
    """
    Animals are the base class for all animal classes.

    Attributes
    ----------
    __name : str
        Animal nickname.
    __species : str
        Species name.
    __age : int
        Animal age.
    __gender : str
        Animal gender.
    __diet : str
        Animal’s diet ('Carnivore', 'Herbivore').
    __animal_class : str
        Biological class ('Mammal', 'Bird').
    __environment : str
        Environment animal needs to survive..
    __movable : bool
        Can animal be moved.
    __health_records : dict
        Collection of animal's health records.

    Methods
    -------
        cry():
            Animal makes a sound.
        eat():
            Animal eating behaviour.
        sleep():
            Animal sleeping behaviour.
        update_movability():
            Update movability based off health records.
        add_health_record(new_record_id, record):
            Adds health record.
        requires_surgery():
            Determine if surgery required.
        check_health():
            Performs health check and updates records.
    """

    def __init__(self, name, species, age, gender, diet, animal_class, environment):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender
        self.__diet = diet
        self.__animal_class = animal_class
        self.__environment = environment
        self.__movable = True
        self.__health_records = {}

    # --- Getters and Setters ---
    def get_name(self):
        return self.__name

    def get_movable(self):
        return self.__movable

    def set_movable(self, status):
        self.__movable = status

    def get_animal_class(self):
        return self.__animal_class

    def get_environment(self):
        return self.__environment

    def get_health_records(self):
        return self.__health_records

    def get_species(self):
        return self.__species

    def get_gender(self):
        return self.__gender

    def get_diet(self):
        return self.__diet

    def get_age(self):
        return self.__age

    # --- Property Attributes ---
    name = property(get_name)
    movable = property(get_movable, set_movable)
    animal_class = property(get_animal_class)
    environment = property(get_environment)
    record = property(get_health_records)
    species = property(get_species)
    gender = property(get_gender)
    diet = property(get_diet)
    age = property(get_age)

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    # --- General Methods ---
    def update_movability(self):
        """
        Update movable status based on active health issues.

            Parameters:
                None

            Returns:
                None: (Prints when animal’s movable change.)
        """


        for r, v in self.record.items():
            # If active issue and severity > 2 then immovable
            if v.status == "Active" and v.severity > 2:
                if self.movable:
                    self.movable = False
                    print(f"{self.name} is {'not movable' if self.movable is False else 'movable'} due to '{v.description}' - {v.date}")

    def add_health_record(self, new_record_id, record):
        """
        Add new health record to animal.

            Parameters:
                new_record_id (str): Unique record ID.
                record (object): HealthRecord to store.

            Returns:
                None: (Adds record and updates movable.)
        """

        self.__health_records[new_record_id] = record
        record.record_id = new_record_id
        print(f"Health record added to {self.name}")
        self.update_movability()

    def adjust_status_after_surgery(self):
        """
        Determine if animal requires surgery.

            Parameters:
                None

            Returns:
                bool: True if active record requires surgery.
        """

        # Changes record to closed if animal met conditions for surgery
        for record in self.record.values():
            if record.plan == "Surgery" and record.status == "Active":
                record.status = "Closed"
                return True
        return False

    def check_health(self):
        """
        Perform health check and update health records.

            Parameters:
                None

            Returns:
                None: (Prints treatment and record updates.)
        """

        # Store as list all records that are 'Active'
        active_issues = [record for record in self.record.values()
                         if record.status == "Active"]
        print(f"{self.name}'s health check begins.")
        # Treat all health issues, decrease its severity.
        if active_issues:
            for record in active_issues:
                print(f"{record.description} is treated.")
                record.severity -= 1
                # If the severity decrease reaches 0 then closed
                if record.severity == 0:
                    print(f"{record.description} is resolved.")
                    record.status = "Closed."
        else:
            print(f"{self.name} has no further issues. "
                  f"Vet has concluded health check.")

    def __str__(self):
        return (f"Animal Class: {self.__animal_class}"
                f"\nSpecies: {self.__species}"
                f"\nNickname: {self.__name}"
                f"\nGender: {self.__gender}"
                f"\nAge: {self.__age}"
                f"\nDiet: {self.__diet}")


class Lion(Animal):
    def __init__(self, name, species, age, gender,
                 diet, animal_class, environment):
        super().__init__(name, species, age, gender,
                         diet, animal_class, environment)
        self.__alpha = False

    def get_alpha(self):
        return self.__alpha

    alpha = property(get_alpha)

    def cry(self):
        print("*ROAAAARR!*")

    def eat(self):
        if self.alpha:
            print(f"{self.name} is the alpha of the pack and "
                  f"gets to eat first. *eats audibly*")
        else:
            print(f"{self.name} stands aside to let the alpha eat first.")

    def sleep(self):
        print("Lion walks in a circle then falls fast asleep.")


class Bird(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class, environment, wing_span):
        super().__init__(name, species, age, gender, diet, animal_class, environment)
        self.__wing_span = wing_span

    def cry(self):

        sounds = {
            "Galah": "*Screeech!*",
            "Toucan": "*KAWWWWW kckaww*",
            "Penguin": "* eee eeee eee*"
        }
        sound = sounds.get(self.species, "*Ckawwww!*")
        print(f"{self.name} the {self.species} goes {sound} ")

    def eat(self):
        print("Pecks at the food.")

    def sleep(self):
        print(f"{self.name} tucks its head between its feathers and heads off to noddy land.")

    def __str__(self):
        return super().__str__() + f"\nWing span: {self.__wing_span}cm"


class Fish(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class, environment, scale_colours):
        super().__init__(name, species, age, gender, diet, animal_class, environment)
        self.__scale_colours = scale_colours

    def cry(self):
        print("*inaudible noises*")

    def eat(self):
        if self.species == "Killer whale" and self.environment == "Arctic":
            print("Dives deep down in the tank for a tasty hunk of fish.")
        elif self.environment == "Tropical":
            print("Curiously bobs around the surface eating fishy food.")

    def sleep(self):
        print("Fish swims around and finds a rock, we think its sleeping "
              "but nobody really knows with fish.")

    def __str__(self):
        description = "I am a combination of "
        for i in range(len(self.__scale_colours)):
            if i < len(self.__scale_colours) - 1:
                description += f"{self.__scale_colours[i].lower()}, "
            else:
                description += f"and {self.__scale_colours[i].lower()}. "
        return super().__str__() + description