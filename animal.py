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
    def __init__(self, name, species, age, gender, diet, animal_class):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender
        self.__diet = diet
        self.__animal_class = animal_class

    def get_name(self):
        return self.__name


    name = property(get_name)

    @abstractmethod
    def cry(self):

        pass


    @abstractmethod
    def eat(self):
        pass


    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return (f"Species: {self.__species}"
                f"\nAnimal Class: {self.__animal_class}"
                f"\nNickname: {self.__name}"
                f"\nGender: {self.__gender}"
                f"\nAge: {self.__age}"
                f"\nDiet: {self.__diet}")






class Lion(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class):
        super().__init__(name, species, age, gender, diet, animal_class)

    def cry(self):
        print("*ROAAAARR!*")

    def eat(self):
        print("Mangles its prey.")

    def sleep(self):
        print("Lion walks in a circle then falls fast asleep.")







class Bird(Animal):
    def __init__(self, name, species, age, gender, diet, animal_class, wing_span):
        super().__init__(name, species, age, gender, diet, animal_class)
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
    def __init__(self, name, species, age, gender, diet, animal_class, scale_colours):
        super().__init__(name, species, age, gender, diet, animal_class)
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