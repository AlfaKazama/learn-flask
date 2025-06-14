# # (*) asterik pada parameter berarti mengumpulkan argument, jadi function akan memilki separangkat argument yang dikumpulkan menjadi sebuah tuple argument, ketika function dipanggil

# def multiply(*args):
#   print(args)

# multiply(1, 3, 5) # kita akan memilki tuple dengan isi 1,3,5

#################################################################################################################

# # Jadi dengan asterik (*) kita dapat mengumpulkan beberapa arguments menjadi satu variable ketika kita memanggil funcion 

# def multiply(*args):
#   print(args)
#   total = 1
#   for arg in args:
#     total = total * arg
#   return total

# print(multiply(-1)) # akan menghasilkan tuple dengan 1 element saja
# print(multiply(1, 3, 5))

#################################################################################################################

# def add(x, y):
#   # print(x, y)
#   return x + y

# nums = [3, 5]
# # dengan asterik(*) kita bisa melakukan kebalikann dri contoh sebelumnya. Kita bisa menggunakan asterik untuk mendestructur arguments menjadi beberapa parameter
# print(add(*nums)) # ini berarti x = 3, y = 5


# # Kita juga bisa menggunakan dictionary sebagai argument untuk functions
# nums = {"x": 15, "y": 25}
# print(add(x=nums["x"], y=nums["y"]))
# # alih alih melakukan seperti diatas kita dapat melakukan ini, karna nama variable parameter sama denga key pada nums
# # dengan menggunakan ** berarti kita memilki dictionary dua keys, dan kita akan pass setiap key dengan nama argument dan nilainya akan terkait dengan key. Jika kondisi seperti ini key dan name argument sama lebih baik gunakan ** agar lebih singkat
# print(add(**nums)) 


#################################################################################################################

def multiply(*args):
  # print(args)
  total = 1
  for arg in args:
    total = total * arg
  return total

def apply(*args, operator):
  print(args)
  if operator == "*":
    return multiply(*args) # pengunaan asterik* disini untuk membongkar tuple, karna args disini adalah tuple, jadi kita bongkar
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator provided to apply()."
  
# Kita harus memasukkan named argument (operator=), jika tidak maka python akan mencoba mengumpulkannya dengan args. jadi kita akan kehilangan parameter operator
print(apply(1, 3, 6, 7, operator="*"))