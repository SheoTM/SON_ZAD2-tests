"""
Module for importing student data from CSV and TXT files.
"""

class ImportStudents:
    """
    Handles importing student data from CSV and TXT files.
    """

    @staticmethod
    def csv(path, student_details_structure):
        """
        Imports student data from a CSV file.
        """
        students = []

        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines[1:]:  # Pomijamy pierwszą linię z nagłówkami
            line = line.rstrip()
            student_details = line.split(";")
            student_details_dict = dict(zip(student_details_structure, student_details))
            students.append(student_details_dict)

        return students

    @staticmethod
    def txt(path, student_details_structure):
        """
        Imports student data from a TXT file.

        Args:
            path (str): Path to the TXT file.
            student_details_structure (list): List defining the structure of student details.

        Returns:
            list: List of student dictionaries.
        """
        students = []

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                student_details = [
                    detail
                    for part in line.split(" - ")
                    for detail in part.split(" ")
                ]
                student_details_dict = dict(
                    zip(student_details_structure, student_details)
                )
                students.append(student_details_dict)

        return students
