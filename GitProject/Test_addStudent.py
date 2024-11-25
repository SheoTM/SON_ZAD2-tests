import pytest

class MockAddStudent:
    @staticmethod
    def add_student(students, name, surname, student_id):
        new_student = {"Name": name, "Surname": surname, "ID": student_id}
        students.append(new_student)

    @staticmethod
    def update_student(students, student_id, new_name, new_surname):
        for student in students:
            if student["ID"] == student_id:
                student["Name"] = new_name
                student["Surname"] = new_surname
                return True
        return False


class TestaddStudent:
    @staticmethod
    def test_add_student():
        # Given
        students = []
        want = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        MockAddStudent.add_student(students, "Anna", "Nowak", "ABC45")

        # Then
        assert students == want

    @staticmethod
    def test_update_student():
        # Given
        students = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]
        want = [{"Name": "Grzegorz", "Surname": "Boczek", "ID": "ABC45"}]

        # When
        result = MockAddStudent.update_student(students, "ABC45", "Grzegorz", "Boczek")

        # Then
        assert result is True
        assert students == want
