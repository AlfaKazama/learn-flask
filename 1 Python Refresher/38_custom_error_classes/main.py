class Book:
  def __init__(self, name: str, page_count: int):
    self.name = name
    self.page_count = page_count
    self.pages_read = 0

  def __repr__(self):
    return (
      f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
    )
  
  def read(self, pages:int):
    self.pages_read += pages
    print(f"You have now read {self.pages_read} pages out of {self.page_count}.")


python101 = Book("Python 101", 50)
# Kita memiliki 50 halaman, tatapi kita membaca 85 halaman, harusnya tidak bisa
python101.read(35)
python101.read(50)



##################################################################################################################
# # Kita akan membuat jenis error baru dengan anama "TooManyPagesReadError" 
# # Kita akan membuat class "TooManyPagesReadError" (letaknya tidak masalah ada sebelum atau sesudah class Book)
# # class ini inherit dari class VallueError. kita perlu menggunakan inherit agar mempermudah dalam pembuatannya
# # jadi class TooManyPagesReadError adalah salinan dari class ValueError

# class TooManyPagesReadError(ValueError):
#   pass

# class Book:
#   def __init__(self, name: str, page_count: int):
#     self.name = name
#     self.page_count = page_count
#     self.pages_read = 0

#   def __reps__(self):
#     return (
#       f"<Book {self.name}, read {self.paage_read} pages out of {self.page_count}>"
#     )
  
#   def read(self, pages:int):
#     if self.pages_read + pages > self.page_count:
#       raise TooManyPagesReadError(
#         f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
#       )
#     self.pages_read += pages
#     print(f"You have now read {self.pages_read} pages out of {self.page_count}.")


# python101 = Book("Python 101", 50)
# # python101.read(35)
# # python101.read(50)

# # Kita bisa menggunakan try catch
# try:
#   python101.read(35)
#   python101.read(50)
# except TooManyPagesReadError as e:
#   print(e)