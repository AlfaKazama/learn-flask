dicti = {
  "user": {
    "name": "alfa",
    "class": "PSIK 2020B",
    "age": 20
    }
  }

user = dicti["user"]

user |= {"age": 25}

print(user)
print(dicti)


if "alfa" not in user:
  print("berhasil")