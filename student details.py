import csv

class Student:
    def __init__(self, name, roll_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name
        self.subjects = {}

    def add_subject(self, subject_name, marks):
        self.subjects[subject_name] = marks

    def get_details(self):
        return f"Name: {self.name} , Roll_no: {self.roll_no} , Class_name: {self.class_name}"


class Reportcard:
    def __init__(self, student):
        self.student = student
     
    def calculate_total(self):
        return sum(self.student.subjects.values())
    
    def calculate_percentage(self):
        total_subjects = len(self.student.subjects)
        if total_subjects == 0:
            return 0 
        total_marks = self.calculate_total()
        percentage = (total_marks / (total_subjects * 100)) * 100
        return percentage

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("\nReport Card....")
        print(f"Student Name: {self.student.name}")  
        print(f"Roll_no: {self.student.roll_no}")
        print(f"Class: {self.student.class_name}")
        print("\nSubjects & Marks:")
        for subject, marks in self.student.subjects.items():
            print(f"{subject}: {marks}")

        total = self.calculate_total()
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()

        print(f"Total Marks = {total}")
        print(f"Total Percentage = {percentage:.2f}%")
        print(f"Grade card = {grade}")
        print("-----------------------")


class SchoolSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\nEnter Student Details.... ")
        name = input("Enter Student Name: ")
        roll_no = int(input("Enter Roll_no: "))
        class_Name = input("Enter Class Name: ")
        student = Student(name, roll_no, class_Name)
    
        num_subjects = int(input("Enter Number Of Subjects: "))
        for i in range(num_subjects):
            subject_name = input(f"Enter the subject Name {i+1}: ")
            marks = int(input(f"Enter the marks for {subject_name}: "))
            student.add_subject(subject_name, marks)

        self.students.append(student)

    def show_reportcard(self):
        print("\n------All Students Report Card-------")
        for student in self.students:
            report = Reportcard(student)
            report.display_report()

    # ✅ NEW FEATURE (CSV SAVE) — existing code untouched
    def save_to_csv(self, filename="students_data.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["Name", "Roll No", "Class", "Subject", "Marks", "Percentage", "Grade"])
            
            for student in self.students:
                report = Reportcard(student)
                percentage = report.calculate_percentage()
                grade = report.calculate_grade()
                
                for subject, marks in student.subjects.items():
                    writer.writerow([
                        student.name,
                        student.roll_no,
                        student.class_name,
                        subject,
                        marks,
                        round(percentage, 2),
                        grade
                    ])


# -------- MAIN PROGRAM --------

school = SchoolSystem()

num_students = int(input("Enter Number Of Students: "))
for i in range(num_students):
    school.add_student()

school.show_reportcard()

# ✅ CSV SAVE CALL
school.save_to_csv()
print("\nData saved to CSV successfully!")