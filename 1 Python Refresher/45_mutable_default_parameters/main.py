# # mutable default parameter

# # Pada grades parameter kita memiliki default value empty list
# # Jangan pernah membuat parameter sama dengan mutable value secara default

# from typing import List

# class Student:
#   def __init__(self, name: str, grades: List[int]= []): # This is bad!
#     self.name = name
#     self.grades = grades

#   def take_exam(self, result):
#     self.grades.append(result)



# ## Tidak akan ada masalah
# # bob = Student("Bob")
# # bob.take_exam(90)
# # print(bob.grades)

# # # Namun bagaimana jika kita membuat student lain(instance / object lain)
# # # dan misal kita tidak memanggil take.exam() pada rolf
# # # Perhatikan kedua studnet memilki element 90, padahal hanya bob yang memanggil take.exam()
# # # Inilah mengapa multabiluty sangatlah penting, dan itulah alasan mengapa membuat parameter sama dengan mutable value secara default adalah ide yang sangat buruk
# # bob = Student("Bob")
# # rolf = Student("Rolf")
# # bob.take_exam(90)
# # print(bob.grades)
# # print(rolf.grades)

# # Jadi ketika class "Student" dibuat, function __init__() di evaluasi sehingga ptyhon mengetahui apa parameternya dan apa name dan seterusnya begitu juga dengan function take_exam()
# # dan nilai default value akan tercipta, itu berati jika kita menggunakan default "self.grades" adalah name dari empty list [] (default value) 
# # dan ketika kita membuat 2 student, "self.grades" keduanya adalah name dari empty list yang sama
# # ini karena default value empty list dibuat (diassign) saat function dibuat bukan saat function dipanggil

# # Jika kita membuat list pada bob, maka akan berbeda. karena bob menggunakan list [70, 80] dan rolf menggunakan empty list
# bob = Student("Bob", [70, 80])
# rolf = Student("Rolf")
# bob.take_exam(90)
# print(bob.grades)
# print(rolf.grades)


#############################################################################################################

# Jadi hindari mutable default value untuk parameter, sebaliknya kita membuat "None" sebagai default valuenya
# Kita dapat menambahkan import Optional, untuk memberi tahu python bawaha parameter List[int] adalah optional

from typing import List, Optional

class Student:
  def __init__(self, name: str, grades: Optional[List[int]] = None): # This is bad!
    self.name = name
    self.grades = grades or []

  def take_exam(self, result):
    self.grades.append(result)



bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
