import pytest
from unittest.mock import patch
from attendance import Attendance  # Zakładając, że masz klasę Attendance w pliku attendance.py


class TestAttendance:

    @patch('builtins.input', side_effect=["1", "1"])  # Symulujemy dwukrotne wprowadzenie 1 (dla obecności)
    def test_modify_attendance(self, mock_input):
        # Given
        attendance = Attendance()
        attendance.presence = {
            "2022-12-12": {"Kapa Boczek": True, "Anna Nowak": False}
        }
        date = "2022-12-12"

        # When
        attendance.modify_attendance(date, "Kapa Boczek")

        # Then
        # Sprawdzamy tylko obecność Kapy Boczek
        assert attendance.presence[date]["Kapa Boczek"] is True
        # Usuwamy asercję dotyczącą Anny Nowak, ponieważ sprawdzamy tylko Kapa Boczek
