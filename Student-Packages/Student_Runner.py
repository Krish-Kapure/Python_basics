from student_package.student import Student

Student.school_name = "Global school"
Student.school_address = "Chennai"

student1 = Student(1001, "Krishna", "krish@gmail.com", 99.99)
student2 = Student(1002, "shivanshu", "shiv@gmail.com", 89.99)
student3 = Student(1003, "dhruvil", "dhruvil@gmail.com", 79.99)

student1 = student2

print(student1.get_student_name)
print(student1.get_name_with_percentage)

print(Student.get_school_details())