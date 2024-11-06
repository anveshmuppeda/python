# Student Grade
### Create a system that calculates and stores student grades. It asks for student names and scores, calculates their grades, and stores them in a list
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()
    def calculate_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'
class GradeBook:
    def __init__(self):
        self.students = []
    def add_student(self):
        name = input("Enter student name: ")
        score = float(input("Enter student score (0-100): "))

        while score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            score = float(input("Enter student score (0-100): "))

        student = Student(name, score)
        self.students.append(student)

        print(f"Student {name} added with grade {student.grade}.")
    def display_grades(self):
        if not self.students:
            print("No students in the list ")
        else:
            print("\nGrade Book:")
            for student in self.students:
                print(f"{student.name}: {student.score} ({student.grade})")

def main():
    grade_book = GradeBook()

    while True:
        print("\nStudent memu:")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            grade_book.add_student()
        elif choice == '2':
            grade_book.display_grades()
        elif choice == '3':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
# Example(output)
Student memu:
1. Add Student
2. Display Student
3. Quit
Enter your choice: 1
Enter student name: ajay
Enter student score (0-100): 85
Student ajay added with grade B.

Student memu:
1. Add Student
2. Display Student
3. Quit
Enter your choice: 2

Grade Book:
ajay: 85.0 (B)