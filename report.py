'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class ReportSystem:
    # Class Docstring
    """
    ReportSystem manages available reports that can be registered,
    retrieved, and generated.

    Attributes
    ----------
    __reports: list
        List registered reports.

    Methods
    -------
        register(report):
            Register a report object.
        get_reports():
            Return all registered reports.
        generate(report_name, zoo):
            Generate report by name.
    """

    def __init__(self):
        self.__reports = []

    def register(self, report):
        self.__reports.append(report)

    def get_reports(self):
        return self.__reports

    def generate(self, report_name, zoo):
        # Search through registered reports to find matching name
        for report in self.__reports:
            if report.name == report_name:
                return report.generate_report(zoo)
        return None

    # --- Property Attributes ---
    reports = property(get_reports)


class Report(ABC):
    # Class Docstring
    """
    Abstract base class for all report types.

    Attributes
    ----------
    __name : str
        Report name.

    Methods
    -------
    generate_report(zoo):
        Abstract method for child classes to expand.
    """

    def __init__(self, name):
        self.__name = name

    # Getters / Setters
    def get_name(self):
        return self.__name

    # --- Property Attributes ---
    name = property(get_name)

    @abstractmethod
    def generate_report(self, zoo):
        pass


class DailyRoutines(Report):
    # Class Docstring
    """
    Generates a readable daily routine report.

    Iterates over zoo operations daily_routine dictionary. Each day
    maps to a list of tuples, each tuple is the staff member
     (object) and their task (object), calls .name property of each.

    Methods
    -------
    generate_report(zoo):
    Generate daily routine report.
    """

    def generate_report(self, zoo):
        """
        Generates daily routine report.

            Parameters:
                zoo (object): Zoo provides daily routines.

            Returns:
                None. (Prints formatted staff and task schedules.)
        """

        print("\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-\n"
              "-=-=- Welcome to the Daily Routine Report -=-=-"
              "\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")

        for day, routine in zoo.daily.items():
            if routine:
                # Handles both single tasks and task lists per staff member
                routine_formatted = " || ".join(
                    f"{staff.name}, {task.name}"
                    for staff, task_list in routine
                    for task in (task_list if isinstance(task_list, list)
                                 else [task_list])
                )
            else:
                routine_formatted = ""

            print(f"{day}: {routine_formatted}")


class AnimalsBySpecies(Report):
    # Class Docstring
    """
    Generates a report listing all zoo animals by species. Iterates over
    list of animals in the zoo, places in dictionary and sorts in alpha
    order.

    Methods
    -------
    generate_report(zoo):
        Generates zoo animals by species report.
    """

    def generate_report(self, zoo):
        """
        Generates zoo animals by species report.
            Parameters:
                zoo (object): Zoo provides list of animals.

            Returns:
                None. (Prints sorted animals by species.)
        """
        print("\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-\n"
              "-=-=-   List of Zoo Animals by Species  -=-=-"
              "\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")
        # Group animals by species
        animals_dict = {}
        for a in zoo.animals:
            if a.species not in animals_dict:
                animals_dict[a.species] = [a]
            else:
                animals_dict[a.species].append(a)

        # Sort alpha order by species name
        sorted_dict = dict(sorted(animals_dict.items()))

        for species, animals in sorted_dict.items():
            print(f"        --- {species} ---")
            for a in animals:
                print(f"--------------------------------"
                      f"\nNickname: {a.name}"
                      f"\nAnimal Class: {a.animal_class}"
                      f"\nGender: {a.gender}"
                      f"\nAge: {a.age}"
                      f"\nDiet: {a.diet}"
                      f"\nEnvironment: {a.environment}"
                      f"\n--------------------------------")


class StatusAllEnclosures(Report):
    # Class Docstring
    """
    StatusAllEnclosures displays a summary of each enclosure’s condition
    and its current occupants. Iterates over list of enclosures in zoo.

    Methods
    -------
    generate_report(zoo):
        Generates status of all enclosures report.
    """

    def generate_report(self, zoo):
        """
        Displays status of all enclosures and occupants.
            Parameters:
                zoo (object): Zoo provides list of enclosures.

            Returns:
                None. (Prints status of all enclosures.)
        """

        print("\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-\n"
              "-=-=-      Status of All Enclosures     -=-=-"
              "\n-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")

        for enclosure in zoo.enclosures:
            print(f"--- {enclosure.name}: ---"
                  f"\nStatus: {enclosure.status}")

            # Comma seperated string of enclosures for readability.
            occupants_enc = ", ".join(str(occupant.name) for
                                      occupant in enclosure.occupants)
            print(f"Occupants: "
                  f"{occupants_enc if occupants_enc else 'None'}\n")
