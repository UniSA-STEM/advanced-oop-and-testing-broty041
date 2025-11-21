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


class TestTask:
    @pytest.fixture()
    def lion_feed_task(self):
        """Creating a feed task for testing."""
        return Feed(
            name="Feed lions",
            description="Feed lions in lion enc",
            roles=["Zoo keeper", "Veterinarian"]
        )

    @pytest.fixture()
    def vet_surgery_task(self):
        """Creating a surgery task for testing."""
        return Surgery(
            name="Surgery",
            description="Perform surgery on animal",
            roles=["Veterinarian"]
        )

    @pytest.fixture()
    def vet_health_check_task(self):
        """Creating a health_check task for testing."""
        return HealthCheck(
            name="Health check",
            description="Perform Health check on animal",
            roles=["Veterinarian"]
        )

    def test_create_feed_task(self, lion_feed_task):
        """Test Feed task initialises correctly."""
        assert lion_feed_task.name == "Feed lions"
        assert "Zoo keeper" in lion_feed_task.roles
        assert "Veterinarian" in lion_feed_task.roles

    def test_create_surgery_task(self, vet_surgery_task):
        """Test Surgery task initialises correctly."""
        assert "Veterinarian" in vet_surgery_task.roles

    def test_create_health_check_task(self, vet_health_check_task):
        """Test HealthCheck task initialises correctly."""
        assert len(vet_health_check_task.roles) == 1

    def test_get_task_name(self, lion_feed_task):
        """Test task name received."""
        assert lion_feed_task.name == "Feed lions"

    def test_get_roles(self, vet_surgery_task):
        """Test task roles received."""
        roles = vet_surgery_task.roles
        assert isinstance(roles, list)
        assert len(roles) == 1
