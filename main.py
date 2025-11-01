'''
File: main.py
Description: Demonstrate running zoo operations.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''


# Import classes
import animal
from enclosure import Enclosure
from zoo_operations import Zoo


def start_zoo():
    """Instantiate basic parts of the zoo."""
    # Zoo
    zoo1 = Zoo("Zoop")

    # Animals
    lion1 = animal.Lion("Athos", "Lion", 3, "Male", "Carnivore", "Mammal", "Savannah")
    bird1 = animal.Bird("Birdy", "Galah", 10, "Female", "Omnivore", "Bird", "Amazon", 10)
    bird2 = animal.Bird("Polly", "Toucan", 5, "Male", "Omnivore", "Bird", "Amazon", 10)
    bird3 = animal.Bird("Pingu", "Penguin", 5, "Male", "Carnivore", "Bird", "Arctic", 10)
    fish1 = animal.Fish("Old Ironjaw", "Trout", 3, "Male", "Omnivore", "Fish", "Tropical", 69)

    animals = [lion1, bird1, bird2, fish1, bird3]

    # Enclosures
    lion_enc = Enclosure("Lion ENC 1", 2, "Savannah", "Lion", "Empty")
    bird_enc = Enclosure("Bird ENC 1",50, "Amazon", "Bird", "Empty")
    bird2_enc = Enclosure("Bird ENC 2",50, "Arctic", "Bird", "Empty")
    fish_enc = Enclosure("Fish ENC 1",100, "Tropical", "Fish", "Empty")

    enclosures = [lion_enc, bird_enc, fish_enc, bird2_enc]

    return zoo1, animals, enclosures


# def zoo_operations():
#


def managing_animals(zoo, animals, enclosures):
    """Demonstrate adding animals to zoos and enclosures"""
    lion1, bird1, bird2, fish1 = animals
    lion_enc, bird_enc, fish_enc = enclosures


    print(f"\n--- Demo adding/removing animal ---")
    zoo.add_animal(lion1)
    zoo.add_animal(lion1)
    zoo.list_zoo_animals()
    zoo.remove_animal(lion1)
    zoo.list_zoo_animals()

    print(f"\n--- Demo assigning animal to enclosure ---")
    zoo.add_animal(bird1)
    zoo.add_enclosure(bird_enc)
    bird_enc.list_enc_animals()
    zoo.assign_animal(bird1, bird_enc)
    bird_enc.list_enc_animals()
    zoo.assign_animal(bird1, bird_enc)
    zoo.add_animal(bird2)
    zoo.assign_animal(bird2, bird_enc)
    bird_enc.list_enc_animals()
    zoo.assign_animal(bird2, bird_enc)
    zoo.assign_animal(bird2, lion_enc)

    print(f"\n--- Demo unassigning animal from enclosure ---")
    zoo.unassign_animal(bird1, bird_enc)
    zoo.unassign_animal(bird2, bird_enc)
    bird_enc.list_enc_animals()
    zoo.list_zoo_animals()
    zoo.assign_animal(bird1, bird_enc)
    zoo.assign_animal(bird2, bird_enc)
    bird_enc.unassign_all_animals()
    bird_enc.list_enc_animals()
    zoo.list_zoo_animals()
    bird1.movable = False
    zoo.assign_animal(bird1, bird_enc)
    bird1.movable = True
    zoo.assign_animal(bird1, bird_enc)
    bird1.movable = False
    zoo.unassign_animal(bird1, bird_enc)
    bird1.movable = True
    zoo.unassign_animal(bird1, bird_enc)


    print(f"\n--- Demo moving animal between enclosures ---")
    zoo.assign_animal(bird1, bird_enc)
    zoo.move_animal(bird1, bird_enc, lion_enc)






def demo_animal_abilities(zoo, animals, enclosures):
    """Demonstrate basic animal abilities."""
    lion1, bird1, fish1 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc = enclosures

    lion1.cry()
    lion1.eat()
    lion1.sleep()


def enclosure_restrictions(zoo, animals, enclosures):
    """
    Demonstrate enforcement of enclosure restrictions
    like max occupancy.
    """
    print(f"\n--- Demo enclosure restriction enforcement ---")
    lion1, bird1, bird2, fish1, bird3 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc = enclosures

    zoo.add_animal(bird1)
    zoo.add_animal(bird2)
    zoo.add_animal(bird3)
    zoo.assign_animal(bird2, bird_enc)
    zoo.add_enclosure(bird_enc)

    bird_enc.clean = 4
    zoo.assign_animal(bird1, bird_enc)
    bird_enc.clean = 5
    bird_enc.size = 1
    zoo.assign_animal(bird1, bird_enc)
    zoo.assign_animal(bird3, bird_enc)
    zoo.add_enclosure(bird2_enc)
    zoo.assign_animal(bird3, bird2_enc)

def managing_staff(zoo, animals, enclosures):
    """Demonstrate staff methods."""



def run_zoo_demonstration():
    # --- Main Demoing Sequence ---
    zoo, animals, enclosures = start_zoo()
    # demo_animal_abilities(zoo, animals, enclosures)
    # managing_animals(zoo, animals, enclosures)
    # enclosure_restrictions(zoo, animals, enclosures)
    managing_staff(zoo, animals, enclosures)


if __name__ == "__main__":
    run_zoo_demonstration()

