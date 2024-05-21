from student import Student
from course import Course
from grade_calculator import calculate_gpa

student1=Student("001","piyush")
student2=Student("002","Vrushbh")

ds_course=Course("DS01","Data science 101")
da_course=Course("DA01","Data Analysis 102")

student1.add_course(ds_course,90)
student1.add_course(da_course,85)
student2.add_course(ds_course,78)
student2.add_course(da_course,92)

print(f"{student1.name}'s Grades:{student1.get_grades()}")
print(f"{student2.name}'s Grades:{student2.get_grades()}")

gpa_student1=calculate_gpa(student1.get_grades())
gpa_student2=calculate_gpa(student2.get_grades())
print(f"{student1.name}'s GPA: {gpa_student1:.2f}")
print(f"{student2.name}'s GPA: {gpa_student2:.2f}")