'''
File: test_animal.py
Description: Testing for animal.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from animal import Lion, Bird, Fish
from health_record import HealthRecord


class TestAnimal:
    @pytest.fixture()
    def animal_lion(self):
        """Create a lion for testing."""
        return Lion(
            name="Leo",
            species="Lion",
            age=5,
            gender="Male",
            diet="Carnivore",
            animal_class="Mammal",
            environment="Savannah"
        )

    @pytest.fixture()
    def animal_bird(self):
        """Create a bird for testing."""
        return Bird(
            name="Polly",
            species="Parrot",
            age=5,
            gender="Male",
            diet="Carnivore",
            animal_class="Bird",
            environment="Savannah",
            wing_span=10,
            can_fly=True
        )

    @pytest.fixture()
    def animal_fish(self):
        """Create a fish for testing."""
        return Fish(
            name="Old Ironjaw",
            species="Trout",
            age=5,
            gender="Male",
            diet="Omnivore",
            animal_class="Fish",
            environment="Tropical",
            scale_colours=["yellow", "blue"],
            swim_depth=200
        )

    @pytest.fixture()
    def injury_health_record(self, animal_lion):
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

    def test_update_movability(self, animal_lion, injury_health_record):
        """
        Test that adding a record that's active and severity > 2 changes
        movability to false.
        """
        animal_lion.movable = True
        animal_lion.update_movability()
        assert animal_lion.movable == True
        animal_lion.add_health_record("Leo1",
                                      injury_health_record)
        assert animal_lion.movable == False

    def test_add_health_record(self, animal_lion, injury_health_record):
        """Test method adds a health record."""
        animal_lion.add_health_record("Leo1",
                                      injury_health_record)
        assert len(animal_lion.record) == 1
        assert "Leo1" in animal_lion.record

    def test_adjust_status_after_surgery(self, animal_lion, injury_health_record):
        """
        Test if record is active and surgery that it changes status
        to closed.
        """
        r = injury_health_record
        r.plan = "Surgery"
        animal_lion.add_health_record("Leo1", r)
        assert animal_lion.adjust_status_after_surgery() is True
        assert r.status == "Closed"

    def test_check_health(self, injury_health_record, animal_lion):
        """Test that check health decreases severity."""
        animal_lion.add_health_record("Leo1",
                                      injury_health_record)
        animal_lion.check_health()
        assert injury_health_record.severity == 2

    def test_lion_behaviour(self, animal_lion):
        """Test lion behaviours."""
        animal_lion.cry()
        animal_lion.eat()
        animal_lion.sleep()

    def test_bird_behaviour(self, animal_bird):
        """Test bird behaviours."""
        animal_bird.cry()
        animal_bird.eat()
        animal_bird.sleep()

    def test_fish_behaviour(self, animal_fish):
        """Test fish behaviours."""
        animal_fish.cry()
        animal_fish.eat()
        animal_fish.sleep()
