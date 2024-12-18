"""
Module for managing student attendance.
"""

import os
from git_project.methods.import_students import ImportStudents

class Attendance:
    """
    Class to manage student attendance.
    """
    def __init__(self):
        """
        Initializes the Attendance class.
        """
        self.presence = {}

    def check_attendance_for_all(self, date, students):
        """
        Checks attendance for all students.

        Args:
            date (str): Date for attendance.
            students (list): List of students.
        """
        if date not in self.presence:
            self.presence[date] = {}

        for student in students:
            student_name = f"{student['Name']} {student['Surname']}"
            present = input(f"Is {student_name} present? (1/0): ") == "1"
            self.presence[date][student_name] = present
            status = "present" if present else "absent"
            print(
                f"Attendance for student {student_name} on {date} "
                f"has been updated to {status}.\n"
            )

    def download_attendance(self, date):
        """
        Downloads attendance data for a specific date.

        Args:
            date (str): Date for attendance.
        """
        if date not in self.presence:
            print(f"No attendance data for {date}.")
            return
        print(f"Attendance for {date}:")
        for student, present in self.presence[date].items():
            status = "present" if present else "absent"
            print(f"{student}: {status}")

    def clear_attendance(self, date):
        """
        Clears attendance data for a specific date.

        Args:
            date (str): Date for attendance to be cleared.
        """
        if date in self.presence:
            del self.presence[date]
            print(f"Attendance data for {date} has been removed.")
        else:
            print(f"No attendance data for {date}.")

    def modify_attendance(self, date, student_name):
        """
        Modifies attendance for a specific student on a specific date.

        Args:
            date (str): Date for attendance.
            student_name (str): Name of the student.
        """
        if date not in self.presence or student_name not in self.presence[date]:
            print(f"No attendance data found for {student_name} on {date}.")
            return
        present = input(f"Is {student_name} present? (1/0): ") == "1"
        self.presence[date][student_name] = present
        status = "present" if present else "absent"
        print(
            f"Attendance for student {student_name} on {date} "
            f"has been updated to {status}."
        )

def main():
    """
    Short description of the function.
    """
    attendance = Attendance()
    students = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path_csv = os.path.join(base_dir, "lists", "student_list.csv")
    file_path_txt = os.path.join(base_dir, "lists", "student_list.txt")

    # Load student list from CSV or TXT
    if os.path.exists(file_path_csv):
        try:
            students = ImportStudents.csv(file_path_csv, ["Name", "Surname", "ID"])
        except Exception as e:
            print(f"Error reading CSV file: {e}")
    elif os.path.exists(file_path_txt):
        try:
            students = ImportStudents.txt(file_path_txt, ["Name", "Surname", "ID"])
        except Exception as e:
            print(f"Error reading TXT file: {e}")
    else:
        print("No file with the student list found.")

    while True:
        print(
            "\n1. Check Attendance for All\n"
            "2. Download Attendance\n"
            "3. Modify Attendance\n"
            "4. Clear Attendance\n"
            "5. Exit"
        )
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): \n")
            attendance.check_attendance_for_all(date, students)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): \n")
            attendance.download_attendance(date)
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): \n")
            student_name = input("Student's full name (Name Surname): ")
            attendance.modify_attendance(date, student_name)
        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD) to clear attendance: \n")
            attendance.clear_attendance(date)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
