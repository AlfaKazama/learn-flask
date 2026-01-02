## Dictionary comprehensions sangat mirip dengan list comprehension. Tetapi bedanya kita mendapatkan dictionary di akhir. Jadi kita perlu menerapkan pasangan key value Bob

users = [
  (0, "Bob", "password"),
  (1, "Rolf", "bob123"),
  (2, "Jose", "longp4assword"),
  (3, "Username", "1234")
]

# Dicitionaru comprehession --> {key: value for x in num }
username_mapping = {user[1]: user for user in users}

print(username_mapping)

# # Mengapa ini berguna ? bayangkan kita mengetahui username seseorang, dan kita ingin mengambil informasinya
# # kita bisa melakukan ini, dan akan mendapatkan informasinya
# print(username_mapping["Bob"])

# # Jika kita tidak memiliki mapping, kita harus melakukan seperti dibawah ini
# for user in users:
#   if user[1] == "Bob":
#     print(user)

#################################################################################################################

# # Misal kita melakukan simulasi login

# username_mapping = {user[1]: user for user in users}

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# # kita bisa melakukan ini, untuk mendapatkan tupple informasi user
# _, username, password = username_mapping[username_input]

# if password_input == password:
#   print("Your details are correct!")
# else:
#   print("Your details are incorrect.")