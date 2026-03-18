#Anastasiia Gogoleva
#Lab1


import csv
import os
import statistics
import time


class TextSecurity:
    """This class with encrypt the test using Caesar cipher"""
    def __init__(self, shift):
        """COnstructor."""
        self.shifter=shift
        self.s = self.shifter % 26
  
    def _convert(self, text,s):
        """return encrypted string."""
        result = ""
        for i,ch in enumerate(text):     
             if (ch.isupper()):
                  result += chr((ord(ch) + s - 65) % 26 + 65)
             else:
                  result += chr((ord(ch) + s - 97) % 26 + 97)
        return  result
  
    def encrypt(self, text):
        """return encrypted string."""
        return self._convert(text, self.shifter)
        
    def decrypt(self, text):
        """return encrypted string."""
        return self._convert(text, 26-self.s) 
    
class Grade:
    """Class for Grade"""
    def __init__(self, grade_id="", grade="", marks_range=""):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    @staticmethod
    def calculate_grade(marks):
        """Calculate the grade based on marks."""
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"
        
    @staticmethod
    def get_marks_range(grade):
        ranges = {
            "A": "90-100",
            "B": "80-89",
            "C": "70-79",
            "D": "60-69",
            "F": "0-59"
        }
        return ranges.get(grade, "Invalid grade")

    def display_grade_report(self):
        """Display the grade report."""
        print(
            f"Grade ID: {self.grade_id}\n"
            f"Grade: {self.grade}\n"
            f"Marks Range: {self.marks_range}"
        )

class Student:
    """Class for Student"""
    def __init__(self, student_id, first_name, last_name,
                email_address, course_id, professor_id,marks):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id
        self.professor_id = professor_id
        self.marks = float(marks)
        self.grade = Grade.calculate_grade(self.marks)

    def display_record(self):
        """Display the record for student"""
        print(
            f"Student ID: {self.student_id}\n"
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Email Address: {self.email_address}\n"
            f"Course ID: {self.course_id}\n"
            f"Professor ID: {self.professor_id}\n"
            f"Marks: {self.marks}"
        )

    def check_my_grades(self):
        """Check the grade for student"""
        print(f"{self.first_name} {self.last_name}Grade: {self.grade}")

    def check_my_marks(self):
        """Check the marks for student"""
        print(f"{self.first_name} {self.last_name} Marks: {self.marks}")

    def to_list(self):
        """Convert the student record to a list for a future CSV write."""
        return [
            self.student_id,
            self.first_name,
            self.last_name,
            self.email_address,
            self.course_id,
            self.professor_id,
            self.marks,
            self.grade
        ]

    

class Course:
    """Class for Course"""
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = int(credits)

    def display_courses(self):
        """Display the course information."""
        print(
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Credits: {self.credits}"
        )

    def to_list(self):
        """Convert the course record to a list for a future CSV write."""
        return [self.course_id, 
                self.course_name, 
                self.credits
            ]
    
class Professor:
    """Class for Professor"""
    def __init__(self, professor_id, name, email_address, rank, course_id):
        self.professor_id = professor_id
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        """Display the professor information."""
        print(
            f"Professor ID: {self.professor_id}\n"
            f"Name: {self.name}\n"
            f"Email Address: {self.email_address}\n"
            f"Rank: {self.rank}\n"
            f"Course ID: {self.course_id}"
        )

    def to_list(self):
        """Convert the professor record to a list for a future CSV write."""
        return [self.professor_id, 
                self.name, 
                self.email_address, 
                self.rank, 
                self.course_id
            ]
        
class Login_User:
    """Class for Login User"""
    def __init__(self, email_id, password, role):
        self.email_id = email_id
        self.password = password
        self.role = role
        self.security = TextSecurity(4)
    
    def encrypt_password(self):
        """Encrypt the password using Caesar cipher."""
        return self.security.encrypt(self.password)
    
    def decrypt_password(self, encrypted_password):
        """Decrypt the password using Caesar cipher."""
        return self.security.decrypt(encrypted_password)
    
    def to_list(self):
        """Convert the login user record to a list for a future CSV write."""
        return [self.email_id, 
                self.encrypt_password(), 
                self.role
            ]
    
class CheckMyGradeApp:
    "Main application class for Check My Grade App"
    def __init__(self):
        self.students = []
        self.courses = []
        self.professors = []
        self.login_users = []

        self.students_file = "students.csv"
        self.courses_file = "courses.csv"
        self.professors_file = "professors.csv"
        self.login_file = "login.csv"

        self.load_students()
        self.load_courses()
        self.load_professors()
        self.load_login_users()

    def load_students(self):
        """Load students from CSV file."""
        self.students = []
        if os.path.exists(self.students_file):
            with open(self.students_file, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) >= 8:
                        student = Student(
                            row[0], row[1], row[2], row[3],
                            row[4], row[5], row[6]
                        )
                        student.grade = row[7]
                        self.students.append(student)

    def save_students(self):
        with open(self.students_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "student_id", "first_name", "last_name", "email_address",
                "course_id", "professor_id", "marks", "grade"
            ])
            for student in self.students:
                writer.writerow(student.to_list())

    def load_courses(self):
        """Load courses from CSV file."""
        self.courses = []
        if os.path.exists(self.courses_file):
            with open(self.courses_file, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) >= 3:
                        course = Course(row[0], row[1], row[2])
                        self.courses.append(course)

    def save_courses(self):
        with open(self.courses_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["course_id", "course_name", "credits"])
            for course in self.courses:
                writer.writerow(course.to_list())

    def load_professors(self):
        """Load professors from CSV file."""
        self.professors = []
        if os.path.exists(self.professors_file):
            with open(self.professors_file, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) >= 5:
                        professor = Professor(
                            row[0], row[1], row[2], row[3], row[4]
                        )
                        self.professors.append(professor)
    
    def save_professors(self):
        with open(self.professors_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "professor_id", "name", "email_address", "rank", "course_id"
            ])
            for professor in self.professors:
                writer.writerow(professor.to_list())

    def load_login_users(self):
        """Load login users from CSV file."""
        self.login_users = []
        if os.path.exists(self.login_file):
            with open(self.login_file, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) >= 3:
                        login_user = Login_User(
                            row[0], row[1], row[2]
                        )
                        self.login_users.append(login_user)

    def save_login_users(self):
        with open(self.login_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["email_id", "password", "role"])
            for login_user in self.login_users:
                writer.writerow(login_user.to_list())

    # Student functions

    def add_new_student(self, student_id, first_name, last_name,
                    email_address, course_id, professor_id, marks):
        """Add a new student record."""

        for student in self.students:
            if student.student_id == student_id:
                print("Student already exists.")
                return

        new_student = Student(
            student_id, first_name, last_name,
            email_address, course_id, professor_id, marks
        )
        self.students.append(new_student)
        self.save_students()
        print("Student added successfully.")

    def delete_student(self, student_id):
        """Delete a student record."""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def update_student(self, student_id, first_name=None, last_name=None,
                    email_address=None, course_id=None, professor_id=None, marks=None):
        """Update a student record."""
        for student in self.students:
            if student.student_id == student_id:
                if first_name is not None:
                    student.first_name = first_name
                if last_name is not None:
                    student.last_name = last_name
                if email_address is not None:
                    student.email_address = email_address
                if course_id is not None:
                    student.course_id = course_id
                if professor_id is not None:
                    student.professor_id = professor_id
                if marks is not None:
                    student.marks = float(marks)
                    student.grade = Grade.calculate_grade(student.marks)
                self.save_students()
                print("Student updated successfully.")
                return
        print("Student not found.")

    def display_record(self):
        """Display a student record."""
        if not self.students:
            print("No student records found.")
            return
        for student in self.students:
            student.display_record()

    def search_student(self, keyword):
            start_time = time.perf_counter()

            results = []
            keyword = keyword.lower()

            for student in self.students:
                if (
                    keyword in student.student_id.lower()
                    or keyword in student.first_name.lower()
                    or keyword in student.last_name.lower()
                    or keyword in student.email_address.lower()
                    or keyword in student.course_id.lower()
                    or keyword in student.professor_id.lower()
                    or keyword in student.grade.lower()
                ):
                    results.append(student)

            end_time = time.perf_counter()

            print(f"Search completed in {end_time - start_time:.8f} seconds")

            if results:
                for student in results:
                    student.display_record()
            else:
                print("No matching student found.")

    def sort_students_by_name(self):
        """Sort students by name."""
        self.students.sort(key=lambda s: (s.last_name, s.first_name))
        self.save_students()
        print("Students sorted by name successfully.")

    def sort_students_by_marks(self):
        """Sort students by marks."""
        self.students.sort(key=lambda s: s.marks, reverse=True)
        self.save_students()
        print("Students sorted by marks successfully.")

    #Course functions

    def add_new_course(self, course_id, course_name, credits):
        """Add a new course record."""
        for course in self.courses:
            if course.course_id == course_id:
                print("Course already exists.")
                return

        new_course = Course(course_id, course_name, credits)
        self.courses.append(new_course)
        self.save_courses()
        print("Course added successfully.")

    def delete_course(self, course_id):
        """Delete a course record."""
        for course in self.courses:
            if course.course_id == course_id:
                self.courses.remove(course)
                self.save_courses()
                print("Course deleted successfully.")
                return
        print("Course not found.")

    def modify_course(self, course_id, course_name=None, credits=None):
        """Modify an existing course record."""
        for course in self.courses:
            if course.course_id == course_id:
                if course_name is not None:
                    course.course_name = course_name
                if credits is not None:
                    course.credits = credits
                self.save_courses()
                print("Course modified successfully.")
                return
        print("Course not found.")

    def display_courses(self):
        """Display all course records."""
        if not self.courses:
            print("No course records found.")
            return
        for course in self.courses:
            course.display_courses()

    # Professor functions

    def add_new_professor(self, professor_id, name, email_address, rank, course_id):
        """Add a new professor record."""
        for professor in self.professors:
            if professor.professor_id == professor_id:
                print("Professor already exists.")
                return

        new_professor = Professor(
            professor_id, name, email_address, rank, course_id
        )
        self.professors.append(new_professor)
        self.save_professors()
        print("Professor added successfully.")

    def delete_professor(self, professor_id):
        """Delete a professor record."""
        for professor in self.professors:
            if professor.professor_id == professor_id:
                self.professors.remove(professor)
                self.save_professors()
                print("Professor deleted successfully.")
                return
        print("Professor not found.")

    def modify_professor_details(self, professor_id, name=None, email_address=None, rank=None, course_id=None):
        """Modify an existing professor record."""
        for professor in self.professors:
            if professor.professor_id == professor_id:
                if name is not None:
                    professor.name = name
                if email_address is not None:
                    professor.email_address = email_address
                if rank is not None:
                    professor.rank = rank
                if course_id is not None:
                    professor.course_id = course_id
                self.save_professors()
                print("Professor modified successfully.")
                return
        print("Professor not found.")

    def display_professors_details(self):
        """Display professor details."""
        if not self.professors:
            print("No professor records found.")
            return

        for professor in self.professors:
            professor.professors_details()

    def show_course_details_by_professor(self, professor_id):
        """Show course details by professor."""
        for professor in self.professors:
            if professor.professor_id == professor_id:
                course_id = professor.course_id
                for course in self.courses:
                    if course.course_id == course_id:
                        course.display_courses()
                        return
        print("Professor or course not found.")

    # Login User functions

    def add_new_login_user(self, email_id, password, role):
        """Add a new login user record."""
        for login_user in self.login_users:
            if login_user.email_id == email_id:
                print("Login user already exists.")
                return

        new_login_user = Login_User(email_id, password, role)
        self.login_users.append(new_login_user)
        self.save_login_users()
        print("Login user added successfully.")

    def delete_login_user(self, email_id):
        """Delete a login user record."""
        for login_user in self.login_users:
            if login_user.email_id == email_id:
                self.login_users.remove(login_user)
                self.save_login_users()
                print("Login user deleted successfully.")
                return
        print("Login user not found.")

    def login(self, email_id, password):
        """Login a user by checking encrypted password."""
        security = TextSecurity(4)

        for user in self.login_users:
            if user.email_id == email_id:  
                if security.encrypt(password) == security.encrypt(password):  
                    print(f"Login successful for {email_id}.")
                    self.logged_in_user = user
                    return True
                else:
                    print("Incorrect password.")
                    return False

        print("User not found.")
        return False

    def logout(self):
        """Logout the user."""
        print("Logout successful.")

    def change_password(self, email_id, old_password, new_password):
        """Change the password for a login user."""
        security = TextSecurity(4)

        for user in self.login_users:
            if user.email_id == email_id:
                if user.password == old_password:
                    user.password = new_password
                    self.save_login_users()
                    print("Password changed successfully.")
                    return
                else:
                    print("Incorrect old password.")
                    return

        print("User not found.")

    def encrypt_password(self, password):
        """Encrypt the password using Caesar cipher."""
        security = TextSecurity(4)
        return security.encrypt(password)

    def decrypt_password(self, encrypted_password):
        """Decrypt the password using Caesar cipher."""
        security = TextSecurity(4)
        return security.decrypt(encrypted_password)

    #Statistic functions

    def calculate_average_for_course(self, course_id):
        """Calculate the average marks for a course."""
        marks_list = [student.marks for student in self.students if student.course_id == course_id]

        if not marks_list:
            print("No student records found for this course.")
            return

        average = sum(marks_list) / len(marks_list)
        print(f"Average marks for course {course_id}: {average:.2f}")

    def calculate_median_for_course(self, course_id):
        marks_list = [student.marks for student in self.students if student.course_id == course_id]

        if not marks_list:
            print("No student records found for this course.")
            return

        median = statistics.median(marks_list)
        print(f"Median marks for course {course_id}: {median:.2f}")

    #Report functions

    def generate_report_by_course(self, course_id):
        """Generate a report of students enrolled in a course."""
        print(f"Report for Course ID: {course_id}")
        found = False
        for student in self.students:
            if student.course_id == course_id:
                student.display_record()
                found = True
        if not found:
            print("No records found for this course.")

    def generate_report_by_professor(self, professor_id):
        """Generate a report of students taught by a professor."""
        print(f"Report for Professor ID: {professor_id}")
        found = False
        for student in self.students:
            if student.professor_id == professor_id:
                student.display_record()
                found = True
        if not found:
            print("No records found for this professor.")

    def generate_report_by_student(self, student_id):
        """Generate a report for a specific student."""
        print(f"Report for Student ID: {student_id}")
        for student in self.students:
            if student.student_id == student_id:
                student.display_record()
                return
        print("No records found for this student.")

#Testing

if __name__ == "__main__":
    app = CheckMyGradeApp()

    # Add Courses
    app.add_new_course("DATA 200", "Python Programming", 3)
    app.add_new_course("DATA 201", "Databases", 3)

    # Add Professors
    app.add_new_professor("P101", "Minerva McGonagall", "mcgonagal@hogwarts.edu", "Senior Professor", "DATA 200")
    app.add_new_professor("P102", "Severus Snape", "snape@hogwarts.edu", "Associate Professor", "DATA 201")

    # Add Students
    app.add_new_student("S101", "Harry", "Potter", "potter@hogwarts.edu", "DATA 200", "P101", 85)
    app.add_new_student("S102", "Hermione", "Granger", "granger@hogwarts.edu", "DATA 201", "P102", 100)
    app.add_new_student("S103", "Ron", "Weasley", "ron@hogwarts.edu", "DATA 200", "P101", 76)

    # Register Login Users
    app.add_new_login_user("mcgonagal@hogwarts.edu", "Welcome12", "professor")
    app.add_new_login_user("potter@hogwarts.edu", "Student123", "student")

    # Login Test
    app.login("mcgonagal@hogwarts.edu", "Welcome12")



    # Display Records
    print("\nAll Student Records")
    app.display_record()

    print("\nAll Courses")
    app.display_courses()

    print("\nAll Professors")
    app.display_professors_details()

    # Search
    print("\nSearch for 'Hermione'")
    app.search_student("Hermione")

    # Sort
    print("\nSort Students by Name")
    app.sort_students_by_name()
    app.display_record()

    print("\nSort Students by Marks")
    app.sort_students_by_marks()
    app.display_record()

    # Update Student
    print("\nUpdate Student S103")
    app.update_student("S103", marks=88)
    app.generate_report_by_student("S103")

    # Statistics
    print("\nStatistics")
    app.calculate_average_for_course("DATA 200")
    app.calculate_median_for_course("DATA 200")

    # Reports
    app.generate_report_by_course("DATA 200")
    app.generate_report_by_professor("P101")
    app.generate_report_by_student("S101")

    # Change Password
    print("\nChange Password")
    app.change_password("potter@hogwarts.edu", "Student123","NewPass123")
    app.login("potter@hogwarts.edu", "NewPass123")

    # Logout
    app.logout()
