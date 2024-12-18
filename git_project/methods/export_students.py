"""
Module for exporting student data to CSV and TXT files.
"""

class ExportStudents:
    """
    Handles exporting student data.
    """

    @staticmethod
    def csv(path, students):
        """
        Exports student data to a CSV file.

        Args:
            path (str): Path to the CSV file.
            students (list): List of student dictionaries.
        """
        with open(path, "w", encoding="utf-8") as file:  # Użycie `with` i dodanie kodowania
            lines = []
            for i in range(len(students)):
                student_details = students[i]
                line = []
                for student_detail_key in student_details:
                    line.append(student_details[student_detail_key])
                line = ";".join(line)
                if i < len(students) - 1:
                    line += "\n"
                lines.append(line)
            file.writelines(lines)

    @staticmethod
    def txt(path, students):
        """
        Exports student data to a TXT file.

        Args:
            path (str): Path to the TXT file.
            students (list): List of student dictionaries.
        """
        with open(path, "w", encoding="utf-8") as file:  # Użycie `with` i dodanie kodowania
            lines = []
            for i in range(len(students)):
                student_details = students[i]
                line = []
                for student_detail_key in student_details:
                    line.append(student_details[student_detail_key])
                    if student_detail_key == "Surname":
                        line.append(" - ")
                    else:
                        line.append(" ")
                line.pop()  # Usunięcie ostatniego niepotrzebnego separatora
                line = "".join(line)
                if i < len(students) - 1:
                    line += "\n"
                lines.append(line)
            file.writelines(lines)
