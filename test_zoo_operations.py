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


class TestZoo:
    @pytest.fixture()
    def zoo_operations(self):
        """Create a zoo for testing."""
        return Zoo(
            name="Zoop"
        )

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
        """Create a enclosure"""
        return Enclosure(
            name="Lion ENC",
            size=10,
            environment="Savannah",
            enclosure_class="Mammal",
            enclosure_status="Empty",
        )

    @pytest.fixture()
    def lion_enclosure2(self):
        """Create a enclosure"""
        return Enclosure(
            name="Lion ENC2",
            size=10,
            environment="Savannah",
            enclosure_class="Mammal",
            enclosure_status="Empty",
        )

    @pytest.fixture
    def staff_zookeeper(self):
        """Create a zookeeper for testing."""
        return Staff(
            name="Bob",
            role="Zoo keeper",
            specialty="Savannah"
        )

    @pytest.fixture
    def staff_vet(self):
        """Create a vet for testing."""
        return Staff(
            name="Brob",
            role="Veterinarian",
            specialty="Savannah"
        )

    @pytest.fixture()
    def lion_feed_task(self, lion_enclosure):
        """Create a feed task for testing."""
        return Feed(
            name="Feed lions",
            description="Feed lions in lion enc",
            roles=["Zoo keeper"],
            assigned_enclosure=lion_enclosure
        )

    @pytest.fixture()
    def lion_surgery_task(self, animal_lion):
        """Create a feed task for testing."""
        """Creating a feed task for testing."""
        return Surgery(
            name="Surgery",
            description="Surgery on lion",
            roles=["Veterinarian"],
            animal=animal_lion
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

    def test_find_animal(self, zoo_operations, animal_lion):
        """
        Test if animal is found with find method and that invalid
        entry returns a type error.
        """
        zoo_operations.add_animal(animal_lion)
        found = zoo_operations.find_animal(animal_lion)
        assert found == animal_lion
        with pytest.raises(TypeError):
            zoo_operations.find_animal(123)

    def test_list_animals(self, zoo_operations, animal_lion):
        """Test listing animals method runs."""
        zoo_operations.list_zoo_animals()

    def test_add_animal(self, zoo_operations, animal_lion):
        """Test adding animals to zoo."""
        assert zoo_operations.add_animal(animal_lion) is True

    def test_remove_animal(self, zoo_operations, animal_lion, lion_enclosure):
        """Test removing animals from zoo."""
        zoo_operations.add_animal(animal_lion)
        zoo_operations.assign_animal(animal_lion, lion_enclosure)
        assert zoo_operations.remove_animal(animal_lion,
                                            lion_enclosure) is True

    def test_check_routine_dependencies_animal(self, zoo_operations,
                                               staff_vet,
                                               animal_lion,
                                               lion_enclosure,
                                               lion_surgery_task):
        """Test animal cannot be removed if it has related daily routine."""
        zoo_operations.add_staff(staff_vet)
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_animal(animal_lion, lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_vet, lion_enclosure)
        zoo_operations.add_task(staff_vet, lion_surgery_task)
        zoo_operations.add_to_routine(staff_vet, lion_surgery_task,
                                      "Monday")
        assert zoo_operations.remove_animal(animal_lion,
                                            lion_enclosure) is False

    def test_check_animal_dependencies_staff(self, zoo_operations,
                                             staff_vet, animal_lion,
                                             lion_enclosure,
                                             lion_surgery_task):
        """Test animal cannot be removed if it has related staff task."""
        zoo_operations.add_staff(staff_vet)
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_vet, lion_enclosure)
        zoo_operations.add_task(staff_vet, lion_surgery_task)
        assert zoo_operations.remove_animal(animal_lion,
                                            lion_enclosure) is False

    def test_assign_animal(self, zoo_operations, animal_lion, lion_enclosure):
        """Test assigning animals to enclosure."""
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        assert zoo_operations.assign_animal(animal_lion,
                                            lion_enclosure) is True

    def test_unassign_animal(self, zoo_operations, animal_lion,
                             lion_enclosure):
        """Test unassigning animals from enclosure runs."""
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_animal(animal_lion, lion_enclosure)
        zoo_operations.unassign_animal(animal_lion, lion_enclosure)

    def test_move_animal(self, zoo_operations, animal_lion, lion_enclosure,
                         lion_enclosure2):
        """Test moving animal between enclosure."""
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.add_enclosure(lion_enclosure2)
        zoo_operations.assign_animal(animal_lion, lion_enclosure)
        assert zoo_operations.move_animal(animal_lion, lion_enclosure,
                                          lion_enclosure2) is True

    def test_add_enclosure(self, zoo_operations, lion_enclosure):
        """Test adding enclosures to zoo runs."""
        zoo_operations.add_enclosure(lion_enclosure)

    def test_remove_enclosure(self, zoo_operations, lion_enclosure):
        """Test adding enclosures to zoo runs."""
        zoo_operations.add_enclosure(lion_enclosure)
        assert zoo_operations.remove_enclosure(lion_enclosure) is True

    def test_check_enclosure_dependencies_staff(self, zoo_operations,
                                                staff_zookeeper,
                                                animal_lion,
                                                lion_enclosure,
                                                lion_feed_task):
        """
        Test enclosure cannot be removed if it has related daily routine.
        """
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_zookeeper, lion_enclosure)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        assert zoo_operations.remove_enclosure(lion_enclosure) is False

    def test_check_routine_dependencies_enclosure(self, zoo_operations,
                                                  staff_zookeeper,
                                                  animal_lion,
                                                  lion_enclosure,
                                                  lion_feed_task):
        """Test enclosure cannot be removed if it has related staff task."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_animal(animal_lion)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_zookeeper, lion_enclosure)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        zoo_operations.add_to_routine(staff_zookeeper, lion_feed_task,
                                      "Monday")
        assert zoo_operations.remove_enclosure(lion_enclosure) is False

    def test_list_staff(self, zoo_operations):
        """Test list staff runs."""
        zoo_operations.list_staff()

    def test_add_staff(self, zoo_operations, staff_zookeeper):
        """Test add staff method runs."""
        zoo_operations.add_staff(staff_zookeeper)

    def test_remove_staff(self, zoo_operations, staff_zookeeper):
        """Test remove staff method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.remove_staff(staff_zookeeper)

    def test_add_task(self, zoo_operations, staff_zookeeper, lion_feed_task):
        """Test add task method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)

    def test_remove_task(self, zoo_operations, staff_zookeeper,
                         lion_feed_task):
        """Test remove task method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        assert zoo_operations.remove_task(staff_zookeeper,
                                          lion_feed_task) is False

    def test_check_routine_dependencies_task(self, zoo_operations,
                                             staff_zookeeper,
                                             lion_feed_task):
        """Test task cannot be removed if it is also in daily routine."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        zoo_operations.add_to_routine(staff_zookeeper, lion_feed_task,
                                      "Monday")
        assert zoo_operations.remove_task(staff_zookeeper,
                                          lion_feed_task) is False

    def test_assign_staff_enclosure(self, zoo_operations, staff_zookeeper,
                                    lion_enclosure):
        """Test assign staff enclosure method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_enclosure(lion_enclosure)

    def test_unassign_staff_enclosure(self, zoo_operations, staff_zookeeper,
                                      lion_enclosure):
        """Test unassign staff enclosure method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_zookeeper, lion_enclosure)
        zoo_operations.unassign_staff_enclosure(staff_zookeeper,
                                                lion_enclosure)

    def test_add_to_routine(self, zoo_operations, staff_zookeeper,
                            lion_feed_task,
                            lion_enclosure):
        """Test staff task can be added to daily routine."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_zookeeper, lion_enclosure)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        assert zoo_operations.add_to_routine(staff_zookeeper, lion_feed_task,
                                             "Monday") is True

    def test_clear_routines(self, zoo_operations,
                            staff_zookeeper,
                            lion_feed_task,
                            lion_enclosure):
        """Test clear routines method runs."""
        zoo_operations.add_staff(staff_zookeeper)
        zoo_operations.add_enclosure(lion_enclosure)
        zoo_operations.assign_staff_enclosure(staff_zookeeper, lion_enclosure)
        zoo_operations.add_task(staff_zookeeper, lion_feed_task)
        zoo_operations.add_to_routine(staff_zookeeper, lion_feed_task,
                                      "Monday")
        zoo_operations.clear_routines()

    def test_generate_health_record(self, zoo_operations, animal_lion):
        """Test that records are being generated and added to animal."""
        zoo_operations.generate_health_record(
            animal_lion,
            description="Bump on head",
            record_type="Injury",
            date="12/12/12",
            status="Active",
            severity_level=3,
            treatment_plan="Rest",
            notes="Ran into fence."
        )
        zoo_operations.generate_health_record(
            animal_lion,
            description="Hurt paw",
            record_type="Injury",
            date="12/12/12",
            status="Active",
            severity_level=3,
            treatment_plan="Rest",
            notes="Ran into fence."
        )
        assert len(animal_lion.record) == 2

    def test_populate_reports(self, zoo_operations):
        """Test populate_reports is being populated."""
        reports = zoo_operations.populate_reports()
        assert len(reports.reports) == 3
        assert "Daily Routine Report" in (r.name for r in reports.reports)
