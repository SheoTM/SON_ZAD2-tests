"""
Unit tests for Import and Export functionalities.
"""

from unittest.mock import mock_open, patch
from git_project.methods.import_students import ImportStudents

class TestImportExport:
    """
    Tests for importing and exporting student data.
    """

    def test_import_students_csv(self):
        """
        Tests importing students from a CSV file.
        """
        mock_csv_data = "Name;Surname;ID\nGrzegorz;Boczek;1\nKarol;Kredka;2"
        with patch("builtins.open", mock_open(read_data=mock_csv_data)):
            result = ImportStudents.csv("mock_path.csv", ["Name", "Surname", "ID"])
            expected = [
                {"Name": "Grzegorz", "Surname": "Boczek", "ID": "1"},
                {"Name": "Karol", "Surname": "Kredka", "ID": "2"},
            ]
            assert result == expected

    def test_import_students_txt(self):
        """
        Tests importing students from a TXT file.
        """
        mock_txt_data = "Grzegorz Boczek - 1\nKarol Kredka - 2"
        with patch("builtins.open", mock_open(read_data=mock_txt_data)):
            result = ImportStudents.txt("mock_path.txt", ["Name", "Surname", "ID"])
            expected = [
                {"Name": "Grzegorz", "Surname": "Boczek", "ID": "1"},
                {"Name": "Karol", "Surname": "Kredka", "ID": "2"},
            ]
            assert result == expected
