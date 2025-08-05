import json
import os

class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(data['roll_no'], data['name'], data['age'], data['grade'])


class StudentManager:
    def __init__(self, filepath='students.json'):
        self.filepath = filepath
        self.students = []
        self.load_data()

    def add_student(self, student):
        self.students.append(student)
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("⚠ No students found.")
            return
        print("\n📋 All Students:")
        for student in self.students:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"\n🔍 Found: Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return student
        print("❌ Student not found.")
        return None

    def update_student(self, roll_no, name=None, age=None, grade=None):
        student = self.search_student(roll_no)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print("✅ Student information updated.")
        else:
            print("❌ Cannot update. Student not found.")

    def delete_student(self, roll_no):
        student = self.search_student(roll_no)
        if student:
            self.students.remove(student)
            print("🗑 Student deleted successfully.")
        else:
            print("❌ Cannot delete. Student not found.")

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump([student.to_dict() for student in self.students], f, indent=4)
        print("💾 Data saved.")

    def load_data(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, 'r') as f:
            try:
                data = json.load(f)
                self.students = [Student.from_dict(s) for s in data]
                print("📂 Data loaded.")
            except json.JSONDecodeError:
                print("⚠ Error loading data. Starting fresh.")


def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save and Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            student = Student(roll_no, name, age, grade)
            manager.add_student(student)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            roll_no = input("Enter roll number to search: ")
            manager.search_student(roll_no)

        elif choice == '4':
            roll_no = input("Enter roll number to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            manager.update_student(roll_no, name or None, age or None, grade or None)

        elif choice == '5':
            roll_no = input("Enter roll number to delete: ")
            manager.delete_student(roll_no)

        elif choice == '6':
            manager.save_data()
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
