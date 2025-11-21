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


@pytest.fixture()
def dummy_animal_lion():
    """Create a dummy lion for testing."""
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
def dummy_animal_bird():
    """Create a dummy bird for testing."""
    return Bird(
        name="Polly",
        species="Parrot",
        age=5,
        gender="Male",
        diet="Carnivore",
        animal_class="Bird",
        environment="Savannah",
        wing_span=10
    )

@pytest.fixture()
def dummy_animal_fish():
    """Create a dummy fish for testing."""
    return Fish(
        name="Old Ironjaw",
        species="Trout",
        age=5,
        gender="Male",
        diet="Omnivore",
        animal_class="Fish",
        environment="Tropical",
        scale_colours=["yellow", "blue"]
    )

@pytest.fixture()
def dummy_health_record(dummy_animal_lion):
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


def test_update_movability(dummy_animal_lion, dummy_health_record):
    """
    Test that adding a record that's active and severity > 2 changes
    movability to false.
    """
    dummy_animal_lion.movable = True
    dummy_animal_lion.update_movability()
    assert dummy_animal_lion.movable == True
    dummy_animal_lion.add_health_record("Leo1",
                                        dummy_health_record)
    assert dummy_animal_lion.movable == False

def test_add_health_record(dummy_animal_lion, dummy_health_record):
    """Test method adds a health record."""
    dummy_animal_lion.add_health_record("Leo1",
                                        dummy_health_record)
    assert len(dummy_animal_lion.record) == 1
    assert "Leo1" in dummy_animal_lion.record

def test_adjust_status_after_surgery(dummy_animal_lion, dummy_health_record):
    """
    Test if record is active and surgery that it changes status
    to closed.
    """
    r = dummy_health_record
    r.plan = "Surgery"
    dummy_animal_lion.add_health_record("Leo1", r)
    assert dummy_animal_lion.adjust_status_after_surgery() is True
    assert r.status == "Closed"

def test_check_health(dummy_health_record, dummy_animal_lion):
    """Test that check health decreases severity."""
    dummy_animal_lion.add_health_record("Leo1",
                                        dummy_health_record)
    dummy_animal_lion.check_health()
    assert dummy_health_record.severity == 2

def test_lion_behaviour(dummy_animal_lion):
    """Test lion behaviours."""
    dummy_animal_lion.cry()
    dummy_animal_lion.eat()
    dummy_animal_lion.sleep()

def test_bird_behaviour(dummy_animal_bird):
    """Test bird behaviours."""
    dummy_animal_bird.cry()
    dummy_animal_bird.eat()
    dummy_animal_bird.sleep()

def test_fish_behaviour(dummy_animal_fish):
    """Test fish behaviours."""
    dummy_animal_fish.cry()
    dummy_animal_fish.eat()
    dummy_animal_fish.sleep()



