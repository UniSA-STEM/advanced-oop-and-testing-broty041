'''
File: test_enclosure.py
Description: Testing for enclosure.py
Author: Thomas Brown
ID: 110454503
Username: broty041
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from animal import Lion
from enclosure import Enclosure

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
    """Create a dummy enclosure for testing."""
    return Enclosure(
        name="Lion ENC",
        size=10,
        environment="Savannah",
        enclosure_class="Mammal",
        enclosure_status="Empty",
    )

def test_can_accept_animal(dummy_enclosure, dummy_animal_lion):
    """Test if enclosure can accept an animal."""
    assert dummy_enclosure.can_accept_animal(dummy_animal_lion) == True

def test_can_accept_animal_dirty(dummy_enclosure, dummy_animal_lion):
    """Test if enclosure too dirty for another animal."""
    dummy_enclosure.clean = 4
    assert dummy_enclosure.can_accept_animal(dummy_animal_lion) == False

def test_feed_animals(dummy_enclosure):
    """Test if feeding runs."""
    assert dummy_enclosure.feed_animals() == True

def test_feed_animals_dirty(dummy_enclosure):
    """Test if enclosure too dirty for feeding."""
    dummy_enclosure.clean = 4
    assert dummy_enclosure.feed_animals() == False

def test_find_animal(dummy_enclosure, dummy_animal_lion):
    """Test if animal is found with find method."""
    dummy_enclosure.add_occupant(dummy_animal_lion)
    found = dummy_enclosure.find_animal(dummy_animal_lion)
    assert found == dummy_animal_lion

def test_add_occupant(dummy_enclosure, dummy_animal_lion):
    """Test if occupant is added to enclosure"""
    result = dummy_enclosure.add_occupant(dummy_animal_lion)
    assert result == True
    assert dummy_enclosure.status == "Occupied"

def test_remove_occupant(dummy_enclosure, dummy_animal_lion):
    """Test removing occupants from enclosure."""
    dummy_enclosure.add_occupant(dummy_animal_lion)
    result = dummy_enclosure.remove_occupant(dummy_animal_lion)
    assert result == True
    assert dummy_enclosure.status == "Empty"

def test_unassign_all_animals(dummy_enclosure, dummy_animal_lion, dummy_animal_lion2):
    """Test removing all occupants from enclosure."""
    dummy_enclosure.add_occupant(dummy_animal_lion)
    dummy_enclosure.add_occupant(dummy_animal_lion2)
    dummy_enclosure.unassign_all_animals()
    assert dummy_enclosure.occupants == []
