"""
Unit tests for the Attendance class.
"""

from unittest.mock import patch
from git_project.methods.attendance import Attendance

class TestAttendance:
    """
    Tests for managing attendance functionalities.
    """

    def test_check_attendance_for_all(self):
        """
        Tests checking attendance for all students.
        """
        attendance = Attendance()
        date = "2020-12-12"
        students = [
            {"Name": "Grzegorz", "Surname": "Boczek", "ID": "1"},
            {"Name": "Karol", "Surname": "Kredka", "ID": "2"},
        ]

        with patch("builtins.input", side_effect=["1", "0"]):
            attendance.check_attendance_for_all(date, students)

        assert attendance.presence[date]["Grzegorz Boczek"] is True
        assert attendance.presence[date]["Karol Kredka"] is False

    def test_download_attendance(self):
        """
        Tests downloading attendance for a specific date.
        """
        attendance = Attendance()
        date = "2020-12-12"
        attendance.presence = {date: {"Grzegorz Boczek": True, "Karol Kredka": False}}

        with patch("builtins.print") as mocked_print:
            attendance.download_attendance(date)

        mocked_print.assert_any_call(f"Attendance for {date}:")
        mocked_print.assert_any_call("Grzegorz Boczek: present")
        mocked_print.assert_any_call("Karol Kredka: absent")

    def test_modify_attendance(self):
        """
        Tests modifying attendance for a specific student on a specific date.
        """
        attendance = Attendance()
        date = "2020-12-12"
        student_name = "Grzegorz Boczek"
        attendance.presence = {date: {student_name: False, "Karol Kredka": False}}

        with patch("builtins.input", return_value="1"):
            with patch("builtins.print") as mocked_print:
                attendance.modify_attendance(date, student_name)

        assert attendance.presence[date][student_name] is True
        mocked_print.assert_any_call(
            f"Attendance for student {student_name} on {date} has been updated to present."
        )

    def test_clear_attendance(self):
        """
        Tests clearing attendance data for a specific date.
        """
        attendance = Attendance()
        date = "2020-12-12"
        attendance.presence = {date: {"Grzegorz Boczek": True, "Karol Kredka": False}}

        with patch("builtins.print") as mocked_print:
            attendance.clear_attendance(date)

        assert date not in attendance.presence
        mocked_print.assert_any_call(f"Attendance data for {date} has been removed.")
