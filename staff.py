'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Staff:
    # Class Docstring
    """
    Staff work at the zoo and perform tasks on animals and enclosures.

    Attributes
    ----------
    __name : str
        Staff name.
    __role : str
        Staff role in zoo (Zoo keeper, Vet).
    __specialty : str
        Environment the staff specialises in.
    __tasks : list
        Responsibilities of the staff member.
    __assigned_enclosures : list
        Enclosures this staff member is assigned to.

    Methods
    -------
    assign_enclosure(enclosure):
        Assign staff to an enclosure.
    unassign_enclosure(enclosure):
        Remove staff from assigned enclosure.
    perform_task(task):
        Perform a task already assigned to staff.
    list_tasks():
        Display list of staffs tasks.
    add_task(task):
        Add task to task list.
    remove_task(task):
        Remove an existing task.
    """

    def __init__(self, name, role, specialty, assigned_enclosures=None):
        self.__name = name
        self.__role = role
        self.__specialty = specialty
        self.__tasks = []
        self.__assigned_enclosures = assigned_enclosures

    # --- Getters and Setters ---
    def get_tasks(self):
        return self.__tasks

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = [role]

    def get_specialty(self):
        return self.__specialty

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    # --- Property Attributes ---
    name = property(get_name)
    role = property(get_role, set_role)
    speciality = property(get_specialty)
    tasks = property(get_tasks)
    enclosures = property(get_assigned_enclosures)

    # --- General staff methods ---
    def assign_enclosure(self, enclosure):
        """
        Assigns staff to enclosure after validation.

            Parameters:
                enclosure (object): Enclosure to assign.

            Returns:
                bool: True if assignment successful.
        """

        allow_assign_enclosure = True

        # Prevent duplicate assignments.
        if self.enclosures is not None and enclosure in self.enclosures:
            print(f"{enclosure.name} already assigned to {self.name}.")
            allow_assign_enclosure = False

        # Ensure enclosure environ matches staff specialty
        if (allow_assign_enclosure and self.speciality
                not in enclosure.environment):
            print(f"{enclosure.name} is a {enclosure.environment} enclosure."
                  f" {self.name} can only work in {self.speciality} "
                  f"enclosures.")
            allow_assign_enclosure = False

        if allow_assign_enclosure:
            self.__assigned_enclosures = [enclosure]
            return True
        return False

    def unassign_enclosure(self, enclosure):
        """
        Unassigns staff from enclosure.

            Parameters:
            enclosure (object): Enclosure to unassign.

            Returns:
                bool: True if unassignment successful, otherwise False.
        """

        allow_unassign_enclosure = True

        # Ensure staff is actually assigned
        if enclosure not in self.enclosures:
            print(f"{enclosure.name} not assigned to {self.name}.")
            allow_unassign_enclosure = False

        # Dependency check staff doesnt have related tasks
        for task in self.tasks:
            if allow_unassign_enclosure and task.enclosure == enclosure:
                print(f"{self.name} is assigned tasks involving "
                      f"{enclosure.name}. Must remove related tasks first.")
                allow_unassign_enclosure = False

        if allow_unassign_enclosure:
            self.__assigned_enclosures.remove(enclosure)
            return True
        return False

    # --- Task Methods ---
    def perform_task(self, task):
        """
        Perform task if staff member is assigned.

            Parameters:
                task (object): The task object to perform.

            Returns:
                None: (Calls the task’s perform_action() method.)
        """

        # Make sure staff has the task
        if task in self.tasks:
            task.perform_action()
        else:
            print(f"{self.name} does not have task '{task.name}'")

    def list_tasks(self):
        """
        Display list of staffs current tasks.

            Parameters:
                None

            Returns:
                None: (Prints task names.)
        """

        print(f"--- {self.name}'s Tasks ---")
        if len(self.tasks) > 0:
            for s in self.tasks:
                print(f"{s}"
                      f"\n--------------------")
        else:
            print(f"{self.name} probably needs some tasks.")

    def add_task(self, task):
        """
        Adds new task to the staff member if valid.

            Parameters:
            task (object): Task  to assign.

            Returns:
                bool: True if task added, otherwise False.
        """

        allow_add_task = True

        # CHeck staff assigned enclosure
        if self.enclosures is None:
            print(f"{self.name} has not been assigned an enclosure. "
                  f"Unable to perform tasks.")
            allow_add_task = False

        # Check staff doesn't already have the task
        if allow_add_task and task in self.tasks:
            print(f"{self.name} already performs the task {task.name}")
            allow_add_task = False

        # Checking if task is assigned to an enclosure and if the staffs
        # assigned enclosure matches
        if (allow_add_task and task.enclosure
                and task.enclosure not in self.enclosures):
            print(f"{self.name} is not assigned to {task.enclosure}")
            allow_add_task = False

        # Check if staff can do a task based on their role
        if allow_add_task and self.role not in task.roles:
            print(f"{self.role}s are not able to perform task '{task.name}'")
            allow_add_task = False

        if allow_add_task:
            self.__tasks.append(task)
            return True
        return False

    def remove_task(self, task):
        """
        Remove a task from staff task list.

            Parameters:
            task (object): Task to remove.

            Returns:
                bool: True if removed , otherwise False.
        """

        # Check staff has task
        if task in self.tasks:
            self.__tasks.remove(task)
            return True
        else:
            return False

    def __str__(self):
        return (f"Name: {self.name}"
                f"\nRole: {self.role}"
                f"\nSpecialty: {self.speciality}")

    def __repr__(self):
        return f"{self.__name}"
