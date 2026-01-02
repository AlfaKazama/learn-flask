student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
  return sum(sequence) / len(sequence)

print(average(student["grades"]))

# Kita ingin memanggil method dengan cara seperti dibawah ini. Ini bisa dilakukan pada OOP, tapi untuk melakukan ini, "student" tidak bisa menjadi sebuah dictionary, karena pada dictionary kita tidak bisa melakukan ini
# kita harus membaut kode kita sendiri di python yang memungkinkan kita memangggila average method didalamnya
# print(student.average()) # ini akan error, karena kita blum bisa melakukannya

#################################################################################################################

# # Jadi mari kita tulis ulang code diatas menggunakan OOP

# # Kita menggunakan keyword "class" untuk membuat class pada OOP, disusul dengan nama classnya
# # kita membuat special funcition menggunakan keyword __init__(self). "self" just variable name, tapi menggunakan nama "self" karena self konvensi diptyhon (umum digunakan). Kita juga bisa tidak menggunakan self  parameter, jika ingin.
# class Student:
#   def __init__(self):
#     self.name = "Rolf" # ini mengakses propertie name didalam self
#     self.grades = (90, 90, 93, 78, 90)

#   def average_grade(self):
#     return sum(self.grades) / len(self.grades)


# # Membuat object dari class    
# student = Student() 
# print(student.name)
# print(student.grades)

# # print(Student.average_grade(student))
# # print(Student.average_grade(Student()))
# print(student.average_grade())

# print(Student())
# print(Student)

#################################################################################################################

# # Membuat class dengan constructor yang memiliki parameter

# class Student:
#   # Ini disebut constructor
#   def __init__(self, name, grades):
#     self.name = name # ini properties
#     self.grades = grades

#   # Ini disebut method
#   def average_grade(self):
#     return sum(self.grades) / len(self.grades)


# # Membuat 2 object student dari class Student
# student1 = Student(name="Bob", grades=(100, 100, 93, 78, 90))
# student2 = Student("Rolf", (90, 90, 93, 78, 90))

# print(student1, student2) # object disimpan pada alamat memori yang berbeda
# print(student1.name)
# print(student2.name)

# print(student1.average_grade())
# print(student2.average_grade())