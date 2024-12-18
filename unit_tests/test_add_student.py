from git_project.methods.export_students import ExportStudents
import unittest
from unittest.mock import mock_open, patch


class TestExportStudents(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_csv_export(self, mock_file):
        # Given
        path = "students.csv"
        students = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        ExportStudents.csv(path, students)

        # Then
        mock_file.assert_called_once_with(path, "w")
        mock_file().writelines.assert_called_once_with(["Anna;Nowak;ABC45"])

    @patch("builtins.open", new_callable=mock_open)
    def test_txt_export(self, mock_file):
        # Given
        path = "students.txt"
        students = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        ExportStudents.txt(path, students)

        # Then
        mock_file.assert_called_once_with(path, "w")
        mock_file().writelines.assert_called_once_with(["Anna Nowak - ABC45"])


class TestAddStudent(unittest.TestCase):
    def test_add_student(self):
        # Given
        students = []
        want = [{"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}]

        # When
        new_student = {"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}
        students.append(new_student)

        # Then
        self.assertEqual(students, want)

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
        self.assertEqual(students, want)


if __name__ == "__main__":
    unittest.main()
