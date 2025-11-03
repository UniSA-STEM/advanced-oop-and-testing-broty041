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
    def __init__(self, name, species, age, gender, diet, animal_class, environment):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender
        self.__diet = diet
        self.__animal_class = animal_class
        self.__environment = environment
        self.__movable = True
        self.__health_records = []


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


    name = property(get_name)
    movable = property(get_movable, set_movable)
    animal_class = property(get_animal_class)
    environment = property(get_environment)
    record = property(get_health_records)


    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass


    @abstractmethod
    def sleep(self):
        pass


    def update_movability(self, record):
        for r in self.record:
            if r.status == "Active" and r.severity > 2:
                self.movable = False


    def add_health_record(self, record):
        self.__health_records.append(record)
        self.update_movability(record)



    def __str__(self):
        return (f"Animal Class: {self.__animal_class}"
                f"\nSpecies: {self.__species}"
                f"\nNickname: {self.__name}"
                f"\nGender: {self.__gender}"
                f"\nAge: {self.__age}"
                f"\nDiet: {self.__diet}")






class Lion(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class, environment):
        super().__init__(name, species, age, gender, diet, animal_class, environment)

    def cry(self):
        print("*ROAAAARR!*")

    def eat(self):
        print("Mangles its prey.")

    def sleep(self):
        print("Lion walks in a circle then falls fast asleep.")







class Bird(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class, environment, wing_span):
        super().__init__(name, species, age, gender, diet, animal_class, environment)
        self.__wing_span = wing_span

    def cry(self):
        print("*Ckkawwww!*")

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
        print("nibbles.")

    def sleep(self):
        print("Lion walks in a circle then falls fast asleep.")

    def __str__(self):
        description = "I am a combination of "
        for i in range(len(self.__scale_colours)):
            if i < len(self.__scale_colours) - 1:
                description += f"{self.__scale_colours[i].lower()}, "
            else:
                description += f"and {self.__scale_colours[i].lower()}. "
        return super().__str__() + description