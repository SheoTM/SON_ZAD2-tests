import pytest
from unittest.mock import patch
from GitProject.methods.attendance import Attendance

class TestAttendance:

    def test_check_attendance_for_all(self):
        # Given
        attendance = Attendance()
        date = "2020-12-12"
        students = [
            {"Name": "Grzegorz", "Surname": "Boczek", "ID": "1"},
            {"Name": "Karol", "Surname": "Kredka", "ID": "2"},
        ]

        # Mocking input to simulate "1" for Grzegorz and "0" for Karol
        with patch("builtins.input", side_effect=["1", "0"]):
            attendance.check_attendance_for_all(date, students)

        # Then
        assert attendance.presence[date]["Grzegorz Boczek"] == True
        assert attendance.presence[date]["Karol Kredka"] == False

    def test_download_attendance(self):
        # Given
        attendance = Attendance()
        date = "2020-12-12"
        attendance.presence = {
            date: {
                "Grzegorz Boczek": True,
                "Karol Kredka": False
            }
        }

        # When
        with patch("builtins.print") as mocked_print:
            attendance.download_attendance(date)

        # Then
        mocked_print.expected_output(f"Attendance for {date}:")
        mocked_print.expected_output("Grzegorz Boczek: present")
        mocked_print.expected_output("Karol Kredka: absent")

    def test_modify_attendance(self):
        # Given
        attendance = Attendance()
        date = "2020-12-12"
        student_name = "Grzegorz Boczek"
        attendance.presence = {
            date: {
                student_name: False,
                "Karol Kredka": False
            }
        }

        # Mocking input to simulate "1" for Grzegorz
        with patch("builtins.input", return_value="1"):
            with patch("builtins.print") as mocked_print:
                attendance.modify_attendance(date, student_name)

        # Then
        assert attendance.presence[date][student_name] == True
        mocked_print.expected_output(f"Attendance for student {student_name} on {date} has been updated to present.")

    def test_clear_attendance(self):
        # Given
        attendance = Attendance()
        date = "2020-12-12"
        attendance.presence = {
            date: {
                "Grzegorz Boczek": True,
                "Karol Kredka": False
            }
        }

        # When
        with patch("builtins.print") as mocked_print:
            attendance.clear_attendance(date)

        # Then
        assert date not in attendance.presence
        mocked_print.assert_any_call(f"Attendance data for {date} has been removed.")
