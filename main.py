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
from report import Report, AnimalsBySpecies
from zoo_operations import Zoo
from staff import Staff
import task


def start_zoo():
    # Class Docstring
    """Instantiate basic parts of the zoo."""

    # Zoo
    zoo1 = Zoo("Zoop")

    # Animals
    lion1 = animal.Lion("Athos", "Lion", 3, "Male",
                        "Carnivore", "Mammal",
                        "Savannah")
    bird1 = animal.Bird("Birdy", "Galah", 10,
                        "Female", "Omnivore", "Bird",
                        "Amazon", 10)
    bird2 = animal.Bird("Polly", "Toucan", 5,
                        "Male", "Omnivore", "Bird",
                        "Amazon", 10)
    bird3 = animal.Bird("Pingu", "Penguin", 5,
                        "Male", "Carnivore", "Bird",
                        "Arctic", 10)
    bird4 = animal.Bird("Sangief", "Galah", 4,
                        "Male", "Omnivore", "Bird",
                        "Amazon", 10)
    fish1 = animal.Fish("Old Ironjaw", "Trout", 3,
                        "Male", "Omnivore", "Fish",
                        "Tropical", ["yellow", "blue"])
    fish2 = animal.Fish("Old Ironjaw", "Killer whale",
                        3, "Male", "Omnivore",
                        "Fish", "Arctic",
                        ["black"])

    animals = [lion1, bird1, bird2, fish1, fish2, bird3, bird4]

    # Enclosures
    lion_enc = Enclosure("Lion ENC 1", 2, "Savannah",
                         "Mammal", "Empty")
    bird_enc = Enclosure("Bird ENC 1", 50, "Amazon",
                         "Bird", "Empty")
    bird2_enc = Enclosure("Bird ENC 2", 50, "Arctic",
                          "Bird", "Empty")
    bird3_enc = Enclosure("Bird ENC 3", 50, "Amazon",
                          "Bird", "Empty")
    bird4_enc = Enclosure("Bird ENC 4", 50, "Savannah",
                          "Bird", "Empty")

    fish_enc = Enclosure("Fish ENC 1", 100, "Tropical",
                         "Fish", "Empty")

    enclosures = [lion_enc, bird_enc, fish_enc, bird2_enc,
                  bird3_enc, bird4_enc]

    # Staff
    zk1 = Staff("Bobbery", "Zoo keeper", "Savannah")
    vet1 = Staff("Dr Harry", "Veterinarian", "Savannah")

    staff_list = [zk1, vet1]

    # Tasks
    feed_lion_enc = task.Feed("Feeding lions",
                              "Feeding lions at the lion enclosure",
                              ["Veterinarian", "Zoo keeper"],
                              lion_enc)
    clean_lion_enc = task.Clean("Cleaning lion enclosure",
                               "Cleaning the lion enclosure",
                               ["Veterinarian", "Zoo keeper"],
                               lion_enc)
    feed_bird_enc = task.Feed("Feeding birds",
                              "Feeding birds at the bird enclosure",
                              ["Veterinarian", "Zoo keeper"],
                              bird_enc)
    feed_fish_enc = task.Feed("Feeding fish",
                              "Feeding fish at the fish enclosure",
                              ["Veterinarian", "Zoo keeper"],
                              fish_enc)
    surgery = task.Surgery("Surgery", "Performs surgery.",
                           ["Veterinarian"], animal=lion1)
    health_check_lion1 = task.HealthCheck("Health check",
                                "Performs health check on lion.",
                                ["Veterinarian"],
                                          animal=lion1)

    tasks = [feed_lion_enc, feed_bird_enc, feed_fish_enc,
             surgery, clean_lion_enc, health_check_lion1]

    return zoo1, animals, enclosures, staff_list, tasks


def demo_animal_abilities(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate basic animal abilities."""
    print(f"\n--- Demonstrating animal abilities ---")

    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals

    print(f"\n--- Animal Cry ---")
    lion1.cry()
    bird1.cry()
    bird2.cry()
    bird3.cry()
    bird4.cry()
    fish1.cry()
    fish2.cry()

    print(f"\n--- Animal Eat ---")
    lion1.eat()
    bird1.eat()
    bird2.eat()
    bird3.eat()
    bird4.eat()
    fish1.eat()
    fish2.eat()

    print(f"\n--- Animal Sleep ---")
    lion1.sleep()
    bird1.sleep()
    bird2.sleep()
    bird3.sleep()
    bird4.sleep()
    fish1.sleep()
    fish2.sleep()


def managing_animals(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate adding animals to zoos and enclosures"""
    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc, bird3_enc, bird4_enc = enclosures
    print(f"\n--- Demonstrating managing animals ---")

    print(f"\n--- Adding/removing animal ---")
    zoo.add_animal(lion1)
    zoo.add_animal(lion1)
    zoo.list_zoo_animals()

    print(f"\n--- Assigning animal to enclosure ---")
    zoo.add_animal(bird1)
    zoo.add_enclosure(bird_enc)
    bird_enc.list_enc_animals()
    zoo.assign_animal(bird1, bird_enc)
    bird_enc.list_enc_animals()

    print(f"\n--- Assign Validation ---")
    zoo.assign_animal(bird1, bird_enc)
    zoo.add_animal(bird2)
    zoo.assign_animal(bird2, bird_enc)
    bird_enc.list_enc_animals()
    zoo.assign_animal(bird2, bird_enc)
    zoo.assign_animal(bird2, lion_enc)

    print(f"\n--- Unassigning animal from enclosure ---")
    zoo.unassign_animal(bird1, bird_enc)
    zoo.unassign_animal(bird2, bird_enc)
    bird_enc.list_enc_animals()
    zoo.list_zoo_animals()

    print(f"\n--- Unassign all animals in enclosure ---")
    zoo.assign_animal(bird1, bird_enc)
    zoo.assign_animal(bird2, bird_enc)
    bird_enc.unassign_all_animals()
    bird_enc.list_enc_animals()
    zoo.list_zoo_animals()

    print(f"\n--- Assigning when not movable ---")
    bird1.movable = False
    zoo.assign_animal(bird1, bird_enc)
    bird1.movable = True
    zoo.assign_animal(bird1, bird_enc)
    bird1.movable = False
    zoo.unassign_animal(bird1, bird_enc)
    bird1.movable = True
    zoo.unassign_animal(bird1, bird_enc)

    print(f"\n--- Moving animal between enclosures ---")
    zoo.assign_animal(bird1, bird_enc)
    zoo.move_animal(bird1, bird_enc, lion_enc)
    zoo.move_animal(bird1, bird_enc, bird3_enc)


def managing_enclosures(zoo, animals, enclosures, staff_list, tasks):
    """
    Demonstrate enclosure management
    """
    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc, bird3_enc, bird4_enc = enclosures

    print(f"\n--- Demonstrating managing enclosures ---")

    print(f"\n--- Further enclosure validation ---")
    zoo.add_animal(bird1)
    zoo.add_animal(bird2)
    zoo.add_animal(bird3)
    zoo.assign_animal(bird2, bird_enc)
    zoo.add_enclosure(bird_enc)
    zoo.assign_animal(bird2, bird_enc)

    print(f"\n--- Enclosure too dirty ---")

    bird_enc.clean = 4
    zoo.assign_animal(bird1, bird_enc)
    bird_enc.clean = 5

    print(f"\n--- Enclosure reached max occupants ---")
    bird_enc.size = 1
    zoo.assign_animal(bird1, bird_enc)

    print(f"\n--- Enclosure environment not suitable for animal ---")
    zoo.assign_animal(bird3, bird_enc)
    zoo.add_enclosure(bird2_enc)
    zoo.assign_animal(bird3, bird2_enc)

    print(f"\n--- Removing enclosure. ---")
    zoo.remove_enclosure(bird2_enc)
    zoo.unassign_animal(bird3, bird2_enc)
    zoo.remove_enclosure(bird2_enc)


def managing_staff(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate staff methods."""
    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc, bird3_enc, bird4_enc = enclosures
    (feed_lion_enc, feed_bird_enc, feed_fish_enc, surgery,
     clean_lion_enc, health_check_lion1) = tasks
    zk1, vet1 = staff_list

    print(f"\n--- Demonstrating managing staff members. ---")

    print(f"\n--- Adding staff members. ---")
    zoo.add_staff(zk1)
    zoo.list_staff()
    zoo.remove_staff(zk1)
    zoo.add_staff(zk1)
    zoo.add_staff(vet1)

    print(f"\n--- Adding task but staff not assigned to enclosure. ---")
    zoo.add_task(zk1, feed_lion_enc)
    zoo.add_enclosure(lion_enc)
    zoo.assign_staff_enclosure(zk1, lion_enc)
    zoo.add_task(zk1, feed_lion_enc)
    zoo.add_task(zk1, clean_lion_enc)

    print(f"\n--- Unassigning with assigned related tasks. ---")
    zoo.unassign_staff_enclosure(zk1, lion_enc)
    zk1.list_tasks()
    zoo.remove_task(zk1, feed_lion_enc)
    zoo.remove_task(zk1, clean_lion_enc)
    zk1.list_tasks()
    zoo.unassign_staff_enclosure(zk1, lion_enc)

    print(f"\n--- Staff cleaning enclosure. ---")
    zk1.perform_task(clean_lion_enc)
    zoo.add_task(zk1, clean_lion_enc)
    zoo.assign_staff_enclosure(zk1, lion_enc)
    zoo.add_task(zk1, clean_lion_enc)
    zoo.add_task(zk1, feed_lion_enc)
    print(lion_enc.clean)
    zk1.perform_task(clean_lion_enc)
    print(lion_enc.clean)
    lion_enc.clean = 7
    zk1.perform_task(clean_lion_enc)
    print(lion_enc.clean)

    print(f"\n--- Staff speciality matches enclosure environment. ---")
    zoo.add_enclosure(bird4_enc)
    zoo.add_enclosure(bird_enc)
    zoo.assign_staff_enclosure(zk1, bird_enc)
    zk1.list_tasks()

    print(f"\n--- Cant remove task staff doesnt have.. ---")
    zoo.remove_task(zk1, feed_lion_enc)
    zoo.remove_task(zk1, feed_fish_enc)
    zoo.remove_task(zk1, feed_lion_enc)

    print(f"\n--- Vet performs surgery ---")
    zoo.assign_staff_enclosure(vet1, lion_enc)
    zoo.add_task(vet1, feed_lion_enc)
    zoo.add_task(vet1, surgery)
    vet1.perform_task(surgery)
    zoo.generate_health_record(lion1, "Appendicitis",
                               "Injury", "03/11/25",
                               "Active", 2, "Surgery", "Ate shoe.")
    vet1.perform_task(surgery)

    print(f"\n--- Zoo keeper feed animals ---")
    zoo.add_task(zk1, feed_lion_enc)
    lion_enc.feed = False
    zk1.perform_task(feed_lion_enc)

    print(f"\n--- Cant feed if enclosure is messy ---")
    lion_enc.clean = 4
    lion_enc.feed = False
    zk1.perform_task(feed_lion_enc)
    lion_enc.clean = 10
    lion_enc.feed = False
    zk1.perform_task(feed_lion_enc)
    print(lion_enc.clean)

    print(f"\n--- Vet performs health check ---")
    zoo.generate_health_record(lion1, "Rumbly tummy", "Injury",
                               "03/11/25", "Active", 3, "Belly rubs.",
                               "Ate peanuts.")
    vet1.perform_task(health_check_lion1)
    zoo.add_task(vet1, health_check_lion1)
    vet1.perform_task(health_check_lion1)

    print(f"\n--- Health check reduces severity working towards healthy ---")
    vet1.perform_task(health_check_lion1)
    vet1.perform_task(health_check_lion1)
    vet1.perform_task(health_check_lion1)

    print(f"\n--- Zoo building daily routine with staff and tasks ---")
    zoo.remove_task(zk1, feed_lion_enc)
    zoo.add_to_routine(zk1, feed_lion_enc, "Monday")
    zoo.add_task(zk1, feed_lion_enc)
    zoo.add_to_routine(zk1, feed_lion_enc, "Monday")
    zoo.add_to_routine(vet1, surgery, "Tuesday")
    print(zoo.daily)


def health_record_system(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate usage of health record system."""
    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals

    print(f"\n--- Demonstrating health records. ---")
    zoo.generate_health_record(lion1, "Rumbly tummy", "Injury",
                               "03/11/25", "Active", 3, "Belly rubs.",
                               "Ate peanuts.")
    zoo.generate_health_record(lion1, "Runny nose", "Illness",
                               "04/11/25", "Active", 2, "Vicks rubs.",
                               "Needs tissues.")
    zoo.generate_health_record(bird1, "Swooping", "Behavioural",
                               "04/11/25", "Active", 3, "Cold water.",
                               "Aggressively swooping visitors.")


def generate_reports(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate usage of zoo operations reports."""
    lion1, bird1, bird2, fish1, fish2, bird3, bird4 = animals
    lion_enc, bird_enc, fish_enc, bird2_enc, bird3_enc, bird4_enc = enclosures

    print(f"\n--- Demonstrating report system. ---")
    for e in enclosures:
        zoo.add_enclosure(e)

    zoo.add_animal(bird1)
    zoo.assign_animal(bird1, bird_enc)
    zoo.add_animal(bird2)
    zoo.assign_animal(bird2, bird_enc)
    zoo.add_animal(bird3)
    zoo.assign_animal(bird3, bird2_enc)
    zoo.add_animal(lion1)
    zoo.assign_animal(lion1, lion_enc)
    zoo.add_animal(fish1)

    # To run the interactive report menu uncomment the line below and
    # comment the for loop code :)
    # zoo.display_report_interface()
    for report in zoo.reports.reports:
        report.generate_report(zoo)


def dependency_checking(zoo, animals, enclosures, staff_list, tasks):
    """Demonstrate dependency checking."""
    (lion1, bird1, bird2, fish1, fish2, bird3, bird4) = animals
    lion_enc, bird_enc, fish_enc, bird2_enc, bird3_enc, bird4_enc = enclosures
    (feed_lion_enc, feed_bird_enc, feed_fish_enc, surgery, clean_lion_enc,
     health_check_lion1) = tasks
    zk1, vet1 = staff_list

    print(f"\n--- Demonstrating dependency checking of tasks. ---")

    print(f"\n--- Removing animal with related task in daily routine ---")
    zoo.add_staff(vet1)
    zoo.add_animal(lion1)
    zoo.assign_staff_enclosure(vet1, lion_enc)
    zoo.add_enclosure(lion_enc)
    zoo.assign_staff_enclosure(vet1, lion_enc)
    zoo.add_task(vet1, surgery)
    zoo.add_to_routine(vet1, surgery, "Monday")
    zoo.remove_animal(lion1, lion_enc)
    zoo.clear_routines()
    zoo.remove_task(vet1, surgery)

    print(f"\n--- Removing animal with related task in staff tasks ---")
    zoo.add_task(vet1, surgery)
    zoo.remove_animal(lion1, lion_enc)
    zoo.remove_task(vet1, surgery)
    lion1.update_movability()

    print(f"\n--- Removing enclosure with related task in daily routine ---")
    zoo.add_staff(zk1)
    zoo.assign_staff_enclosure(zk1, lion_enc)
    zoo.add_task(zk1, feed_lion_enc)
    zoo.add_to_routine(zk1, feed_lion_enc, "Monday")
    zoo.remove_enclosure(lion_enc)
    zoo.clear_routines()
    zoo.remove_task(zk1, feed_lion_enc)
    zoo.remove_enclosure(lion_enc)

    print(f"\n--- Removing enclosure with related task in staff tasks ---")
    zoo.add_task(zk1, feed_lion_enc)
    zoo.add_enclosure(lion_enc)
    zoo.remove_enclosure(lion_enc)
    zoo.remove_task(zk1, feed_lion_enc)
    zoo.remove_enclosure(lion_enc)

    print(f"\n--- Removing task with related daily routine ---")
    zoo.add_task(vet1, surgery)
    zoo.add_to_routine(vet1, surgery, "Monday")
    zoo.remove_task(vet1, surgery)
    zoo.clear_routines()
    zoo.remove_task(vet1, surgery)


def run_zoo_demonstration():
    # --- Full Zoo Demonstration ---

    print(f"\n--- Start the zoo ---")
    zoo, animals, enclosures, staff_list, tasks = start_zoo()

    demo_animal_abilities(zoo, animals, enclosures, staff_list, tasks)
    managing_animals(zoo, animals, enclosures, staff_list, tasks)
    managing_enclosures(zoo, animals, enclosures, staff_list, tasks)
    managing_staff(zoo, animals, enclosures, staff_list, tasks)
    health_record_system(zoo, animals, enclosures, staff_list, tasks)
    generate_reports(zoo, animals, enclosures, staff_list, tasks)
    dependency_checking(zoo, animals, enclosures, staff_list, tasks)


if __name__ == "__main__":
    run_zoo_demonstration()
