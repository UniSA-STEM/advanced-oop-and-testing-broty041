'''
File: test_report.py
Description: Testing for report.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest

from report import (ReportSystem, DailyRoutines,
                    AnimalsBySpecies, StatusAllEnclosures)


class TestReport:
    @pytest.fixture
    def report_system(self):
        """Instantiate a ReportSystem for testing."""
        return ReportSystem()

    @pytest.fixture()
    def report_daily_routines(self):
        """Instantiate a Report for testing."""
        return DailyRoutines("Daily Routine Report")

    @pytest.fixture()
    def report_animals_species(self):
        """Instantiate a Report for testing."""
        return AnimalsBySpecies("Animals by Species")

    @pytest.fixture()
    def report_status_enclosures(self):
        """Instantiate a Report for testing."""
        return StatusAllEnclosures("Status of All Enclosures")

    def test_create_report_system(self, report_system):
        """Test that report system is instantiated."""
        assert report_system.reports == []

    def test_register_of_daily_report(self, report_system,
                                      report_daily_routines):
        """Test that daily report is registered."""
        report_system.register(report_daily_routines)
        assert len(report_system.reports) == 1

    def test_register_of_animal_report(self, report_system,
                                       report_animals_species):
        """Test that animal report is registered."""
        report_system.register(report_animals_species)
        assert len(report_system.reports) == 1

    def test_register_of_enclosure_report(self, report_system,
                                          report_status_enclosures):
        """Test that enclosure report is registered."""
        report_system.register(report_status_enclosures)
        assert len(report_system.reports) == 1
