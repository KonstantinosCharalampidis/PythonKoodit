class Student:
    def __init__(self, name):
        self.name = name
        self.is_present = False
class Teacher:
    def __init__(self, name):
        self.name = name
class Lecture:
    def __init__(self, topic, teacher):
        self.topic = topic
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_attendance(self):
        print("\nLecture topic:", self.topic)
        print("Teacher:", self.teacher.name)
        print("Attendance list:")

        present_count = 0
        for s in self.students:
            status = "Present" if s.is_present else "Absent"
            print("-", s.name, ":", status)
            if s.is_present:
                present_count += 1

        print("\nTotal students:", len(self.students))
        print("Present:", present_count)
        print("Absent:", len(self.students) - present_count)

teacher_name = input("Enter teacher name: ")
teacher = Teacher(teacher_name)

topic = input("Enter lecture topic: ")
lecture = Lecture(topic, teacher)

while True:
    student_name = input("Enter student name (or type 'done' to finish): ")
    if student_name.lower() == "done":
        break

    student = Student(student_name)
    status = input(f"Is {student_name} present? (yes/no): ").lower()
    if status == "yes":
        student.is_present = True

    lecture.add_student(student)

lecture.show_attendance()
