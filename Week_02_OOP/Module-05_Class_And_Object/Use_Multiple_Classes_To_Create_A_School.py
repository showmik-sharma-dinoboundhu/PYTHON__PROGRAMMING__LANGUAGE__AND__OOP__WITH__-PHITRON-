class Student:
    def __init__(self,name,id,Class):
        self.name = name
        self.id = id
        self.Class = Class

    def __repr__(self) -> str:
        return f"Student With Name: {self.name}, Class: {self.Class}, ID: {self.id}"
    

class Teacher:
    def __init__(self,Name,Subject,ID) -> None:
        self.Name = Name
        self.Subject = Subject
        self.ID = ID

    def __repr__(self) -> str:
        return f"Teacher: {self.Name}, Subject: {self.Subject}"


class School:
    def __init__(self,Name,Situated) -> None:
        self.Name = Name
        self.Situated = Situated
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee < 6500:
            return f"Not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name,"c",id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}, extra money {fee - 6500}"

    def __repr__(self) -> str:
        print("Welcome to",self.Name)
        print("--------Our Teacher--------")
        for teacher in self.teachers:
            print(teacher)
        print("---------Our Students--------")
        for student in self.students:
            print(student)
        return "All done here"




alia = Student("Alia Torkari",9,1)
Ranbir = Teacher("Ranbir Kapoor", "Algorithm",102)


print(alia)
print(Ranbir)

phitron = School("Phitron", "Dhaka")
phitron.enroll("Alia",5200)
phitron.enroll("Rani",7000)
phitron.enroll("Aiswariya",8000)
phitron.enroll("Vaijan",9000)

phitron.add_teacher("Tom Cruise","Data Structure")
phitron.add_teacher("Decap","Algorithms")
phitron.add_teacher("AJ","Database")

print(phitron)