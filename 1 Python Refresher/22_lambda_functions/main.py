# ## Lambda Functions adalah jenis funcion yang berbeda yang tidak memiliki nama, dan hanya digunakan untuk mengembalikan (return) nilai
# # Ingat sebelumya kita tahu bahwa function dapat digunakan untuk melakukan tindakan seperti mencetak sesuatu, atau mengoperasikan value lalu mereturnnya, seperfi sum function dll.
# # Tapi lambda functions secara ekslusif digunakan untuk mengeoperasikan input dan mereturn output. Mereka hampir tidak pernah digunakan untuk melakukan tindakan

# # simple function yang mendapatkan input dan mengembalikan output
# def add(x, y):
#   return x + y

# print(add(5, 7))

#################################################################################################################

# # kita dapat menulis ulang function diatas dengan lamda function
# # terdiri dari: lambda keword -- parameter: --- return value
# # kita bahkan tidak memerlukan return keyword
# # lambda x, y: x + y 

# # Lambda dimaksudkan untuk menjadi short functions, sering digunakan tanpa memberi mereka nama. misal nya seperti pada penggunaan function bawaan yaitu "map". kita akan belajar map di materi yang akan datang. 
# # kita bisa meassign lambda ke variable jika kita mau
# add = lambda x, y: x + y
# print(add(5, 7))

#################################################################################################################

# # Jika ingin menggunakan lambda function tanpa harus meassign nya kevariable, kita hanya perlu membungkusnya dalam tanda kurung. Python akan menganggapnya sebagai single unit, dan kemudian memanggilfunction nya dengan mengisikan argument yang kita inginkan
# (lambda x, y: x + y)(5, 7)

# # mencetaknya
# print((lambda x, y: x + y)(5, 7))

#################################################################################################################

# def double(x):
#   return x * 2


# # misal kita ingin membuat list yang isinya adalah setiap element dari list sequence yang menjadi dua kali lipatnya
# # kita menggunakan lsit comprehension
# sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# print(doubled)

# # Jadi alih alih menggunakan list comprehension, kita bisa menggunakan map function. Dan disitulah lambda function menjadi sangat berguna
# # Map bisa digunakan pada : list, tupple, set (iterable)
# # apa yang dilakukan map function sepeti ini: 
# # melalui setiap nilai (element) dalam sequence, dan kemudian menerapkan function double pada setiap element dan kemduaian mengembalikan final sequence kepada kita
# doubled = map(double, sequence)
# print(doubled)

# # untuk memprint hasil map nya kita harus mengubahnya ke list, karena map tidak mengembalikan list, tetapi mengembalikan sesuatu yang disebut map object
# doubled = list(map(double, sequence))
# print(doubled)


#################################################################################################################

# Kita bisa menggunakan lambda function pada list comprehension meskipun code akan terlihat membingungkan
sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)

# Jika ingin menggunakan lambda lebih baik lakukan pada map function
doubled = map(lambda x: x * 2, sequence)
print(doubled)
