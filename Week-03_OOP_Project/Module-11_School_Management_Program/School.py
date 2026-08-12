class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # Compositions:
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom


    def add_teacher(self, subject, teacher):   
        self.teachers[subject] = teacher


    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            # TODO : set student id (roll num) at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f"No ClassRoom as named {className}")

    def __repr__(self) -> str:
        print("----- All Classrooms -----")
        for key, value in self.classrooms.items():
            print(key)


        print("------ Student ------")
        eight = self.classrooms["Eight"]
        for student in eight.students:
            print(student.name)
        print(len(eight.students))


        print("---- Subject ----")
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        return ""


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # compositon
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f"{self.name} - {len(self.students) + 1}"
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f"{self.name} - {len(self.students)}"


    # TODO : sort students by grade
    def get_to_students(self):
        pass

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 38

            