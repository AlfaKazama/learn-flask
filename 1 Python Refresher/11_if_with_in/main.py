movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
  print(f"I've watched {user_movie} too!")
else:
  print("I haven't watched that yet")

############################################################################################################

# ## import random
# ## number = random.randint(1, 10)


# ## Create a magic number App
# number = 7
# user_input = input("Enter 'y' if you would like to play: ").lower()

# # if user_input in ("y", "Y"): ## kita bisa melakukan ini, alih alih menggunakan lower() pada user_input
# if user_input == "y":
#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#     print("You guessed correctly!")
#   # elif number - user_number in (1, -1): # ada cara yang lebih baik dari ini yaitu menggunkan abs()
#   # abs akan memberikan nilai absolute, abs akan merubah -1 menjadi positif
#   elif abs(number - user_number) == 1:
#     print("You were off by one")
#   else:
#     print("Sorry, it's wrong!")