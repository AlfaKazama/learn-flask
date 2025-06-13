# # Penggunaan kurung pada tuple kadang tidak diperlukan, penggunaan tanda kurung digunakan ketika python akan sulit saat membuat tuple dan kondisi lain bersamaan

# # contoh penggunaan tanda kurung saat membuat tuple didalam list
# x = [(5, 11)]

# # jadi kita bisa membuat tuple seperti ini (tanpa tanda kurung)
# x = 5, 11


# # Destructuring variabel
# # kita bisa memisah nilai seperti berikut
# x, y = 5, 11

# # dengan destructuring kita bisa melakukan ini
# t = 5, 11
# x, y = t

# print(x, y)

########################################################################################################################

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# ## Merubah dictionary menjadi list dengan menggunakan list()
# print(list(student_attendance.items()))

# # student, attendance in student_attendance.items() -> akan menghasilkan tiga tuple yang berbeda
# # for student, attendance in student_attendance.items():
# #   print(f"{student}: {student_attendance}")

# # t disini akan menghasilkan tupple
# for t in student_attendance.items():
#   print(t)

########################################################################################################################

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
# # people = [("Bob", 42), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")] # ketika 1 element hilang, maka akan terjadi error unpack

# # for name, age, profession in people:
# #   print(f"Name: {name}, Age: {age}, Profession: {profession}")

# ## cara yang lebih baik
# for person in people:
#   print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

########################################################################################################################

# # Misal kita ingin mengabaikan nilai 42. Kita bisa memecah variabel dan menggunakan "_". underscore seperti ini dalam komunitas python berarti variabel yang tidak dianggap

# person = ("Bob", 42, "Mechanic")
# name, _, profession = person

# print(name, profession)

########################################################################################################################

# Memisahkan menjadi 2 list
head, *tail = [1, 2, 3, 4, 5] # mengambil 1 nilai dan (*) mengambil sisa nilainya
print(head)
print(tail)