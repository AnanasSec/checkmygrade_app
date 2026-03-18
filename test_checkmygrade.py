import unittest
from checkmygrade import CheckMyGradeApp


class TestCheckMyGradeApp(unittest.TestCase):

    def setUp(self):
        self.app = CheckMyGradeApp()

        self.app.students = []
        self.app.courses = []
        self.app.professors = []
        self.app.login_users = []

        self.app.add_new_course("DATA200", "Python Programming", 3)
        self.app.add_new_course("DATA201", "Databases", 4)

        self.app.add_new_professor("P101", "Minerva McGonagall", "mcgonagall@hogwarts.edu", "Senior Professor", "DATA200")
        self.app.add_new_professor("P102", "Severus Snape", "snape@hogwarts.edu", "Associate Professor", "DATA201")

    # Testing of student records addition/deletion and modification. 

    def test_add_student(self):
        result = self.app.add_new_student("S001", "Harry", "Potter", "harry@hogwarts.edu", "DATA200", "P101", 95)
        self.assertTrue(result)
        self.assertEqual(len(self.app.students), 1)
        student = self.app.students[0]
        self.assertEqual(student.first_name, "Harry")
        self.assertEqual(student.grade, "A")

    def test_delete_student(self):
        self.app.add_new_student("S001", "Harry", "Potter", "harry@hogwarts.edu", "DATA200", "P101", 95)
        result = self.app.delete_student("S001")
        self.assertTrue(result)
        self.assertEqual(len(self.app.students), 0)

    def test_update_student(self):

        self.app.add_new_student(
            "S001", "Harry", "Potter", "harry@hogwarts.edu", "DATA200", "P101", 95
        )
        self.app.update_student("S001", marks=82)
        student = next(s for s in self.app.students if s.student_id == "S001")
        self.assertEqual(student.marks, 82.0)
        self.assertEqual(student.grade, "B")

    # Testing to have the student files at least 1000 records.

    def test_student_records_with_1000_records(self):
        for i in range(1000):
            self.app.add_new_student(
                f"S{i:04d}",
                "Student",
                str(i),
                f"student{i}@hogwarts.edu",
                "DATA200",
                "P101",
                60 + (i % 41)
            )
        self.assertEqual(len(self.app.students), 1000)

    # Testing search and sorting functions with timing.

    def test_load_and_search_with_timing(self):
        for i in range(1000):
            self.app.add_new_student(
                f"S{i:04d}",
                "Student",
                str(i),
                f"student{i}@hogwarts.edu",
                "DATA200",
                "P101",
                70 + (i % 25)
            )

        new_app = CheckMyGradeApp()

        results, elapsed = new_app.search_student("student500@hogwarts.edu")
        print(f"Search time for loaded CSV data: {elapsed:.8f} seconds")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].student_id, "S0500")

    def test_sort_by_marks_timing(self):
        for i in range(1000):
            self.app.add_new_student(
                f"S{i:04d}",
                "Student",
                str(i),
                f"student{i}@hogwarts.edu",
                "DATA200",
                "P101",
                100 - (i % 100)
            )

        elapsed = self.app.sort_students_by_marks(descending=False)
        print(f"Sort by marks time: {elapsed:.8f} seconds")

        self.assertLessEqual(self.app.students[0].marks, self.app.students[-1].marks)

    def test_sort_by_email_timing(self):
        for i in range(1000):
            self.app.add_new_student(
                f"S{i:04d}",
                "Student",
                str(i),
                f"student{i}@hogwarts.edu",
                "DATA200",
                "P101",
                80
            )

        elapsed = self.app.sort_students_by_email(descending=False)
        print(f"Sort by email time: {elapsed:.8f} seconds")

        self.assertLessEqual(
            self.app.students[0].email_address.lower(),
            self.app.students[-1].email_address.lower()
        )

  
    # Course tests

    def test_add_course(self):
        self.app.courses = []
        result = self.app.add_new_course("DATA202", "Math", 3)
        self.assertTrue(result)
        self.assertEqual(len(self.app.courses), 1)

    def test_delete_course(self):
        result = self.app.delete_course("DATA201")
        self.assertTrue(result)
        self.assertEqual(len(self.app.courses), 1)
        remaining_course = self.app.courses[0]
        self.assertEqual(remaining_course.course_id, "DATA200")

    def test_modify_course(self):
        self.app.add_new_course("DATA202", "Math", 3)
        result = self.app.modify_course("DATA202", course_name="Math for Data", credits=5)
        self.assertTrue(result)
        course = next(c for c in self.app.courses if c.course_id == "DATA202")
        self.assertEqual(course.course_name, "Math for Data")
        self.assertEqual(course.credits, 5)


    # Professor tests

    def test_add_professor(self):
        self.app.professors = []
        result = self.app.add_new_professor(
            "P103", "Remus Lupin", "lupin@hogwarts.edu", "Professor", "DATA200"
        )
        self.assertTrue(result)
        self.assertEqual(len(self.app.professors), 1)

    def test_delete_professor(self):
        result = self.app.delete_professor("P102")
        self.assertTrue(result)
        self.assertEqual(len(self.app.professors), 1)
        remaining_prof = self.app.professors[0]
        self.assertEqual(remaining_prof.professor_id, "P101")

    def test_modify_professor(self):
        result = self.app.modify_professor_details("P101", rank="Head Professor", email_address="minerva@hogwarts.edu")
        self.assertTrue(result)
        prof = next(p for p in self.app.professors if p.professor_id == "P101")
        self.assertEqual(prof.rank, "Head Professor")
        self.assertEqual(prof.email_address, "minerva@hogwarts.edu")


if __name__ == "__main__":
    unittest.main()