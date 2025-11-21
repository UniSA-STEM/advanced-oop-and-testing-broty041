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


class TestStaff:
    @pytest.fixture
    def staff_zookeeper(self):
        """Create a zookeeper for testing."""
        return Staff(
            name="Bob",
            role="Zoo keeper",
            specialty="Savannah"
        )
    
    @pytest.fixture()
    def lion_enclosure(self):
        """Create a enclosure for testing."""
        return Enclosure(
            name="Lion ENC",
            size=10,
            environment="Savannah",
            enclosure_class="Mammal",
            enclosure_status="Empty",
        )
    
    @pytest.fixture()
    def lion_feed_task(self):
        """Create a feed task for testing."""
        return Feed(
            name="Feed lions",
            description="Feed lions in lion enc",
            roles=["Zoo keeper"]
        )
    
    def test_create_staff_zookeeper(self, staff_zookeeper):
        """Test creating a zoo keeper."""
        assert staff_zookeeper.name == "Bob"
        assert staff_zookeeper.role == "Zoo keeper"
    
    def test_assign_enclosure(self, staff_zookeeper, lion_enclosure):
        """Test assigning an enclosure too zoo keeper."""
        test_enc = staff_zookeeper.assign_enclosure(lion_enclosure)
        assert test_enc == True
    
    def test_add_task(self, staff_zookeeper, lion_enclosure, lion_feed_task):
        """Test adding task to zoo keeper."""
        staff_zookeeper.assign_enclosure(lion_enclosure)
        test_task = staff_zookeeper.add_task(lion_feed_task)
        assert test_task == True
        assert lion_feed_task in staff_zookeeper.tasks
    
    def test_remove_task(self, staff_zookeeper, lion_enclosure,
                         lion_feed_task):
        """Test removing task from zoo keeper."""
        staff_zookeeper.assign_enclosure(lion_enclosure)
        staff_zookeeper.add_task(lion_feed_task)
        test_task = staff_zookeeper.remove_task(lion_feed_task)
    
        assert test_task == True
        assert lion_feed_task not in staff_zookeeper.tasks
    
    def test_remove_no_task(self, staff_zookeeper, lion_feed_task):
        """Test removing when task not in zoo keepers task list"""
        test_task = staff_zookeeper.remove_task(lion_feed_task)
        assert test_task == False
    
    def test_perform_task(self, staff_zookeeper, lion_enclosure,
                          lion_feed_task):
        """Test zoo keeper performing feed task. If no crash then pass."""
        lion_feed_task.enclosure = lion_enclosure
        staff_zookeeper.assign_enclosure(lion_enclosure)
        staff_zookeeper.add_task(lion_feed_task)
        staff_zookeeper.perform_task(lion_feed_task)
    
    def test_list_tasks(self, staff_zookeeper):
        """Test list tasks runs."""
        staff_zookeeper.list_tasks()

