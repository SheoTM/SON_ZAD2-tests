"""
Unit tests for the add_student module.
"""



class TestaddStudent:
    def test_add_student(self):
        # Given
        students = []
        want = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        new_student = {"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}
        students.append(new_student)

        # Then
        assert students == want

    def test_update_student(self):
        # Given
        students = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]
        want = [{"Name": "Grzegorz", "Surname": "Boczek", "ID": "ABC45"}]

        # When
        student_id = "ABC45"
        for student in students:
            if student["ID"] == student_id:
                student["Name"] = "Grzegorz"
                student["Surname"] = "Boczek"
                break

        # Then
        assert students == want
