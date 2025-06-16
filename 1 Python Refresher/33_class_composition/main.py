# ## Composition adalah counterpart dari inheritance jika kita amembangun class yang menggunakan class lain. Kita akan menggunakan inheritance dengan sedikit pada python. Kita akan lebih banyak menggunakan composition

# # Compisition memungkinkan class kita menjadi lebih sederhana, dan mengurangi kompleksitas code secara keseluruhan

# class BookShelf:
#   def __init__(self, quantity):
#     self.quantity = quantity

#   def __str__(self):
#     return f"BookShelf with {self.quantity} books."

# class Book(BookShelf):
#   def __init__(self, name, quantity):
#     super().__init__(quantity)
#     self.name = name

#   def __str__(self):
#     return f"Book {self.name}"
  
# # shelf = BookShelf(300)
# # print(shelf)

# # Tapi penulisan seperti ini adalah pendekatan yang buruk
# # Ada 2 alasan, salah satu alasannya adalah konseptual, cara berfikir tentangnya. dan yang satunya lagi adalah teknik
# # Alasan konseptualnya adalah: ketika kita melakukan inheritance, kita melakukan evolusi inheritance. Sebagai contoh harimau adalah mamalia, tetapi tidak semua mamalia adalah harimau. jadi semua Book adalah BookShelf, tetapi tidak semua BookShelf adalah Book
# # Alaasan tekniknya adlaah: tidak ada alasan untuk mewarisi, jika kita tidak menggunakan warisan yang diberi. Jadi disinilah composition berperan
# book = Book("Haryy Potter", 120)
# print(book)

#################################################################################################################

# Jadi dari pada kita meangatur "quantity" BookShelf, kita akan mengizinkan constructor untuk dapat mengambil sejumlah Book

class BookShelf:
  def __init__(self, *books):
    self.books = books

  def __str__(self):
    return f"BookShelf with {len(self.books)} books."

# Kita tidak perlu inheritance
class Book:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Book {self.name}"
  


# Sekarang kita diatas memilki dua class yang simple, lalu bagaimana cara menggunakannya?
# Kita cukup membuat object/instance dari Book, kemudian kita membuat instance dari BookShelf dan memberinya buku(instance/obejct)
# Ketika kita memilki class yang berisi sekelompok class yang lain, disini kita memilki "BookShelf" yang berisi banyak "Book" . Dan ketika kita menggunakannya, kita dapat passing sekumpulan instance/object. 

book = Book("Haryy Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

# print(shelf.books)
print(shelf)

