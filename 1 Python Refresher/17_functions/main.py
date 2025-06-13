# # Membuat function sederhana

# def hello():
#   print("Hello World!")


# hello()

###################################################################################################

# # Membuat function menghitung detik dari umur

# def user_age_in_seconds():
#   user_age = int(input("Enter your age: "))
#   age_seconds = user_age * 365 * 24 * 60 * 60
#   print(f"Your age in seconds is {age_seconds}.")


# print("Welcome to the age in seconds program!")
# user_age_in_seconds()

# print("Goodbye!")


###################################################################################################

# # Jangan membuat function dengan nama function bawaan python
# # misal
# def print(): 
#   print("Hello!")

# # ini akan error, karena print tidak memiliki parameter/argument


###################################################################################################

# # Perhatikan dalam melakukan shadowing variabel. ingat variabel global, dan perhatikan scopenya
# friends = ["Rolf", "Bob"]

# # # ini akan berhasil
# # friend_name = input("Enter your friend name: ")
# # friends = friends + [friend_name]
# # print(friends)

# # Menggunakan function
# def add_friend():
#   friend_name = input("Enter your friend name: ")
#   # friends = friends + [friend_name] # ini akan error karna mencoba mencoba membuat, mengakses dan merubah variabel global didalam scope function. dengan kata lain karna variabel dengan nama yang sama
#   f = friends + [friend_name] # ini akan berhasil
#   print(f)

# add_friend()

###################################################################################################

# # Function tidak bisa digunakan sebelum didefinisikan
# # seperti berikut akan menghasilkan error
# say_hello()

# def say_hello():
#   print("Hello!")

###################################################################################################
# kita dapat mengakses variabel global didalam scope function terlebih dahulu sebelum didefinisikan, tapi kita harus membuat variabel tersebut sebelum function dipanggil

def add_friends():
  friends.append("Rolf")

friends = []

add_friends()
add_friends()
add_friends()

print(friends)