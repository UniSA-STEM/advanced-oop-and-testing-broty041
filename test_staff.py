'''
File: test_staff.py
Description: Testing for staff.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from staff import Staff
from enclosure import Enclosure
from task import Feed



@pytest.fixture
def dummy_zookeeper():
    """Create a dummy zookeeper for testing."""
    return Staff(
        name="Bob",
        role="Zoo keeper",
        specialty="Savannah"
    )

@pytest.fixture()
def dummy_enclosure():
    """Create a dummy enclosure for testing."""
    return Enclosure(
        name="Lion ENC",
        size=10,
        environment="Savannah",
        enclosure_class="Mammal",
        enclosure_status="Empty",
    )

@pytest.fixture()
def dummy_feed_task():
    """Create a dummy feed task for testing."""
    return Feed(
        name="Feed lions",
        description="Feed lions in lion enc",
        roles=["Zoo keeper"]
    )

def test_create_dummy_zookeeper(dummy_zookeeper):
    """Test creating a zoo keeper."""
    assert dummy_zookeeper.name == "Bob"
    assert dummy_zookeeper.role == "Zoo keeper"

def test_assign_enclosure(dummy_zookeeper, dummy_enclosure):
    """Test assigning an enclosure too zoo keeper."""
    test_enc = dummy_zookeeper.assign_enclosure(dummy_enclosure)
    assert test_enc == True

def test_add_task(dummy_zookeeper, dummy_enclosure, dummy_feed_task):
    """Test adding task to zoo keeper."""
    dummy_zookeeper.assign_enclosure(dummy_enclosure)
    test_task = dummy_zookeeper.add_task(dummy_feed_task)
    assert test_task == True
    assert dummy_feed_task in dummy_zookeeper.tasks

def test_remove_task(dummy_zookeeper, dummy_enclosure, dummy_feed_task):
    """Test removing task from zoo keeper."""
    dummy_zookeeper.assign_enclosure(dummy_enclosure)
    dummy_zookeeper.add_task(dummy_feed_task)
    test_task = dummy_zookeeper.remove_task(dummy_feed_task)

    assert test_task == True
    assert dummy_feed_task not in dummy_zookeeper.tasks

def test_remove_no_task(dummy_zookeeper, dummy_feed_task):
    """Test removing when task not in zoo keepers task list"""
    test_task = dummy_zookeeper.remove_task(dummy_feed_task)
    assert test_task == False

def test_perform_task(dummy_zookeeper, dummy_enclosure, dummy_feed_task):
    """Test zoo keeper performing feed task. If no crash then pass."""
    dummy_feed_task.enclosure = dummy_enclosure
    dummy_zookeeper.assign_enclosure(dummy_enclosure)
    dummy_zookeeper.add_task(dummy_feed_task)
    dummy_zookeeper.perform_task(dummy_feed_task)

def test_list_tasks(dummy_zookeeper):
    """Test list tasks runs."""
    dummy_zookeeper.list_tasks()

