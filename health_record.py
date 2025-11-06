'''
File: health_record.py
Description: Generates records stored on animals that contain
information from a health event.
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''


class HealthRecord:
    # Class Docstring
    """
    HealthRecord represents a single record containing information such as an
    illness, injury, behavioural problem etc.

    Attributes
    ----------
    __record_id : str
        Unique ID for health record.
    __description : str
        Summary of the health issue.
    __record_type : str
        Type of record ('Injury,' 'Illness').
    __date : str
        Date created.
    __status : str
        Current state of health issue ('Active', 'Closed').
    __severity_level : int
        Numeric seriousness of health issue.
    __treatment_plan : str
        How the patients health issue will be managed.
    __notes : str
        Additional comments.

    Methods
    -------
        Basic getters and setters.
    """

    def __init__(self, description, record_type, date, status,
                 severity_level, treatment_plan, notes):
        self.__record_id = ""
        self.__description = description
        self.__record_type = record_type
        self.__date = date
        self.__status = status
        self.__severity_level = severity_level
        self.__treatment_plan = treatment_plan
        self.__notes = notes

    # --- Getters and Setters ---
    def get_record_id(self):
        return self.__record_id

    def set_record_id(self, new_record_id):
        self.__record_id = new_record_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_severity_level(self):
        return self.__severity_level

    def set_severity_level(self, change):
        self.__severity_level = change

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def get_treatment_plan(self):
        return self.__treatment_plan

    def set_treatment_plan(self, new_plan):
        self.__treatment_plan = new_plan

    # --- Property Attributes ---
    record_id = property(get_record_id, set_record_id)
    status = property(get_status, set_status)
    severity = property(get_severity_level, set_severity_level)
    date = property(get_date)
    description = property(get_description)
    plan = property(get_treatment_plan, set_treatment_plan)

    def __repr__(self):
        return f"{self.__description}{self.__status}"

    def __str__(self):
        return f"{self.__description}{self.__status}"
