'''
File: main.py
Description: Demonstrate running zoo operations.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from idlelib.pyshell import fix_x11_paste

# Import classes
import animal
from zoo_operations import Zoo


def basic_zoo_start():
    """Instantiate a basic functioning zoo for testing."""
    # Zoo
    z1 = Zoo("Zoop")

    # Animals
    l1 = animal.Lion("Athos", "Lion", 3, "Male", "Carnivore", "Mammal")
    b1 = animal.Bird("Birdy", "Galah", 10, "Female", "Omnivore", "Bird", 10)
    f1 = animal.Fish("Fishy", "Trout", 3, "Male", "Omnivore", "Fish", 69)

    return z1, l1, b1, f1


def zoo_operations():
    z1, l1, b1, f1 = basic_zoo_start()



def processing_animals():
    z1, l1, b1, f1 = basic_zoo_start()

    print(f"\n--- Test adding/removing animal ---")
    z1.add_animal(l1)
    z1.print_animals()
    z1.remove_animal(l1)
    z1.print_animals()

    print(f"\n--- Test adding/removing animal to enclosure ---")
    z1.add_animal(l1)



def test_animal_abilities():
    """Test basic animal abilities."""
    basic_zoo_start()
    l1.cry()
    l1.eat()
    l1.sleep()



# --- Main Testing Sequence ---
# zoo_operations()

processing_animals()
