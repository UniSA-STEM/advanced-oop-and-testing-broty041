'''
File: test_health_record.py
Description: Testing for health_record.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from health_record import HealthRecord

@pytest.fixture()
def dummy_health_record():
    """Create a health record for testing."""
    return HealthRecord(
            description="Bump on head",
            record_type="Injury",
            date="12/12/12",
            status="Active",
            severity_level=3,
            treatment_plan="Rest",
            notes="Ran into fence."
        )

def test_dummy_health_record(dummy_health_record):
    """Test HealthRecord initializes correctly."""
    assert dummy_health_record.description == "Bump on head"
    assert dummy_health_record.severity == 3


def test_set_record_id(dummy_health_record):
    """Test setting record id."""
    dummy_health_record.record_id = "asdf1"
    assert dummy_health_record.record_id == "asdf1"

def test_set_status(dummy_health_record):
    """Test setting record status."""
    dummy_health_record.status = "Closed"
    assert dummy_health_record.status == "Closed"

def test_get_date(dummy_health_record):
    """Test using get_date method"""
    assert dummy_health_record.date == "12/12/12"

