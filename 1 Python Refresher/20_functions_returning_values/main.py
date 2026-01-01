## Function returning

def add(x, y):
  print(x + y)

add(5, 8)

# jika kita melakukan ini, kita akan menjalankan function add() karena kita memanggilnya dan kemudian kita menetapkan nilainya ke variable result dan kita mencetak result variable
# tapi saat mencetak result kita akan mencetak "None"
# None adalah spesial function pada python yang berarti tidak ada value, missing value, atau undeclared value
# itu berarti bahwa function add(10, 2), ketika kita selesai menjalankannya, akan membuat variable result menghasilkan none
result = add(10, 2)
print(result)

# jika kamu melakukan ini, maka akan mencetak apa yang dicetak function dan none
# add function() akan dijalankan terlebih dahulu, print akan mencetak x + y, dan kemudian akan mengembalikan none dan mencetak none
print(add(11, 9))

#################################################################################################################

# ## Dari contoh diatas disinilah peran dari return values. Function akan mengembalikan (mereturn) None, itu yang mereka lakukan secara default.  Jika ingin mendapatkan/mengembalikan value, maka kita harus menggunakan keyword return

# def add(x, y):
#   return x + y

# add(5, 8) # tidak akan ada yang dicetak, karana functionnya tidak mencetak apapun
# result = add(10, 2)
# print(result)

#################################################################################################################

# # Jika kita melakan ini, ini akan mencetak 2 kali

# def add(x, y):
#   print(x + y)
#   return x + y

# result = add(10, 2)
# print(result)

# print(add(13, 5))

#################################################################################################################

# # Jika kita melakukan ini, print pada function tidak akan dijalankan. Karena line code setelah return tidak akan dieksekusi

# def add(x, y):
#   # return # ini akan return none dan membuat kedua line dibawahnya tidak dieksekusi 
#   return x + y
#   print(x + y)

# result = add(10, 2)
# print(result)

#################################################################################################################

# # Menggunakan function yang sebelumnya kita pelajari

# def divide(dividend, divisor):
#   if divisor != 0:
#     return dividend / divisor
#   else:
#     return "You fool!"

# # result = divide(15, 3)

# # function diatas mereturn 2 tipe, yang pertama integer, yang kedua string. Function seperti ini tidak disarankan sebenarnya, karena misal kita melakukan perubahan operation maka akan seperti ini
# result = divide(15, 3) * 5 # ini akan berhasil karena function mereturn integer 
# print(result)

# result = divide(15, 0) * 5 # ini akan mencetak string sbanyak 5 kali
# print(result)

