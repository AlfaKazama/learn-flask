# class ClassTest:

#   # Semua function didalam class yang menggunakan object (self) sebagai parameter pertama disebut instance methods
#   # method ini untuk mendapatkan instance
#   def instance_method(self):
#     print(f"called instance_method of {self}")


# # Membuat object bertipe classTest (atau kita bisa menyebut proses ini: membuat instance dari classTest)
# test = ClassTest()

# # Mendapatkan instance_method dari object yang kita buat
# test.instance_method() # bisa gini
# ClassTest.instance_method(test) # bisa juga gini


#################################################################################################################

# class ClassTest:

#   # Semua function didalam class yang menggunakan object (self) sebagai parameter pertama disebut instance methods
#   # method ini untuk mendapatkan instance
#   def instance_method(self):
#     print(f"called instance_method of {self}")

#   # Kita bisa membuat method lain, namun alih alih menggunakan self/instance kita membutuhkan parameter yang berbeda
#   # kita akan membuat parameter "cls", karena nama cls umum digunakan pada python (tapi kita bisa menggunakan nama lain)
#   # disini kita membuat namanya  functionya "class_method", namun kita bisa menamai nya apa saja
#   # method ini untuk mendapatkan class
#   @classmethod
#   def class_method(cls):
#     print(f"Called class_method of {cls}")



# # kita tidak memerlukan instance dalam memanggil @classmethod
# ClassTest.class_method() ## menuliskan seperti ini, sama saja dengan seperti ini: ClassTest.class_method(ClassTest)

#################################################################################################################

# class ClassTest:

#   # Semua function didalam class yang menggunakan object (self) sebagai parameter pertama disebut instance methods
#   # method ini untuk mendapatkan instance
#   def instance_method(self):
#     print(f"called instance_method of {self}")

#   # Kita bisa membuat method lain, namun alih alih menggunakan self/instance kita membutuhkan parameter yang berbeda
#   # kita akan membuat parameter "cls", karena nama cls umum digunakan pada python (tapi kita bisa menggunakan nama lain)
#   # disini kita membuat namanya  functionya "class_method", namun kita bisa menamai nya apa saja
#   # method ini untuk mendapatkan class
#   @classmethod
#   def class_method(cls):
#     print(f"Called class_method of {cls}")


#   # Dalam static method, method ini tidak memilki parameter, dan ketika memanggil method ini kita tidak mendapatkan apapun
#   # method ini tidak mendapatkan apapun
#   @staticmethod
#   def static_method():
#     print("Called static_method.")


# # cara memanggil static method
# ClassTest.static_method()

#################################################################################################################

class Book:
  # Membuat properties
  TYPES = ("hardcover", "paperback")

  def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight
  
  def __repr__(self):
    return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
  
  @classmethod
  def hardcover(cls, name, page_weight):
    # return Book(name, cls.TYPES[0], page_weight + 100)
    return cls(name, cls.TYPES[0], page_weight + 100)
  
  @classmethod
  def paperback(cls, name, page_weight):
    return cls(name, cls.TYPES[1], page_weight)

# # Mengakses properties
# print(Book.TYPES)

# book = Book("Harry Potter", "comic book", 1500)
# # print(book.name)
# print(book)

book = Book.hardcover("Hary Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)