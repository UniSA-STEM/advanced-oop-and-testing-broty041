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


class TestEnclosure:
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
    def animal_lion2(self):
        """Create a lion for testing."""
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
    def lion_enclosure(self):
        """Create a enclosure for testing."""
        return Enclosure(
            name="Lion ENC",
            size=10,
            environment="Savannah",
            enclosure_class="Mammal",
            enclosure_status="Empty",
        )

    def test_can_accept_animal(self, lion_enclosure, animal_lion):
        """Test if enclosure can accept an animal."""
        assert lion_enclosure.can_accept_animal(animal_lion) == True

    def test_can_accept_animal_dirty(self, lion_enclosure, animal_lion):
        """Test if enclosure too dirty for another animal."""
        lion_enclosure.clean = 4
        assert lion_enclosure.can_accept_animal(animal_lion) == False

    def test_feed_animals(self, lion_enclosure):
        """Test if feeding runs."""
        assert lion_enclosure.feed_animals() == True

    def test_feed_animals_dirty(self, lion_enclosure):
        """Test if enclosure too dirty for feeding."""
        lion_enclosure.clean = 4
        assert lion_enclosure.feed_animals() == False

    def test_find_animal(self, lion_enclosure, animal_lion):
        """Test if animal is found with find method."""
        lion_enclosure.add_occupant(animal_lion)
        found = lion_enclosure.find_animal(animal_lion)
        assert found == animal_lion

    def test_add_occupant(self, lion_enclosure, animal_lion):
        """Test if occupant is added to enclosure"""
        result = lion_enclosure.add_occupant(animal_lion)
        assert result == True
        assert lion_enclosure.status == "Occupied"

    def test_remove_occupant(self, lion_enclosure, animal_lion):
        """Test removing occupants from enclosure."""
        lion_enclosure.add_occupant(animal_lion)
        result = lion_enclosure.remove_occupant(animal_lion)
        assert result == True
        assert lion_enclosure.status == "Empty"

    def test_unassign_all_animals(self, lion_enclosure, animal_lion,
                                  animal_lion2):
        """Test removing all occupants from enclosure."""
        lion_enclosure.add_occupant(animal_lion)
        lion_enclosure.add_occupant(animal_lion2)
        lion_enclosure.unassign_all_animals()
        assert lion_enclosure.occupants == []

    def test_clean_enclosure(self, lion_enclosure):
        """Test cleaning enclosure."""
        lion_enclosure.clean = 7
        assert lion_enclosure.clean == 7
        lion_enclosure.clean_enclosure()
        assert lion_enclosure.clean == 10
