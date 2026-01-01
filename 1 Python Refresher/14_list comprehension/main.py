## Membuat list baru dengan element yang dikalikan dua
numbers = [1, 3, 5]

# # dengan menggunakan for 
# double = []
# for num in numbers:
#   double.append(num * 2)

# Menggunakan list comprehension
double = [x * 2 for x in numbers]

print(double)

#############################################################################################################################################

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# # # Membuat list teman yang nama awalnya huruf s
# # start_s = []

# # for friend in friends:
# #   if friend.startswith("S"):
# #     start_s.append(friend)

# # print(start_s)

# # Menggunakan list comprehension
# start_s = [friend for friend in friends if friend.startswith("S")]
# print(start_s)

# # Note: ketika kita mengggunakan list comprehension, sebuah list baru akan dibuat. yang artinya akan terdapat list baru dengan alamat nya dalam memori

# friends = ["Sam", "Samantha", "Saurabh"]
# print(friends)
# print(start_s)
# print(friends is start_s) # false karena list disimpan pada alamat memori yang berbeda
# # kamu bisa mengecek id dari kedua list tersebut
# print("friends: ", id(friends), "start_s: ", id(start_s)) # perhatikan nilai id nya berbeda

# # cara membuat id yang sama adalah seperti berikut:
# start_s = friends
# print("friends: ", id(friends), "start_s: ", id(start_s)) # id akan sama, karna ini menyalin list
#############################################################################################################################################