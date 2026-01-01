# ## Penggunaaan parameter dan arguments pada functions

# # def add(x, y):
# #   pass # pass berati didalam function tidak terjadi apa apa, atau kosong

# # (x, y) adalah parameter, and (5, 3) adalah argument
# def add(x, y):
#   result = x + y
#   print(result)

# add(5, 3)

#############################################################################################################

## Kita tidak bisa mengirimkan (passing) argument ke pada funtion yang tidak memiliki parameter
# def say_hello():
#   print("Hello!")

# say_hello("Bob") # ini akan error, karna kita mencoa passing argument 


#############################################################################################################

# ## Penggunaan parameter dan argument
# def say_hello(name):
#   print(f"Hello, {name}")

# say_hello("Bob")
# # say_hello() # ini akan error karna kita tidak memamsukkan argument


#############################################################################################################

# ## Posisi argument mempengaruhi nilai
# def say_hello(name, surname):
#   print(f"Hello, {name} {surname}")

# say_hello("Bob", "Smith")
# ## kita bisa menggunakan keywor/name argument agar kita tidak peduli dengan posisi argument
# say_hello(surname="Bob", name="Smith")


#############################################################################################################
# position argument harus ditempatkan terlebih dahulu dibanding keyword argument

def divide(dividend, divisor):
  if divisor != 0:
    print(dividend / divisor)
  else:
    print("You fool!")

# divide(dividend=15, 0) # akan error, karnea position argument harus ditempatkan terlebih dahulu 
divide(15, divisor=5)