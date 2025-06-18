# def divide(dividend, divisor):
#   if divisor == 0:
#     print("Divisor cannot be 0")
#     return
  
#   return dividend / divisor


# # divide(15, 0)

# grades = [78, 99, 85, 100]

# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}")

#################################################################################################################
# # Namun jika kita ingin mencetak error yang lebih bagus, jika kita tidak menggunakan user error(kondisi if error)

# def divide(dividend, divisor):
#   if divisor == 0:
#     print("Divisor cannot be 0")
#     return
  
#   return dividend / divisor

# grades = []

# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}") # ini mencetak none, ini tidak bagus 

# print(sum(grades), len(grades))


#################################################################################################################
# # Di ptyhon, errors sering digunaan untk flow control, sangat mirip denagan if statement, meskipun kita membiarkan function kita menimbulkan errors namun kita bisa menangkap(catch) error tersebut dan kemudian menghadlenya
# # Kita menggunakan "raise" dan menggunakan exception name (erro name): "ZeroDivisionError()". Kemduaina message errornya
# # jadi kita membuat exception object, karnea "ZeroDivisionError" adalah class yang ada di ptyhon
# # Dengan membuat ini kita tidak menunjukkan error kepada users, tapi ini sangat membantu karena menjelaskan dimana error tersebut terjadi
# # Errors membantu kita untuk melacak masalah, dimana dan mengapa hal itu terjadi. Error memberi developer tools untuk melakukan debugging

# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0")
#   return dividend / divisor

# grades = []

# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}") 


#################################################################################################################

# Kita dapat menangkap(catch) error, jika terjadi kesalahan kita ingin melakukan sesuatu. 
# Untuk melakukan itu kita memerlukan syntax try-except block

# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0")
#   return dividend / divisor

# grades = []

# print("Welcome to the average grade program.")

# # jika line tersebut error, error akan di catch
# # Jika kita mendapati ZeroDivisionError, kita tidak akan mencetak traceback, tetapi kita mencetak "There are no grades yet in yor list."
# # Jika kita membuat error ZeroDivision pada line lain, dan kita tidak membungkusnya dalam try-except block, error traceback akan dicetak: "Divisor cannot be 0"
# # Jadi code dibawah ini digunakan untuk menghandle dan mencath error
# try:
#   average = divide(sum(grades), len(grades))
# except ZeroDivisionError:
#   print("There are no grades yet in yor list.")

# # print(f"The average grade is {average}")

#################################################################################################################

# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0")
#   return dividend / divisor

# grades = []

# print("Welcome to the average grade program.")

# # pada except block kita bisa menuliskan "as e", ini akan membuat variable e dan memasukkan value error kedalamnya jika ada
# # kita bisa menamainya selain "e", sesuai dengan yang kita inginkan
# try:
#   average = divide(sum(grades), len(grades))
#   print(f"The average grade is {average}")
# except ZeroDivisionError as e:
#   print(e)
#   print("There are no grades yet in yor list.")


# # Ketahuilah ada jenis error lain selain ZeroDivisionError
# # ada "TypeError", error yang terjadi ketika typenya salah
# # ada "ValueError", error yang terjadi ketika valuenya salah atau  value tidak diharapkan (unexpecte value)
# # ada "RuntimeError" dan ada banyak jenis error lainnya
# # Dan kita juga bisa membuat error kita sendiri

#################################################################################################################
# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0")
#   return dividend / divisor

# grades = []

# print("Welcome to the average grade program.")

# # Kita juga dapat menggunakan else, else akan dijalankan ketika program nya berhasil (error tidak terjadi)
# # Kita menggunakan error biasanya, ketika kita ingin menangkap(catch) beberapa error dalam baris code tertentu, dan disaat bersamaan kita tidak ingin menempatkan code kita dalam block yang sama
# # Jika kita ingin menjalankan sepotong code, tidak perduli, ada error atau tidak ada error. gunakan "finally"
# try:
#   average = divide(sum(grades), len(grades))
# except ZeroDivisionError as e:
#   # print(e)
#   print("There are no grades yet in yor list.")
# # # Kita juga bisa membuat kondisi error lain
# # except ValueError:
# #   pass
# else:
#   print(f"The average grade is {average}.")
# finally:
#   print("Thank you!")

#################################################################################################################

def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cannot be 0.")
  
  return dividend / divisor

students = [
  {"name": "Bob", "grades": [75, 90]},
  {"name": "Rolf", "grades": [50]},
  {"name": "Jen", "grades": [100, 90]},
]

try:
  for student in students:
    name = student["name"]
    grades = student["grades"]
    average = divide(sum(grades), len(grades))
    print(f"{name} averaged {average}.")
except ZeroDivisionError:
  print(f"ERROR: {name} has no grades!")
else:
  print("-- All student averages calculated --")
finally:
  print("-- End of student average calculation ")