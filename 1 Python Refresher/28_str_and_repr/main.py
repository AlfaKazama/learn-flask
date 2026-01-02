class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


# Dalam  python method dengan dua garis bawah __ disetiap sisi adalah spesial method karena python akan memanggilnya otomatis
# saat memanggil Person() ptyhon akan memanggil init method, meskipun kita tidak menyebutkannya

# Membuat object
bob = Person("Bob", 35)
print(bob) # akan mencetak string yang merepresentikan object bob

#################################################################################################################

# # Kita akan memodifikasi object bob sehingga ketika kita mencetaknya, kita akan mendapatkan informasi yang menarik yang bisa dimanfaatkan user
# # Untuk melakukan itu kita membutuhkan special method __str__()
# # Selain itu juga ada special method __repc__()
# # INGAT KITA TIDAK HARUS MENGGUNAKAN KEDUA SPECIAL METHOD INI, INI HANYA DIGUNAKAN JIKA KITA INGIN MEREPRESENTASIKAN OBJECT

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   # Special method ini akan dipanggil, ketika kita ingin mengubah object kita menjadi string
#   def __str__(self):
#     return f"Person {self.name}, {self.age} years old."
  
#   # Special method ini digunakan untuk mencetak representasi yang tidak ambigu dari suatu object
#   def __repr__(self):     
#     return f"<Person('{self.name}', {self.age})>"



# bob = Person("Bob", 35) 
# print(bob) # akan mencetak string

# # Untuk memanggil special method __repr_() nonaktifkan __str__ method atau kita bisa memanggil methodnya secara manual seperti ini
# print(bob.__repr__())

# # print(Person("Alfa", 25).__repr__())