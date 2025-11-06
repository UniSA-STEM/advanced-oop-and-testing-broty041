'''
File: test_zoo_operations.py
Description: Testing for zoo_operations.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from zoo_operations import Zoo
from animal import Lion
from enclosure import Enclosure
from staff import Staff
from health_record import HealthRecord
from task import Feed, Surgery

@pytest.fixture()
def dummy_zoo():
    """Create a dummy zoo for testing."""
    return Zoo(
            name="Zoop"
        )

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
def dummy_animal_lion2():
    """Create a dummy lion for testing."""
    return Lion(
        name="Larry",
        species="Lion",
        age=5,
        gender="Male",
        diet="Carnivore",
        animal_class="Mammal",
        environment="Savannah"
    )

@pytest.fixture()
def dummy_enclosure():
    """Create a dummy enclosure"""
    return Enclosure(
        name="Lion ENC",
        size=10,
        environment="Savannah",
        enclosure_class="Mammal",
        enclosure_status="Empty",
    )

@pytest.fixture()
def dummy_enclosure2():
    """Create a dummy enclosure"""
    return Enclosure(
        name="Lion ENC2",
        size=10,
        environment="Savannah",
        enclosure_class="Mammal",
        enclosure_status="Empty",
    )

@pytest.fixture
def dummy_zookeeper():
    """Create a dummy zookeeper for testing."""
    return Staff(
        name="Bob",
        role="Zoo keeper",
        specialty="Savannah"
    )

@pytest.fixture
def dummy_vet():
    """Create a dummy vet for testing."""
    return Staff(
        name="Brob",
        role="Veterinarian",
        specialty="Savannah"
    )

@pytest.fixture()
def dummy_feed_task(dummy_enclosure):
    """Create a dummy feed task for testing."""
    return Feed(
        name="Feed lions",
        description="Feed lions in lion enc",
        roles=["Zoo keeper"],
        assigned_enclosure=dummy_enclosure
    )

@pytest.fixture()
def dummy_surgery_task(dummy_animal_lion):
    """Create a dummy feed task for testing."""
    """Creating a feed task for testing."""
    return Surgery(
        name="Surgery",
        description="Surgery on lion",
        roles=["Veterinarian"],
        animal = dummy_animal_lion
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


def test_find_animal(dummy_zoo, dummy_animal_lion):
    """Test if animal is found with find method."""
    dummy_zoo.add_animal(dummy_animal_lion)
    found = dummy_zoo.find_animal(dummy_animal_lion)
    assert found == dummy_animal_lion

def test_list_animals(dummy_zoo, dummy_animal_lion):
    """Test listing animals method runs."""
    dummy_zoo.list_zoo_animals()

def test_add_animal(dummy_zoo, dummy_animal_lion):
    """Test adding animals to zoo."""
    assert dummy_zoo.add_animal(dummy_animal_lion) is True

def test_remove_animal(dummy_zoo, dummy_animal_lion, dummy_enclosure):
    """Test removing animals from zoo."""
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.assign_animal(dummy_animal_lion, dummy_enclosure)
    assert dummy_zoo.remove_animal(dummy_animal_lion, dummy_enclosure) is True

def test_check_routine_dependencies_animal(dummy_zoo, dummy_vet, dummy_animal_lion, dummy_enclosure, dummy_surgery_task):
    """Test animal cannot be removed if it has related daily routine."""
    dummy_zoo.add_staff(dummy_vet)
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_animal(dummy_animal_lion, dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_vet, dummy_enclosure)
    dummy_zoo.add_task(dummy_vet, dummy_surgery_task)
    dummy_zoo.add_to_routine(dummy_vet, dummy_surgery_task, "Monday")
    assert dummy_zoo.remove_animal(dummy_animal_lion, dummy_enclosure) is False

def test_check_animal_dependencies_staff(dummy_zoo, dummy_vet, dummy_animal_lion, dummy_enclosure, dummy_surgery_task):
    """Test animal cannot be removed if it has related staff task."""
    dummy_zoo.add_staff(dummy_vet)
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_vet, dummy_enclosure)
    dummy_zoo.add_task(dummy_vet, dummy_surgery_task)
    assert dummy_zoo.remove_animal(dummy_animal_lion, dummy_enclosure) is False

def test_assign_animal(dummy_zoo, dummy_animal_lion, dummy_enclosure):
    """Test assigning animals to enclosure."""
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    assert dummy_zoo.assign_animal(dummy_animal_lion, dummy_enclosure) is True

def test_unassign_animal(dummy_zoo, dummy_animal_lion, dummy_enclosure):
    """Test unassigning animals from enclosure runs."""
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_animal(dummy_animal_lion, dummy_enclosure)
    dummy_zoo.unassign_animal(dummy_animal_lion, dummy_enclosure)

def test_move_animal(dummy_zoo, dummy_animal_lion, dummy_enclosure, dummy_enclosure2):
    """Test moving animal between enclosure."""
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.add_enclosure(dummy_enclosure2)
    dummy_zoo.assign_animal(dummy_animal_lion, dummy_enclosure)
    assert dummy_zoo.move_animal(dummy_animal_lion, dummy_enclosure, dummy_enclosure2) is True

def test_add_enclosure(dummy_zoo, dummy_enclosure):
    """Test adding enclosures to zoo runs."""
    dummy_zoo.add_enclosure(dummy_enclosure)

def test_remove_enclosure(dummy_zoo, dummy_enclosure):
    """Test adding enclosures to zoo runs."""
    dummy_zoo.add_enclosure(dummy_enclosure)
    assert dummy_zoo.remove_enclosure(dummy_enclosure) is True

def test_check_enclosure_dependencies_staff(dummy_zoo, dummy_zookeeper, dummy_animal_lion, dummy_enclosure, dummy_feed_task):
    """Test enclosure cannot be removed if it has related daily routine."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_zookeeper, dummy_enclosure)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    assert dummy_zoo.remove_enclosure(dummy_enclosure) is False

def test_check_routine_dependencies_enclosure(dummy_zoo, dummy_zookeeper, dummy_animal_lion, dummy_enclosure, dummy_feed_task):
    """Test enclosure cannot be removed if it has related staff task."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_animal(dummy_animal_lion)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_zookeeper, dummy_enclosure)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    dummy_zoo.add_to_routine(dummy_zookeeper, dummy_feed_task, "Monday")
    assert dummy_zoo.remove_enclosure(dummy_enclosure) is False

def test_list_staff(dummy_zoo):
    """Test list staff runs."""
    dummy_zoo.list_staff()

def test_add_staff(dummy_zoo, dummy_zookeeper):
    """Test add staff method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)

def test_remove_staff(dummy_zoo, dummy_zookeeper):
    """Test remove staff method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.remove_staff(dummy_zookeeper)

def test_add_task(dummy_zoo, dummy_zookeeper, dummy_feed_task):
    """Test add task method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)

def test_remove_task(dummy_zoo, dummy_zookeeper, dummy_feed_task):
    """Test remove task method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    assert dummy_zoo.remove_task(dummy_zookeeper, dummy_feed_task) is False

def test_check_routine_dependencies_task(dummy_zoo, dummy_zookeeper, dummy_feed_task):
    """Test task cannot be removed if it is also in daily routine."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    dummy_zoo.add_to_routine(dummy_zookeeper, dummy_feed_task, "Monday")
    assert dummy_zoo.remove_task(dummy_zookeeper, dummy_feed_task) is False

def test_assign_staff_enclosure(dummy_zoo, dummy_zookeeper, dummy_enclosure):
    """Test assign staff enclosure method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_enclosure(dummy_enclosure)

def test_unassign_staff_enclosure(dummy_zoo, dummy_zookeeper, dummy_enclosure):
    """Test unassign staff enclosure method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_zookeeper, dummy_enclosure)
    dummy_zoo.unassign_staff_enclosure(dummy_zookeeper, dummy_enclosure)

def test_add_to_routine(dummy_zoo, dummy_zookeeper, dummy_feed_task, dummy_enclosure):
    """Test staff task can be added to daily routine."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_zookeeper, dummy_enclosure)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    assert dummy_zoo.add_to_routine(dummy_zookeeper, dummy_feed_task, "Monday") is True

def test_clear_routines(dummy_zoo, dummy_zookeeper, dummy_feed_task, dummy_enclosure):
    """Test clear routines method runs."""
    dummy_zoo.add_staff(dummy_zookeeper)
    dummy_zoo.add_enclosure(dummy_enclosure)
    dummy_zoo.assign_staff_enclosure(dummy_zookeeper, dummy_enclosure)
    dummy_zoo.add_task(dummy_zookeeper, dummy_feed_task)
    dummy_zoo.add_to_routine(dummy_zookeeper, dummy_feed_task, "Monday")
    dummy_zoo.clear_routines()

def test_generate_health_record(dummy_zoo, dummy_animal_lion):
    """Test that records are being generated and added to animal."""
    dummy_zoo.generate_health_record(
        dummy_animal_lion,
        description="Bump on head",
        record_type="Injury",
        date="12/12/12",
        status="Active",
        severity_level=3,
        treatment_plan="Rest",
        notes="Ran into fence."
    )
    dummy_zoo.generate_health_record(
        dummy_animal_lion,
        description="Hurt paw",
        record_type="Injury",
        date="12/12/12",
        status="Active",
        severity_level=3,
        treatment_plan="Rest",
        notes="Ran into fence."
    )
    assert len(dummy_animal_lion.record) == 2

def test_populate_reports(dummy_zoo):
    """Test populate_reports is being populated."""
    reports = dummy_zoo.populate_reports()
    assert len(reports.reports) == 3
    assert "Daily Routine Report" in (r.name for r in reports.reports)





