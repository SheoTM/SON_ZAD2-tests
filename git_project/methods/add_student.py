"""
Module for modifying student records and exporting data to CSV and TXT files.
"""

import os
from git_project.methods.export_students import ExportStudents

class ModifyStudents:
    """
    Class for managing student data modifications and exporting.
    """

    @staticmethod
    def add_student_and_export(path, path2, students):
        """
        Adds a new student to the list and exports updated data to CSV and TXT files.

        Args:
            path (str): Path to the CSV file.
            path2 (str): Path to the TXT file.
            students (list): List of current students.
        """
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")

        # Validate inputs
        if not name or not surname or not student_id:
            raise KeyError("Missing required student data.")

        students.append({"Name": name, "Surname": surname, "ID": student_id})
        ExportStudents.csv(path, students)
        ExportStudents.txt(path2, students)

    @staticmethod
    def add_student_by_overwriting(path, path2):
        """
        Adds a new student directly to files, creating them if they do not exist.

        Args:
            path (str): Path to the CSV file.
            path2 (str): Path to the TXT file.
        """
        student = [
            input("Enter student's name: "),
            input("Enter student's surname: "),
            input("Enter student's ID: "),
        ]
        mode = "a" if os.path.exists(path) else "w"
        with open(path, mode, encoding="utf-8") as file:
            file.write("\n" + ";".join(student) if mode == "a" else ";".join(student))

        with open(path2, mode, encoding="utf-8") as file2:
            file2.write(
                "\n" + student[0] + " " + student[1] + " - " + student[2]
                if mode == "a"
                else student[0] + " " + student[1] + " - " + student[2]
            )

    @staticmethod
    def modify_student(path, path2, students):
        """
         Modifies a student's details in the list and exports updated data.

         Args:
             path (str): Path to the CSV file.
             path2 (str): Path to the TXT file.
             students (list): List of current students.
         """
        student_id = input("Enter student's ID to modify: ")
        for student in students:
            if student["ID"] == student_id:
                name = input("Enter new student's name: ")
                surname = input("Enter new student's surname: ")
                student["Name"] = name
                student["Surname"] = surname
                ExportStudents.csv(path, students)
                ExportStudents.txt(path2, students)
                return
        print("Student not found.")

    @staticmethod
    def delete_student(path, path2, students):
        """
        Deletes a student from the list and exports updated data.

        Args:
            path (str): Path to the CSV file.
            path2 (str): Path to the TXT file.
            students (list): List of current students.
        """
        student_id = input("Enter student's ID to delete: ")
        for i in range(len(students)):
            if students[i]["ID"] == student_id:
                del students[i]
                ExportStudents.csv(path, students)
                ExportStudents.txt(path2, students)
                return
        print("Student not found.")
