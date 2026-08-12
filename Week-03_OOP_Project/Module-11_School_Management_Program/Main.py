from School import School, ClassRoom, Subject
from Persons import Student, Teacher






def main():
   school = School("Kalidaha SC High", "Kalidaha")

   eight = ClassRoom("Eight")
   school.add_classroom(eight)

   nine = ClassRoom("Nine")
   school.add_classroom(nine)

   ten = ClassRoom("Ten")
   school.add_classroom(ten)


   abir = Student("Abir Sharma", eight)
   school.student_admission(abir)

   bir = Student("bir Sharma", eight)
   school.student_admission(bir)

   ohir = Student("ohir Sharma", eight)
   school.student_admission(ohir)


    # Subject
   physics_teacher = Teacher("Samir Baran Das")
   physics = Subject("Physics", physics_teacher)
   eight.add_subject(physics)

   chemistry_teacher = Teacher("Indralal Dev Nath")
   chemistry = Subject("chemistry", chemistry_teacher)
   eight.add_subject(chemistry)

   Biology_teacher = Teacher("Nusrin Sultana / Liton Kumar Bhowmik")
   Biology = Subject("Biology", Biology_teacher)
   eight.add_subject(Biology)



   print(school)

if __name__ == "__main__":
    main()