'''
File: zoo_operations.py
Description: Orchestrates the management of animals, enclosures, staff,
tasks, health records and reports for the zoo.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from health_record import HealthRecord
from report import (ReportSystem, DailyRoutines,
                    AnimalsBySpecies, StatusAllEnclosures)


class Zoo:
    # Class Docstring
    """
    Zoo orchestrates management of all animals, enclosures, staff,
     daily routines, and reports.

    Attributes
    ----------
    __name : str
        Zoo name.
    __animals : list
        List of animal objects within entire zoo.
    __enclosures : list
        List of enclosure objects.
    __staff : list
        List of staff objects.
    __daily_routines : dict
        Maps weekdays to lists of staff/task tuples.
    __reports : object
        Stores report.

    Methods
    -------
    find_animal(animal):
        Locate animal by name or object.
    list_zoo_animals():
        Display zoo animals.
    list_staff():
        Display staff members.
    add_animal(animal):
        Add new animal to zoo.
    remove_animal(animal, enclosure):
        Remove animal.
    assign_animal(animal, enclosure):
        Assign animal to an enclosure.
    unassign_animal(animal, enclosure):
        Remove animal from an enclosure.
    move_animal(animal, enclosure_from, enclosure_to):
        Move animal between enclosures.
    add_enclosure(enclosure):
        Add new enclosure to zoo.
    remove_enclosure(enclosure):
        Remove enclosure.
    add_staff(staff):
        Add staff member to zoo.
    remove_staff(staff):
        Remove staff member from zoo.
    add_task(staff, task):
        Assign task to staff.
    remove_task(staff, task):
        Remove task from staff.
    assign_staff_enclosure(staff, enclosure):
        Assign staff to enclosure.
    unassign_staff_enclosure(staff, enclosure):
        Unassign staff from enclosure.
    add_to_routine(staff, task, day):
        Add staff and task pair to daily routine.
    clear_routines():
        Clear all daily routines.
    generate_health_record(animal, ...):
        Create health record for animal.
    populate_reports():
        Initialise available reports.
    display_report_interface():
        Display report interface.
    __check_routine_dependencies_animal(animal):
        Check whether animal appears in any daily routines.
    __check_animal_dependencies_staff(animal):
        Check if animal appears in any staff tasks.
    __check_routine_dependencies_enclosure(enclosure)
        Check if enclosure appears in any daily routines.
    __check_enclosure_dependencies_staff(enclosure):
        Check if enclosure appears in any staff tasks
    __check_routine_dependencies_task(task):
        Check if task appears in any daily routines.
    """

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
        # Initialise with current list of reports
        self.__reports = self.populate_reports()

    # --- Getters and Setters ---
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

    # --- Property Attributes ---
    animals = property(get_animals)
    daily = property(get_daily_routines)
    reports = property(get_reports)
    enclosures = property(get_enclosures)
    staff = property(get_staff)

    # --- Animal Management ---
    def find_animal(self, animal):
        """
        Find an animal with either a string or object as a parameter.

            Parameters:
                animal (object or str): Animal to find.

            Returns:
                object: Animal if found, otherwise None.
        """

        if not isinstance(animal, (Animal, str)):
            raise TypeError("Animal object or string "
                            "name of animal expected")

        find_ref = animal.name if isinstance(animal, Animal) else animal
        for a in self.__animals:
            if a.name == find_ref:
                return a
        return None

    def list_zoo_animals(self):
        """
        Display all animals currently in the zoo.

            Parameters:
                None

            Returns:
                None. (Prints list of zoo animals.)
        """
        print('--- Zoo Animals ---')
        if len(self.__animals) > 0:
            for a in self.animals:
                print(f"{a}"
                      f"\n--------------------")
        else:
            print("Matt Damon would be disappointed, you need animals in "
                  "your zoo!")

    def add_animal(self, animal):
        """
        Perform validation and then add animal to the zoo.

            Parameters:
                animal (object): Animal to add.

            Returns:
                bool: True if added successfully, otherwise False.
        """

        allow_add_animal = True

        # Ensure passed object is an animal
        if not isinstance(animal, Animal):
            print("Ensure animal object exists.")
            allow_add_animal = False

        # Prevent duplicates
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
        """
        Perform validation and then remove animal from zoo.

            Parameters:
                animal (object): Animal to remove.
                enclosure (object): Enclosure animal removed from.

            Returns:
                bool: True if removal successful, otherwise False.
        """

        allow_remove_animal = True

        # Ensure passed object is an animal
        if not self.find_animal(animal):
            print(f"Animal is not in {enclosure.name}")
            allow_remove_animal = False

        # Dependency check in animal is part of any daily routine entries
        if allow_remove_animal:
            routine_dependencies = (
                self.__check_routine_dependencies_animal(animal))
            if routine_dependencies:
                print(f"Cannot remove {animal.name}. Animal is"
                      f" assigned to daily routines: {routine_dependencies}")
                allow_remove_animal = False

        # Dependency check in animal is part of any current staff tasks
        if allow_remove_animal:
            staff_dependencies = self.__check_animal_dependencies_staff(animal)
            if staff_dependencies:
                print(f"Cannot remove {animal.name}. Animal is"
                      f" assigned to staff tasks: {staff_dependencies}")
                allow_remove_animal = False

        # Check if animal can be moved
        if allow_remove_animal and animal.movable is False:
            print("Animal is under treatment and cannot be moved.")
            allow_remove_animal = False

        if allow_remove_animal:
            self.__animals.remove(animal)
            print(f"{animal.name} removed from zoo holding pen.")
            return True
        return False

    def __check_routine_dependencies_animal(self, animal):
        """
        Check if animal appears in any daily routine.

            Parameters:
                animal (object): Animal to check.

            Returns:
                str:    Comma sep string of dependencies found that
                        need to be addressed.
        """

        # Iterate over the staff and tasks in dailyroutines and list the
        # ones in conflict
        found_days = []
        for day, routines in self.daily.items():
            for staff, task in routines:
                if task.animal and task.animal.name == animal.name:
                    found_days.append(f"{day} ({staff.name}: {task.name})")
        return ", ".join(found_days) if found_days else None

    def __check_animal_dependencies_staff(self, animal):
        """
        Check if animal appears in any staff tasks.

            Parameters:
                animal (object): Animal to check.

            Returns:
                str:    Comma sep string of dependencies found that
                        need to be addressed.
        """

        # Iterate over staff tasks and list the ones in conflict
        found_list = []
        for s in self.staff:
            for task in s.tasks:
                if task.animal == animal:
                    if task.name not in found_list:
                        found_list.append(task.name)
        return ", ".join(found_list) if found_list else None

    def assign_animal(self, animal, enclosure):
        """
        Assign animal to enclosure.

            Parameters:
                animal (object): Animal to assign.
                enclosure (object): Enclosure animal is going to.

            Returns:
                None: (Adds animal or prints error message.)
        """
        allow_assign_animal = True

        # Check animal movable
        if not animal.movable:
            print(f"{animal.name} is under treatment and cannot be moved.")
            allow_assign_animal = False

        if allow_assign_animal and enclosure not in self.enclosures:
            print(f"There is no enclosure '{enclosure.name}' attached to "
                  f"the zoo for {animal.name} to be housed in.")
            allow_assign_animal = False

        if allow_assign_animal:
            enclosure.add_occupant(animal)
            return True
        return False

    def unassign_animal(self, animal, enclosure):
        """
        Perform validation and then unassign animal from an enclosure.

            Parameters:
                animal (object): Animal to remove.
                enclosure (object): Enclosure to remove animal from.

            Returns:
                None: (Removes animal from enclosure or print message.)
        """

        # Check animal movable
        if animal.movable:
            enclosure.remove_occupant(animal)
        else:
            print(f"{animal.name} is under treatment and cannot be moved.")

    def move_animal(self, animal, enclosure_from, enclosure_to):
        """
        Perform validation then move animal between enclosures.

            Parameters:
                animal (object): Animal to move.
                enclosure_from (object): Enclosure moving animal from.
                enclosure_to (object): Enclosure moving animal to

            Returns:
                bool: True if move successful, otherwise False.
        """

        allow_move = True

        # Check 'to' enclosure can accept animal.
        if not enclosure_to.can_accept_animal(animal):
            allow_move = False

        # Check animal can move
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

    # --- Enclosure Management ---
    def add_enclosure(self, enclosure):
        """
        Add new enclosure to zoo.

            Parameters:
                enclosure (object): Enclosure to add.

            Returns:
                None: (Append enclosure, print confirmation.)
        """

        self.__enclosures.append(enclosure)
        print(f"{enclosure.name} added to the zoo.")

    def remove_enclosure(self, enclosure):
        """
        Remove enclosure if no dependencies exist.

            Parameters:
                enclosure (object): Enclosure to remove.

            Returns:
                bool: True if removal successful, otherwise False.
        """

        allow_remove_enclosure = True

        # Dependency check enclosure is part of any daily routine entries
        if allow_remove_enclosure:
            routine_dependencies = (
                self.__check_routine_dependencies_enclosure(enclosure))
            if routine_dependencies:
                print(
                    f"Cannot remove {enclosure.name}."
                    f" Enclosure is assigned to a related"
                    f" daily routine: {routine_dependencies}")
                allow_remove_enclosure = False

        # Dependency check enclosure is part of any current staff tasks
        if allow_remove_enclosure:
            enc_dependencies = self.__check_enclosure_dependencies_staff(enclosure)
            if enc_dependencies:
                print(
                    f"Cannot remove {enclosure.name}."
                    f" Enclosure is assigned to a"
                    f" related staff task: {enc_dependencies}")
                allow_remove_enclosure = False

        # Check if enclosure has occupants
        if enclosure.occupants:
            print(f"Cannot remove enclosure. {enclosure.name}"
                  f" still has occupants!")
            allow_remove_enclosure = False

        if allow_remove_enclosure:
            self.enclosures.remove(enclosure)
            print(f"{enclosure.name} has been removed from the zoo.")
            return True
        return False

    def __check_enclosure_dependencies_staff(self, enclosure):
        """
        Check if enclosure is assigned to any staff.

            Parameters:
                enclosure (object): Enclosure to check.

            Returns:
                str:    Comma sep string of dependencies found that
                        need to be addressed.
        """

        # Iterate over staff tasks and list the ones in conflict
        found_list = []
        for s in self.staff:
            for task in s.tasks:
                if task.enclosure == enclosure:
                    if task.name not in found_list:
                        found_list.append(task.name)
        return ", ".join(found_list) if found_list else None

    def __check_routine_dependencies_enclosure(self, enclosure):
        """
        Check if enclosure appears in any daily routine.

            Parameters:
                enclosure (object): Enclosure to check.

            Returns:
                str:    Comma sep string of dependencies found that
                        need to be addressed.
        """
        # Iterate over the staff and tasks in dailyroutines and list the
        # ones in conflict
        found_days = []
        for day, routines in self.daily.items():
            for staff, task in routines:
                if task.enclosure and task.enclosure.name == enclosure.name:
                    found_days.append(f"{day} ({staff.name}: {task.name})")
        return ", ".join(found_days) if found_days else None

    # --- Staff Management ---
    def list_staff(self):
        """
        Display list of zoo staff members

            Parameters:
                None

            Returns:
                None. (Prints list of zoo staff.)
        """

        print('--- Zoo Staff ---')
        if len(self.__staff) > 0:
            for s in self.staff:
                print(f"{s}"
                      f"\n--------------------")
        else:
            print("You probably need some staff.")

    def add_staff(self, staff):
        """
        Add staff member to zoo roster.

            Parameters:
                staff (object): Staff to add.

            Returns:
                None: (Print confirmation.)
        """

        self.staff.append(staff)
        print(f"{staff.name} the {staff.role} has been added to the Zoo.")

    def remove_staff(self, staff):
        """
        Remove staff from zoo roster.

            Parameters:
                staff (object): Staff to remove.

            Returns:
                None: (Prints confirmation.)
        """

        self.staff.remove(staff)
        print(f"{staff.name} the {staff.role} has been removed from the Zoo.")

    def add_task(self, staff, task):
        """
        Assign task to staff member.

            Parameters:
                staff (object): Staff performing task.
                task (object):  Task to assign.

            Returns:
                None: (Prints confirmation.)
        """

        if staff.add_task(task):
            print(f"Task '{task.name}' added"
                  f" to {staff.name}'s official tasks.")

    def remove_task(self, staff, task):
        """
        Remove task from staff member.

            Parameters:
                staff (object): Staff task to remove.
                task (object):  Task to remove.

            Returns:
                None: (Print confirmation or warning.)
        """
        allow_remove_task = True

        # Dependency check task is part of any daily routine entries
        if allow_remove_task:
            routine_dependencies = self.__check_routine_dependencies_task(task)
            if routine_dependencies:
                print(
                    f"Cannot remove {task.name}. Task is"
                    f" assigned to a related"
                    f" daily routine: {routine_dependencies}")
                allow_remove_task = False

        # Check task not already in staff tasks
        if allow_remove_task and task not in staff.tasks:
            print(f"Task '{task.name}' is not listed in"
                  f" {staff.name}'s official tasks.")
            allow_remove_task = False

        if allow_remove_task:
            staff.remove_task(task)
            print(f"Task '{task.name}' removed from"
                  f" {staff.name}'s official tasks.")
            return True
        return False

    def __check_routine_dependencies_task(self, check_task):
        """
        Check if task appears in any daily routine.

            Parameters:
                animal (object): Animal to check.

            Returns:
                str:    Comma sep string of dependencies found that
                        need to be addressed.
        """

        # Iterate over the staff and tasks in dailyroutines and list the
        # ones in conflict
        found_days = []
        for day, routines in self.daily.items():
            for staff, task in routines:
                if task.name == check_task.name:
                    found_days.append(f"{day} ({staff.name}: {task.name})")
        return ", ".join(found_days) if found_days else None

    def assign_staff_enclosure(self, staff, enclosure):
        """
        Assign staff to existing enclosure.

            Parameters:
                staff (object): Staff to assign.
                enclosure (object): Enclosure to assign staff.

            Returns:
                None: (Prints confirmation or error.)
        """

        if enclosure in self.enclosures:
            staff.assign_enclosure(enclosure)
            print(f"{staff.name} assigned to {enclosure.name}")
        else:
            print(f"Enclosure doesn't exist at the zoo")

    def unassign_staff_enclosure(self, staff, enclosure):
        """
        Unassign staff from enclosure.

            Parameters:
                staff (object): Staff to unassign.
                enclosure (object): Enclosure staff removed from.

            Returns:
                None: (Prints confirmation or warning.)
        """
        # Check if staff assigned to enclosure
        if enclosure in staff.enclosures:
            staff.unassign_enclosure(enclosure)
            print(f"{staff.name} unassigned from {enclosure.name}")
        else:
            print(f"{staff.name} is not assigned to {enclosure.name}")

    def add_to_routine(self, staff, task, day):
        """
        Add staff and task pair to a day's routine.

            Parameters:
                staff (object): Staff performing task.
                task (object):  Task to assign.
                day (str):      Day for task.

            Returns:
                bool: True if successfully added, otherwise False.
        """

        allow_add_to_routine = True

        # Check staff has task
        if task not in staff.tasks:
            print(f"This task is not in {staff.name}'s"
                  f" official list of tasks.")
            allow_add_to_routine = False

        if allow_add_to_routine:
            self.daily[day].append((staff, task))
            print(f"{staff.name} '{task.name}' added to {day}")
            return True
        return False

    def clear_routines(self):
        """
        Reset all daily routines to default.

            Parameters:
                None

            Returns:
                None: (Resets routines.)
        """

        self.__daily_routines = {"Monday": [],
                                 "Tuesday": [],
                                 "Wednesday": [],
                                 "Thursday": [],
                                 "Friday": []}

    def generate_health_record(self, animal, description,
                               record_type, date, status,
                               severity_level, treatment_plan,
                               notes):
        """
        Generate and attach health record to an animal.

            Parameters:
                animal (object): Animal receiving record.
                description (str): Summary health issue.
                record_type (str): Type of record.
                date (str): Date record created.
                status (str): Current health status.
                severity_level (int): Severity.
                treatment_plan (str): Treatment.
                notes (str): Additional comments.

            Returns:
                None: (Add record to animal.)
        """

        # Maintaining incrementing record id based off animals name
        # First is name1
        if len(animal.record) == 0:
            dict_first = f"{animal.name}1"
            animal.add_health_record(dict_first, HealthRecord(
                description, record_type, date, status,
                severity_level, treatment_plan, notes))

        # All others increment by 1
        else:
            dict_next_record = f"{animal.name}{len(animal.record) + 1}"
            animal.add_health_record(dict_next_record, HealthRecord(
                description, record_type, date, status,
                severity_level, treatment_plan, notes))

    def populate_reports(self):
        """
        Initialise and register all report.

            Parameters:
                None

            Returns:
                object: Populate with registered reports.
        """

        reports = ReportSystem()
        reports.register(DailyRoutines("Daily Routine Report"))
        reports.register(AnimalsBySpecies("Animals by Species"))
        reports.register(StatusAllEnclosures("Status of All Enclosures"))

        return reports

    def display_report_interface(self):
        """
        Display interface for generating reports.

            Parameters:
                None

            Returns:
                None: (Prompts user select report.)
        """

        print(f"\n--- Initiating Report Interface ---"
              f"\nPlease select from reports below:\n")
        for i, report in enumerate(self.reports.reports):
            print(f"{i + 1}. {report.name}")

        # Try/catch for invalid use inputs
        try:
            report_choice = int(input(("Enter number: ")))
            if 1 <= report_choice <= len(self.reports.reports):
                self.reports.reports[report_choice - 1].generate_report(self)
            else:
                print(f"\nNumber not listed.")
                self.display_report_interface()
        except ValueError:
            print("\nInvalid input. Try again.")
            self.display_report_interface()
