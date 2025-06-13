# # WHILE Loop
# number = 7

# while True:
#   user_input = input("Would you like to play? (Y/n): ").lower()

#   if user_input == "n":
#     break

#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#     print("You guessed correctly!")
#   elif abs(number - user_number) == 1:
#     print("You were off by one")
#   else:
#     print("Sorry, it's wrong!")


################################################################################################################

# ## FOR Loop
# friends = ["Rolf", "Jen", "Bob", "Anne"]

# # # Jika kita ingin mencetak semua element secara manual maka akan seperti ini
# # print(f"{friends[0]} is my friend.")
# # print(f"{friends[1]} is my friend.")
# # print(f"{friends[2]} is my friend.")
# # print(f"{friends[3]} is my friend.")

# # Namun cara diatas akan semakin rumit jika element pada listnya terlalu banyak, maka digunakanlah For Loop
# for friend in friends:
#   print(f"{friend} is my friend")

# # Jika kamu ingin mengulang sebanyak yang ingin kamu ulang, gunakan range
# for friend in range(4):
#   print(f"{friends[friend]} is my friend")

################################################################################################################

## Menggunakan FOR loop untuk menghitung rata rata
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

# for grade in grades:
#   total += grade

# atau alih alih menggunakan for loop, kita bisa mengggunakan sum()
total = sum(grades)

print(total / amount)