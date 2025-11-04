'''
File: filename.py
Description: A brief description of this Python module.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Staff:
    def __init__(self, name, role, specialty, assigned_enclosures):
        self.__name = name
        self.__role = role
        self.__specialty = specialty
        self.__duties = []
        self.__assigned_enclosures = assigned_enclosures

    # Getters / Setters

    def get_duties(self):
        return self.__duties

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
    duties = property(get_duties)
    enclosures = property(get_assigned_enclosures)


    # General staff methods
    def add_duty(self, task):
        allow_add_duty = True

        # Check staff doesn't already have the task
        if task in self.duties:
            print(f"{self.name} already performs the task {task.name}")
            allow_add_duty = False

        # Checking if task is assigned to an enclosure and if the staffs
        # assigned enclosure matches
        if allow_add_duty and task.enclosure and task.enclosure not in self.enclosures:
            print(f"{self.name} is not assigned to {task.enclosure}")
            allow_add_duty = False

        # Check if staff can do a task based on their role
        if allow_add_duty and self.role not in task.roles:
            print(f"{self.role[0]}s are not able to perform task '{task.name}'")
            allow_add_duty = False

        if allow_add_duty:
            self.__duties.append(task)
            print(f"Task '{task.name}' added to {self.name}'s official duties.")
            return True
        return False



    def __str__(self):
        return (f"--- Staff Details ---"
                f"\nName: {self.name}"
                f"\nRole: {self.role}"
                f"\nSpecialty: {self.speciality}")

    def __repr__(self):
        return f"{self.__name}"

class Zookeeper(Staff):
    def __init__(self, name, role, specialty, assigned_enclosures):
        super().__init__(name, role, specialty, assigned_enclosures)


class Vet(Staff):
    def __init__(self, name, role, specialty, assigned_enclosures):
        super().__init__(name, role, specialty, assigned_enclosures)

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
