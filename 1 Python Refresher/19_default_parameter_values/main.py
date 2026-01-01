# Disini kita memiliki 2 parameter x dan y
# kita bisa menggunakan default parameter (nilai default pada parameter)
# Jika kita melakukan seperti dibawah ini, y adalah optional parameter, jadi tidak apa untuk tidak memberikan value y saaat memanggil function
# tapi ingat x tetap harus diberi value saat memanggil function, karena x tidak menggunakan default parameter
def add(x, y=8):
  print(x + y)

# add(5, 8)
add(5)
add(x=5)
add(7, 11)

########################################################################################################

# def add(x, y=8):
#   print(x + y)

# # add(5, 8)
# add(x=5, y=5)
# # add(x=5, 5) # tidak bisa melakukan ini, karena kita tidak bisa menempatkan positional argument setelah keyword argument

########################################################################################################

# # selain itu pada function kita juga tidak bisa memiliki parameter default, diikuti dengan parameter non default
# # akan error:
# def add(x=5, y):
#   print(x + y)

# # add(5, 8)
# add(x=5, y=5)

########################################################################################################

# # Kita tidak bisa menset parameter default dengan nilai dari variabel karena akan berakibat buruk, jadi tidak di rekomendasikan
# default_y = 3

# def add(x, y=default_y):
#   sum = x + y
#   print(sum)

# add(2)

# default_y = 4
# # kita akan mendapatkan value yang sama seperti sebelumnya, karena mengubah variable yang telah digunakan tidak memodifikasi function. jadi nilai default_y  = 3 akan didefinisikan saat function dibuat
# add(2) 