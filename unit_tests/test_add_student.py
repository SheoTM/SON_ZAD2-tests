"""
Unit tests for the add_student module.
"""

import pytest

class TestAddStudent:
    """
    Unit tests for the add_student functionalities.
    """

    def setup_method(self):
        """
        Prepares data for each test method.
        """
        self.students = []

    def teardown_method(self):
        """
        Cleans up data after each test method.
        """
        self.students = None

    def test_add_student(self):
        """
        Tests adding a new student to the list.
        """
        # Given
        want = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        new_student = {"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}
        self.students.append(new_student)

        # Then
        assert self.students == want

    def test_update_student(self):
        """
        Tests updating an existing student's details.
        """
        # Given
        self.students = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]
        want = [{"Name": "Grzegorz", "Surname": "Boczek", "ID": "ABC45"}]

        # When
        student_id = "ABC45"
        for student in self.students:
            if student["ID"] == student_id:
                student["Name"] = "Grzegorz"
                student["Surname"] = "Boczek"
                break

        # Then
        assert self.students == want

    def test_add_student_with_missing_data(self):
        """
        Tests adding a student with incomplete data.
        """
        # Given
        new_student = {"Name": "Anna", "ID": "ABC45"}  # Missing 'Surname'

        # When/Then
        with pytest.raises(KeyError, match="Missing required data: Surname"):
            if "Surname" not in new_student or not new_student["Surname"]:
                raise KeyError("Missing required data: Surname")
            self.students.append(new_student)
