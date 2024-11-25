import pytest
import os

class ImportStudents:
    @staticmethod
    def csv(path, student_details_structure):
        students = []

        with open(path, "r") as file:
            for line in file:
                line = line.rstrip()
                student_details_dict = {}
                student_details = line.split(";")

                for i in range(len(student_details_structure)):
                    student_details_dict[student_details_structure[i]] = student_details[i]

                students.append(student_details_dict)

        return students

class ExportStudents:
    @staticmethod
    def csv(path, list):
        lines = []

        for student_details in list:
            line = ";".join(student_details.values())
            lines.append(line)

        with open(path, "w") as file:
            file.writelines("\n".join(lines))

class Testing:
    @staticmethod
    def test_import():
        # given
        path = "test_students_import.csv"
        student_details_structure = ["Name", "Surname", "ID"]
        file_content = """Anna;Nowak;ABC45"""
        with open(path, "w") as file:
            file.write(file_content)
        want = [
            {"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}
        ]

        # when
        got = ImportStudents.csv(path, student_details_structure)

        # then
        assert want == got
        os.remove(path)

    @staticmethod
    def test_export():
        # given
        path = "test_students_export.csv"
        students = [
            {"Name": "Anna", "Surname": "Nowak", "ID": "ABC45"}
        ]
        want = "Anna;Nowak;ABC45"

        # when
        ExportStudents.csv(path, students)
        with open(path, "r") as file:
            got = file.read().strip()

        # then
        assert got == want
        os.remove(path)
