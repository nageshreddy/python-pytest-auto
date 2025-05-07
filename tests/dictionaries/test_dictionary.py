import pytest

class TestStudentGrades:
    def setup_method(self):
        self.student = {
            "name": "Bob",
            "grades": {
                "math": 90,
                "science": 85
            }
        }

    def test_math_grade(self):
        # Assert the math grade is 90
        assert self.student["grades"]["math"] == 90

    def test_science_grade(self):
        # Assert the science grade is 85
        assert self.student["grades"]["science"] == 85

    def test_grades_key_exists(self):
        # Check that "grades" key exists
        assert "grades" in self.student

    def test_student_name(self):
        # Check that the student has a name
        assert self.student["name"] == "Bob"