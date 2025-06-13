# # IF statement

# day_of_week = input("What day of the week is it today? ")

# # print(day_of_week == "Monday")

# if day_of_week == "Monday":
#   print("Have a great start to your week!")

# if day_of_week != "Monday":
#   print("Full speed ahead!")


# # Ini akan selalu dicetak, karena print() ini berada diluar identasi dari if statement
# print("This always runs.")

####################################################################################################################

## Using elif, and else syntax

day_of_week = input("What day of the week is it today? ").lower()

# print(day_of_week == "Monday")

if day_of_week == "monday":
  print("Have a great start to your week!")
elif day_of_week == "tuesday":
  print("It's Tuesday.")
else:
  print("Full speed ahead!")

print("This always runs.")
