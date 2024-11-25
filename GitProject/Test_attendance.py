import pytest


class Attendance:
    def __init__(self):
        self.presence = {}

    def download_attendance(self, date):
        if date not in self.presence:
            return f"No attendance data for {date}."
        result = [f"Attendance for {date}:"]
        for student, present in self.presence[date].items():
            result.append(f"{student}: {'present' if present else 'absent'}")
        return "\n".join(result)

    def modify_attendance(self, date, student_name, present):
        if date not in self.presence:
            self.presence[date] = {}

        self.presence[date][student_name] = present
        return f"Attendance for {student_name} on {date} has been updated to {'present' if present else 'absent'}."


class TestAttendance:
    @staticmethod
    def test_download_attendance():
        # given
        attendance = Attendance()
        date = "2020-12-12"
        students = [
            {"Name": "Grzegorz", "Surname": "Boczek"},
            {"Name": "Karol", "Surname": "Kredka"}
        ]
        attendance.presence = {
            date: {
                "Grzegorz Boczek": True,
                "Karol Kredka": False
            }
        }

        # when
        result = attendance.download_attendance(date)

        # then
        expected_output = "Attendance for 2020-12-12:\nGrzegorz Boczek: present\nKarol Kredka: absent"
        assert result == expected_output

    @staticmethod
    def test_modify_attendance():
        # given
        attendance = Attendance()
        date = "2020-12-12"
        student_name = "Grzegorz Boczek"
        attendance.presence = {
            date: {
                "Grzegorz Boczek": False,
                "Karol Kredka": False
            }
        }

        # when
        result = attendance.modify_attendance(date, student_name, True)

        # then
        expected_output = "Attendance for Grzegorz Boczek on 2020-12-12 has been updated to present."
        assert result == expected_output
        assert attendance.presence[date][student_name] == True

        # when
        result = attendance.modify_attendance(date, student_name, False)

        # then
        expected_output = "Attendance for Grzegorz Boczek on 2020-12-12 has been updated to absent."
        assert result == expected_output
        assert attendance.presence[date][student_name] == False
