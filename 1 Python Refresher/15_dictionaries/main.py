# ## Dictionary
# ## Dictionary terdiri dari key dan values. Key harus bertipe string atau type data hash

# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# print(friend_ages["Adam"]) # kita mencetak value dengan memanggil key

# # Add element in dictionary
# friend_ages["Bob"] = 20

# # change value of key
# friend_ages["Rolf"] = 20
# print(friend_ages)

########################################################################################################################
# ## LIST of Dictionary
# friends = [
#   {"name": "Rolf", "age": 24},
#   {"name": "Adam", "age": 30},
#   {"name": "Anne", "age": 27},
# ]

# print(friends[1]["name"])

########################################################################################################################

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# ##  Mengakses dictionary dalam loop
# for student in student_attendance:
#   print(f"{student}: {student_attendance[student]}")

# ## Ada cara yang lebih baik dalam mengakses dictionary dalam loop, yaitu menggunakan items()
# for student, attendance in student_attendance.items():
#   print(f"{student}: {attendance}")


# ## kita juga bisa menggunakan "in" keyword untuk mengecek apakah ada nilai dalam sebuah dictionary
# if "Bob" in student_attendance:
#   print(f"Bob: {student_attendance['Bob']}")
# else:
#   print("Bob is not a student in this class.")

## Menghitung rata rata nilai, menggunakan .values()
attendance_values = student_attendance.values()
# print(attendance_values)

print(sum(attendance_values) / len(attendance_values))