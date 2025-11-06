'''
File: task.py
Description: Create tasks for use by zoo staff.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod


class Task(ABC):
    # Class Docstring
    """
    Task is an abstract base class representing a task that staff perform
    such as feeding.

    Attributes
    ----------
    __name : str
        Task name.
    __description : str
        Description of task.
    __assigned_enclosure : object
        Enclosure the task is related to.
    __roles : list
        Staff roles required to perform task.
    __animal : object
        Animal related to the task.

    Methods
    -------
        perform_action():
            Abstract method for child classes. Represents the core action
            the task performs.
    """

    def __init__(self, name, description, roles=None,
                 assigned_enclosure=None, animal=None):
        self.__name = name
        self.__description = description
        self.__assigned_enclosure = assigned_enclosure
        self.__roles = roles
        self.__animal = animal

    # --- Getters and Setters ---
    def get_name(self):
        return self.__name

    def get_roles(self):
        return self.__roles

    def get_assigned_enclosure(self):
        return self.__assigned_enclosure

    def set_assigned_enclosure(self, enclosure):
        self.__assigned_enclosure = enclosure

    def get_animal(self):
        return self.__animal

    # --- Property Attributes ---
    name = property(get_name)
    roles = property(get_roles)
    enclosure = property(get_assigned_enclosure, set_assigned_enclosure)
    animal = property(get_animal)

    @abstractmethod
    def perform_action(self):
        pass

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__name}"


class Feed(Task):
    # Class Docstring
    """
    Perform feeding task within an enclosure.

    Methods
    -------
    perform_action():
        Calls feed_animals() on the assigned enclosure. Feeds animals.
    """

    def __init__(self, name, description, roles=None,
                 assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles,
                         assigned_enclosure, animal)

    def perform_action(self):
        """
        Performs feeding for enclosure.

            Parameters:
                None

            Returns:
                None: (Calls enclosures feed_animals() method.)
        """
        self.enclosure.feed_animals()


class Surgery(Task):
    # Class Docstring
    """
    Surgery is performed on an animal with the animal performing validation
    and other logic.

    Methods
    -------
    perform_action():
        Perform surgery, else print message.
    """

    def __init__(self, name, description, roles,
                 assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles,
                         assigned_enclosure, animal)

    def get_health_record(self):
        return self.__health_record

    def perform_action(self):
        """
        Perform surgery if validation true.

            Parameters:
                None

            Returns:
                None: (Prints surgery outcome message.)
        """

        # Perform validation check in animal class whether surgery is needed
        if self.animal.adjust_status_after_surgery():
            print(f"Surgery is performed on {self.animal.name} the "
                  f"{self.animal.species} and is successful.")
        else:
            print(f"{self.animal.name} the {self.animal.species} does not "
                  f"need surgery. Please confirm with Veterinarian.")


class HealthCheck(Task):
    """
    HealthCheck examines animals ongoing health issues if any. Logic
    performed in the animals class.

    Methods
    -------
    perform_action():
        Performs animal health check.
    """

    def __init__(self, name, description, roles,
                 assigned_enclosure=None, animal=None):
        super().__init__(name, description, roles,
                         assigned_enclosure, animal)

    def perform_action(self):
        """
        Performs health check on animal.

            Parameters:
                None

            Returns:
                None: (Calls animal's check_health() method.)
        """

        # Logic done by the animal
        self.animal.check_health()
