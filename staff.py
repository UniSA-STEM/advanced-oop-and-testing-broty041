'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Staff:
    def __init__(self, name, role, specialty, assigned_enclosures=None):
        self.__name = name
        self.__role = role
        self.__specialty = specialty
        self.__tasks = []
        self.__assigned_enclosures = assigned_enclosures

    # Getters / Setters

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

    name = property(get_name)
    role = property(get_role, set_role)
    speciality = property(get_specialty)
    tasks = property(get_tasks)
    enclosures = property(get_assigned_enclosures)


    # General staff methods

    def perform_task(self, task):
        if task in self.tasks:
            task.perform_action()
        else:
            print(f"{self.name} does not have task '{task.name}'")

    def list_duties(self):
        print(f"--- {self.name}'s Duties ---")
        if len(self.tasks) > 0:
            for s in self.tasks:
                print(f"{s}"
                      f"\n--------------------")
        else:
            print(f"{self.name} probably needs some duties.")


    def assign_enclosure(self, enclosure):
        allow_assign_enclosure = True



        if self.enclosures is not None and enclosure in self.enclosures:
            print(f"{enclosure.name} already assigned to {self.name}.")
            allow_assign_enclosure = False

        if allow_assign_enclosure and self.speciality not in enclosure.environment:
            print(f"{enclosure.name} is a {enclosure.environment} enclosure."
                  f" {self.name} can only work in {self.speciality} "
                  f"enclosures.")
            allow_assign_enclosure = False

        if allow_assign_enclosure:
            self.__assigned_enclosures = [enclosure]
            return True
        return False



    def unassign_enclosure(self, enclosure):
        allow_unassign_enclosure = True

        if enclosure not in self.enclosures:
            print(f"{enclosure.name} not assigned to {self.name}.")
            allow_unassign_enclosure = False

        for task in self.tasks:
            if allow_unassign_enclosure and task.enclosure == enclosure:
                print(f"{self.name} is assigned duties involving "
                    f"{enclosure.name}. Must remove related duties first.")
                allow_unassign_enclosure = False

        if allow_unassign_enclosure:
            self.__assigned_enclosures.remove(enclosure)
            return True
        return False


        # if self.enclosures:
        #     for e in self.enclosures:
        #         for t in self.duties:
        #             if e == t.enclosure:
        #                 print(f"{self.name} is assigned duties involving "
        #                       f"{enclosure.name}. Must remove related duties first.")





    def add_task(self, task):
        allow_add_task = True

        if self.enclosures is None:
            print(f"{self.name} has not been assigned an enclosure. Unable to perform tasks.")
            allow_add_task = False

        # Check staff doesn't already have the task
        if allow_add_task and task in self.tasks:
            print(f"{self.name} already performs the task {task.name}")
            allow_add_task = False

        # Checking if task is assigned to an enclosure and if the staffs
        # assigned enclosure matches
        if allow_add_task and task.enclosure and task.enclosure not in self.enclosures:
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



# def feed
#

# connection between feed and eat
#
# def clean
#
#
# def health_check
#
#
#
#
