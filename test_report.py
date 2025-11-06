'''
File: test_report.py
Description: Testing for report.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from report import ReportSystem, DailyRoutines, AnimalsBySpecies, StatusAllEnclosures


@pytest.fixture
def report_system():
    """Instantiate a ReportSystem for testing."""
    return ReportSystem()

@pytest.fixture()
def report_daily_routines():
    """Instantiate a Report for testing."""
    return DailyRoutines("Daily Routine Report")

@pytest.fixture()
def report_animals_species():
    """Instantiate a Report for testing."""
    return AnimalsBySpecies("Animals by Species")

@pytest.fixture()
def report_status_enclosures():
    """Instantiate a Report for testing."""
    return StatusAllEnclosures("Status of All Enclosures")


def test_create_report_system(report_system):
    """Test that report system is instantiated."""
    assert report_system.reports == []

def test_register_of_daily_report(report_system, report_daily_routines):
    report_system.register(report_daily_routines)
    assert len(report_system.reports) == 1

def test_register_of_animal_report(report_system, report_animals_species):
    report_system.register(report_animals_species)
    assert len(report_system.reports) == 1

def test_register_of_enclosure_report(report_system, report_status_enclosures):
    report_system.register(report_status_enclosures)
    assert len(report_system.reports) == 1