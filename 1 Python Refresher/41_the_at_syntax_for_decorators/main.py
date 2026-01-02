user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
  return "1234"

def make_secure(func):
  def secure_function():
    if user["access_level"] == "admin":
      return func()
    else:
      return f"No admin permission for {user["username"]}"
  
  return secure_function

# Dari pada melakukan ini, yang dapat menyebabkan error jika kita memanggil get_admin_password() sebelum line code ini kita dapat menggunakan syntax @
# @ akan melakukan hal yang sama persis
get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

#################################################################################################################
# # Menerapkan @, ini akan sama persis cara kerjanya tanpa kita harus mendefinisikan get_admin_password = make_secure(get_admin_password)

# user = {"username": "jose", "access_level": "guest"}


# def make_secure(func):
#   def secure_function():
#     if user["access_level"] == "admin":
#       return func()
#     else:
#       return f"No admin permission for {user["username"]}"
  
#   return secure_function

# @make_secure
# def get_admin_password():
#   return "1234"



# # print(get_admin_password())

# # namun ada masalah dalam penggunaan decorator @, ketika kita melakukan ini get_admin password akan menjadi secure_function
# # dampak dari ini get_admin_password tidak akan tercatat sebagai function internal
# # selain itu jika kita memiliki documentation pada function get_admin_password(), documentation itu akan terhapus
# print(get_admin_password.__name__)


#################################################################################################################

# # Untuk menghindari hal diatas, kita dapat menggunakan decorator lain, kita akan mengimport functools, modul bawaan python
# # kemudian kita akan decorate secure function kita 

# import functools

# user = {"username": "jose", "access_level": "guest"}


# def make_secure(func):
#   # kita akan memberitahu secure_function bawha dia adalah wrapper(pembungkus) dari func
#   # apa yang kita lakukan adalah menyimpan name dan documentation dari function get_admin_password() (jika ada)
#   @functools.wraps(func)
#   def secure_function():
#     if user["access_level"] == "admin":
#       return func()
#     else:
#       return f"No admin permission for {user["username"]}"
  
#   return secure_function

# @make_secure
# def get_admin_password():
#   return "1234"

# print(get_admin_password.__name__)

