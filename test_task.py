'''
File: test_task.py
Description: Testing for task.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from task import Surgery, Feed, HealthCheck

@pytest.fixture()
def dummy_feed_task():
    """Creating a feed task for testing."""
    return Feed(
        name="Feed lions",
        description="Feed lions in lion enc",
        roles=["Zoo keeper"]
    )

@pytest.fixture()
def dummy_surgery_task():
    """Creating a surgery task for testing."""
    return Surgery(
        name="Surgery",
        description="Perform surgery on animal",
        roles=["Zoo keeper"]
    )

@pytest.fixture()
def dummy_health_check_task():
    """Creating a health_check task for testing."""
    return HealthCheck(
        name="Health check",
        description="Perform Health check on animal",
        roles=["Veterinarian"]
    )



def test_create_feed_task(dummy_feed_task):
    assert dummy_feed_task.name == "Feed lions"

def test_create_surgery_task(dummy_surgery_task):
    assert "Zoo keeper" in dummy_surgery_task.roles

def test_create_health_check_task(dummy_health_check_task):
    assert len(dummy_health_check_task.roles) == 1











