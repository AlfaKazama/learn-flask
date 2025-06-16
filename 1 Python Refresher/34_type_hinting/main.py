# def list_avg(sequence):
#   return sum(sequence) / len(sequence)

# list_avg(123) # ini akan error, karena sum() dan len() meneria masukan iterable, tapi tidak ada yang meberi tahu kita kalo masukannya iterable. jadi untuk mencegah kesalahan, itu salah satu kegunaan type hinting

#################################################################################################################

# # Dengan menambahkan ":list" python akan memberitahukan bahwa ini harus berupa iterable. dan "-> float" memberitahu bahwa function nya akan mengembalikan float. jadi beginilah type hinting di ptyhon
# def list_avg(sequence: list) -> float:
#   return sum(sequence) / len(sequence)

# list_avg(123) 


#################################################################################################################

# # menggunakan seperti ini ":list" sebenernya tidak direkomendasikan. biasnaya kita akan melakukannya dengan menggunakan import
# from typing import List

# def list_avg(sequence: List) -> float:
#   return sum(sequence) / len(sequence)


# # Jika kita menggunakan IDE seperti pycharm, pycharm akan memberi tahu bahwa masukan dibawah ini salah
# list_avg(123) 


#################################################################################################################

# # Kita dapat menggunakan type hinting dimana saja, misalanya pada class
# class Book:
#   def __init__(self, name: str, page_count: int):
#     self.name = name
#     self.page_count = page_count


#################################################################################################################

# from typing import List   # , Tuple, Set, etc ...

# class Book:
#   pass

# class BookShelf:
  
#   # Ini berarti parameter books harus berupa "Book" object
#   def __init__(self, books: List[Book]):
#     self.books = books

#   # Ini akan mengembalikan string
#   def __str__(self) -> str:
#     return f"BookShelf with {len(self.books)} books."
  

#################################################################################################################

class Book:
  TYPES = ("hardcover", "paperback")

  def __init__(self, name: str, book_type: str, weight: int):
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __repr__(self) -> str:
    return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
  

  # kita menggunakan type hint "Book" disini menggunakan string untuk penanda. karena kita tidak bisa menuliskannya tanpa string. Karena method ini dijalankan sebelum class Book selesai diseksekusi (Jenisnya sama dengan yang kita jalankan). Jika misal kita memaksudkannya untuk class lain kita tidak perlu tanda kutip. misal class BookShelf, jadi kita bisa menuliskannya ....)-> BookShelf:
  @classmethod
  def hardcover(cls, name: str, page_weight: int) -> "Book":
    return cls(name, cls.TYPES[0], page_weight + 100)
  
  @classmethod
  def paperback(cls, name: str, page_weight: int) -> "Book":
    return cls(name, cls.TYPES[1], page_weight)