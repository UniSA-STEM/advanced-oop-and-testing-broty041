'''
File: animal.py
Description: The abstract class from which all animals inherit.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

from health_record import HealthRecord


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
        self.__health_records = {}


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


    def update_movability(self):
        for r, v in self.record.items():
            if v.status == "Active" and v.severity > 2:
                if self.movable:
                    self.movable = False
                    print(f"{self.name} is {"not movable" 
                    if self.movable is False else "movable"} "
                          f"due to "
                          f"'{v.description}' - {v.date}")


    def add_health_record(self, new_record_id, record):
        self.__health_records[new_record_id] = record
        record.record_id = new_record_id
        print(f"Health record added to {self.name}")
        self.update_movability()


    def requires_surgery(self):
        for record in self.record.values():
            if record.plan == "Surgery" and record.status == "Active":
                record.status = "Closed"
                return True
        return False



    def check_health(self):
        active_issues = [record for record in self.record.values()
                         if record.status == "Active"]
        print(f"{self.name}'s health check begins.")
        if active_issues:
            for record in active_issues:
                print(f"{record.description} is treated.")
                record.severity = -1
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