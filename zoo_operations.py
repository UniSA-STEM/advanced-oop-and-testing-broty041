'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from health_record import HealthRecord
from report import DailyRoutines, AnimalsBySpecies, StatusAllEnclosures


class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []
        self.__daily_routines = {"Monday": [],
                                 "Tuesday": [],
                                 "Wednesday": [],
                                 "Thursday": [],
                                 "Friday": []}
        self.__reports = self.populate_reports()

    # Getters / setters
    def get_animals(self):
        return self.__animals

    def get_daily_routines(self):
        return self.__daily_routines

    def get_reports(self):
        return self.__reports

    def get_enclosures(self):
        return self.__enclosures

    def get_staff(self):
        return self.__staff

    animals = property(get_animals)
    daily = property(get_daily_routines)
    reports = property(get_reports)
    enclosures = property(get_enclosures)
    staff = property(get_staff)


    # Animal management
    def find_animal(self, animal):
        """
        Find an animal with either a string or object as a parameter.
        """
        find_ref = animal.name if isinstance(animal, Animal) else animal
        for a in self.__animals:
            if a.name == find_ref:
                return a
        return None

    def list_zoo_animals(self):
        print('--- Zoo Animals ---')
        if len(self.__animals) > 0:
            for a in self.animals:
                print(f"{a}"
                      f"\n--------------------")
        else:
            print("Matt Damon would be disappointed, you need animals in "
                  "your zoo!")

    def list_staff(self):
        print('--- Zoo Staff ---')
        if len(self.__staff) > 0:
            for s in self.staff:
                print(f"{s}"
                      f"\n--------------------")
        else:
            print("You probably need some staff.")


    def add_animal(self, animal):
        """Perform validation and then add animal to the zoo."""

        allow_add_animal = True

        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_add_animal = False

        if allow_add_animal and self.find_animal(animal):
            print(f"{animal.name} already in holding pen. "
                  f"They require assignment to an enclosure.")
            allow_add_animal = False

        if allow_add_animal:
            self.__animals.append(animal)
            print(f"{animal.name} added to zoo holding pen, "
                  f"awaiting assignment to enclosure.")
            return True

        return False


    def remove_animal(self, animal, enclosure):
        """Perform validation and then remove animal from zoo."""
        allow_remove_animal = True

        if not self.find_animal(animal):
            print(f"Animal is not in {enclosure.name}")
            allow_remove_animal = False

        if allow_remove_animal:
            routine_dependencies = self.check_routine_dependencies_animal(animal)
            if routine_dependencies:
                print(f"Cannot remove {animal.name}. Animal is assigned to daily routines: {routine_dependencies}")
                allow_remove_animal = False

        if allow_remove_animal:
            staff_dependencies = self.check_animal_dependencies_staff(animal)
            if staff_dependencies:
                print(f"Cannot remove {animal.name}. Animal is assigned to staff tasks: {staff_dependencies}")
                allow_remove_animal = False

        if allow_remove_animal and animal.movable is False:
            print("Animal is under treatment and cannot be moved.")
            allow_remove_animal = False

        if allow_remove_animal:
            self.__animals.remove(animal)
            print(f"{animal.name} removed from zoo holding pen.")
            return True
        return False


    def check_routine_dependencies_animal(self,animal):
        found_days = []
        for day, routines in self.daily.items():
            for staff, task in routines:
                if task.animal and task.animal.name == animal.name:
                    found_days.append(f"{day} ({staff.name}: {task.name})")
        return ", ".join(found_days) if found_days else None

    def check_animal_dependencies_staff(self, animal):
        found_list = []
        for s in self.staff:
            for task in s.tasks:
                if task.animal == animal:
                    if task.name not in found_list:
                        found_list.append(task.name)
        return ", ".join(found_list) if found_list else None



    def assign_animal(self, animal, enclosure):
        """Assign animal to an enclosure."""
        if animal.movable:
            enclosure.add_occupant(animal)
        else:
            print(f"{animal.name} is under treatment and cannot be moved.")

    def unassign_animal(self, animal, enclosure):
        """Perform validation and then unassign animal from an enclosure."""
        if animal.movable:
            enclosure.remove_occupant(animal)
        else:
            print(f"{animal.name} is under treatment and cannot be moved.")

    def move_animal(self, animal, enclosure_from, enclosure_to):
        """Perform validation then move animal between enclosures."""
        allow_move = True

        if not enclosure_to.can_accept_animal(animal):
            allow_move = False

        if allow_move and not animal.movable:
            print("Animal is under treatment and cannot be moved.")
            allow_move = False

        if allow_move:
            print(f"Moving {animal.name} from {enclosure_from.name} to "
                  f"{enclosure_to.name}:")
            self.unassign_animal(animal, enclosure_from)
            self.assign_animal(animal, enclosure_to)
            return True
        return False

    # Enclosure management
    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)
        print(f"{enclosure.name} added to the zoo.")

    def remove_enclosure(self, enclosure):
        allow_remove_enclosure = True


        if allow_remove_enclosure:
            routine_dependencies = self.check_routine_dependencies_enclosure(enclosure)
            if routine_dependencies:
                print(f"Cannot remove {enclosure.name}. Enclosure is assigned to a related daily routine: {routine_dependencies}")
                allow_remove_enclosure = False

        if allow_remove_enclosure:
            enc_dependencies = self.check_enclosure_dependencies_staff(enclosure)
            if enc_dependencies:
                print(f"Cannot remove {enclosure.name}. Enclosure is assigned to a related daily routine: {enc_dependencies}")
                allow_remove_enclosure = False


        if enclosure.occupants:
            print(f"Cannot remove enclosure. {enclosure.name} still has occupants!")
            allow_remove_enclosure = False

        if allow_remove_enclosure:
            self.enclosures.remove(enclosure)
            print(f"{enclosure.name} has been removed from the zoo.")
            return True
        return False


    def check_enclosure_dependencies_staff(self, enclosure):
        found_list = []
        for s in self.staff:
            for enc in s.enclosures:
                if enc == enclosure:
                    if enc.name not in found_list:
                        found_list.append(enc.name)
        return ", ".join(found_list) if found_list else None

    def check_routine_dependencies_enclosure(self, enclosure):
        found_days = []
        for day, routines in self.daily.items():
            for staff, task in routines:
                if task.enclosure and task.enclosure.name == enclosure.name:
                    found_days.append(f"{day} ({staff.name}: {task.name})")
        return ", ".join(found_days) if found_days else None


    # Staff management

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"{staff.name} the {staff.role} has been added to the Zoo.")

    def remove_staff(self, staff):
        self.staff.remove(staff)
        print(f"{staff.name} the {staff.role} has been removed from the Zoo.")

    def add_task(self, staff, task):

        if staff.add_task(task):
            print(f"Task '{task.name}' added to {staff.name}'s official duties.")

    def remove_task(self, staff, task):
        if staff.remove_task(task):
            print(f"Task '{task.name}' removed from {staff.name}'s official duties.")
        else:
            print(f"Task '{task.name}' is not listed in {staff.name}'s official duties.")

    def assign_staff_enclosure(self, staff, enclosure):
        if enclosure in self.enclosures:
            staff.assign_enclosure(enclosure)
            print(f"{staff.name} assigned to {enclosure.name}")
        else:
            print(f"Enclosure doesn't exist at the zoo")

    def unassign_staff_enclosure(self, staff, enclosure):
        if enclosure in staff.enclosures:
            staff.unassign_enclosure(enclosure)
            print(f"{staff.name} unassigned from {enclosure.name}")
        else:
            print(f"{staff.name} is not assigned to {enclosure.name}")



    def add_to_routine(self, staff, task, day):
        allow_add_to_routine = True

        if task not in staff.tasks:
            print(f"This task is not in {staff.name}'s official list of duties.")
            allow_add_to_routine = False

        if allow_add_to_routine:
            self.daily[day].append((staff, task))
            print(f"{staff.name} '{task.name}' added to {day}")
            return True
        return False

    def clear_routines(self):
        self.__daily_routines = {"Monday": [],
                                 "Tuesday": [],
                                 "Wednesday": [],
                                 "Thursday": [],
                                 "Friday": []}




    def generate_health_record(self, animal, description, record_type, date,
                               status, severity_level, treatment_plan, notes):

        if len(animal.record) == 0:
            dict_first = f"{animal.name}1"
            animal.add_health_record(dict_first, HealthRecord(
                description, record_type, date, status,
                severity_level, treatment_plan, notes))
        else:
            dict_next_record = f"{animal.name}{len(animal.record) + 1}"
            animal.add_health_record(dict_next_record, HealthRecord(
                description, record_type, date, status,
                severity_level, treatment_plan, notes))



    def populate_reports(self):
        reports = []
        reports.append(DailyRoutines("Daily Routine Report"))
        reports.append(AnimalsBySpecies("Animals by Species"))
        reports.append(StatusAllEnclosures("Status of All Enclosures"))



        return reports

    def display_report_interface(self):
        print(f"\n--- Initiating Report Interface ---"
              f"\nPlease select from reports below:\n")
        for i, report in enumerate(self.reports):
            print(f"{i + 1}. {report.name}")

        report_choice = int(input(("Enter number: ")))


        self.reports[report_choice - 1].generate_report(self)









#     validation = does it have any pending cases that check box cant be moved

#remove_routine
# remove_staff
# remove anything else

#
#


#

#

#
# extracuricular

# new arrivals quarantine
# def enclosure_breach
#
#
# def sanitation_protocol
#
#
#
# def visitor_overboard