# Kita akan membaut function sederhana yang akan menggunakan unpacking key arguments
def named(**kwargs):
  print(kwargs)


# Ini akan menghasilkan sebuah dictionary 
# Apa yang terjadi di python ? kedua key argument ini akan dikumpulkan ke dalam variabel kwargs dan akan ditempatkan dalam sebuah dictionary
# Dimana dictionary keynya sama dengan name dari argument
named(name="Bob", age=25)

#################################################################################################################

# # Kita dapat melakukan sebaliknya, kita dapat membongkar sebuah dictionary menjadi named arguments

# def named(name, age):
#   print(name, age)


# details = {"name": "Bob", "age": 25}
# # Kita tau ini tidak akan berfungsi, karena details adalah dictionary, dan kita mencoba passing sebagai positional arguments
# # yang berarti bahwa details dictionary akan menjadi value dari name parameter, dan age tidak akan memiliki value
# # named(details)

# # named(details, 25) # age parameter memiliki value 25 jika kita melakukan ini

# # Jadi yang kita inginkan adalah passing "name" key sebagai name parameter dan "age" key sebagai age parameter
# # kita akan melakukannya dengan unpacking dictionary menjadi dua named argument dengan melakukan ini
# named(**details)


#################################################################################################################

# def named(**kwargs):
#   print(kwargs)


# details = {"name": "Bob", "age": 25}

# # dengan melakukan ini,  kita akan mengirimkan (pass) beberapa keyword arguments, kemudian mereka dikumpulkan menjadi dictionary
# named(**details)
# # ini sama seperti kita melakukan ini
# named(name="Bob", age=25)


#################################################################################################################

# def named(**kwargs):
#   print(kwargs)

# def print_nicely(**kwargs): ## **kwargs-> mengemas
#   named(**kwargs) ## **kwargs -> membongkar ulang
#   for arg, value in kwargs.items():
#     print(f"{arg}: {value}")


# # Yang terjadi disini kita akan mengumpulkan named argument ke dalam dictionary
# # dan kemudian kita memanggil named() function, tetapi kita akan membongkar dictionary tadi kedalam named argument
# # setelah named() dijalankan akan mereturn menjadi dictionary lagi
# print_nicely(name="Bob", age=25)


#################################################################################################################

# # Kita dapat menggunakan * dan ** secara bersamaan

# def both(*args, **kwargs):
#   print(args)
#   print(kwargs)

# # 1,3,5 akan dicollected menjadi args karena mereka positional argument
# # name="Bob" dan age=25 akan dikumpulkan menjadi kwargs
# both(1, 3, 5, name="Bob", age=25)

#################################################################################################################

## TONTON PENJELASAN PENGGUNAAN * dan ** dalam function function dipython yang umum di menit 06:51

#################################################################################################################

# def myfunctions(**kwargs):
#   print(kwargs)

# # myfunctions(**"Bob") # ERROR, must be a mapping. Karena yang dipassing haruslah dictionary, ini string
# # myfunctions(**None) # ERROR Karena yang dipassing haruslah dictionary
# myfunctions(**{"test": "Testing"})
