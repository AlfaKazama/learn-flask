# # first-class function berarti functions hanyalah sebuah variable. kita dapat mempassingnya sebagai function dan menggunakannya dengan cara sama seprti kita menggunakan variabel

# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0.")
  
#   return dividend / divisor


# def calculate(*values, operator):
#   return operator(*values)


# # ini akan passing divide function sebagai operator. jadi operator memilki value yang sama dengan function divide
# result = calculate(20, 4, operator=divide)
# print(result)

#################################################################################################################

# # Yang jadi masalah pada code diatas, values parameter pada calculate menerima sejumlah value. Tapi operator cuma mengharapkan 2 value
# # Ketika kita mencoba memasukkan lebih banyak nilai, kita akan mendapatkan error

# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Divisor cannot be 0.")
  
#   return dividend / divisor


# def calculate(*values, operator):
#   return operator(*values)


# result = calculate(20, 4, 5, operator=divide)
# print(result)

#################################################################################################################
# # Misal kita ingin mengetahui teman mana yang namanya "Bob Smith", yang dilist friends tidak ada

# def search(sequence, expected, finder):
#   for elem in sequence:
#     if finder(elem) == expected:
#       return elem
    
#   raise RuntimeError(f"Could not find an element with {expected}")

# friends = [
#   {"name": "Rolf Smith", "age": 24},
#   {"name": "Adam Wool", "age": 30},
#   {"name": "Anne Pun", "age": 27}
# ]

# def get_friend_name(friend):
#   return friend["name"]

# # print(search(friends, "Bob Smith", get_friend_name))
# print(search(friends, "Rolf Smith", get_friend_name))

#################################################################################################################
# Kita bisa menggunakan lambda function

from operator import itemgetter

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
    
  raise RuntimeError(f"Could not find an element with {expected}")

friends = [
  {"name": "Rolf Smith", "age": 24},
  {"name": "Adam Wool", "age": 30},
  {"name": "Anne Pun", "age": 27}
]
  
# menggunakan lambda function
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# Menggunkana imgetter fungsinya sama seperti lambda function
print(search(friends, "Rolf Smith", itemgetter("name")))


# (lambda x, y: print(x + y))(20, 10)