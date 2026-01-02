# Decorator memungkinkan kita memodifikasi function dengan sangat mudah
# Mengamnakan function get_admin_password() dari user guest

user = {"username": "jose", "access_levels": "guest"}

def get_admin_password():
  return "1234"


if user["access_levels"] == "admin":
  print(get_admin_password())

# Tapi dengan kondisi if diatas get_admin_password() masih tetap tidak aman
get_admin_password()

#################################################################################################################

# # Jadi code diatas, bukanlah solusi, yang harus kita lakukan ialah kita dapat mendefinisikan secure function

# user = {"username": "jose", "access_levels": "guest"}

# def get_admin_password():
#   return "1234"

# def secure_get_admin():
#   if user["access_levels"] == "admin":
#     return 1234

# print(secure_get_admin())
# # print(get_admin_password()) # ini memang akan tetap bisa mengakses

#################################################################################################################

# # pada code diatas, kita membuat if function pada secure_get_admin() namun kita tidak akan melakukan itu jika kita menggunakan decorator

# user = {"username": "jose", "access_levels": "admin"}

# def get_admin_password():
#   return "1234"

# def secure_function(func):
#   if user["access_levels"] == "admin":
#     return func

# get_admin_password = secure_function(get_admin_password)

# print(get_admin_password())

#################################################################################################################

# # jadi code diatas ini adalah langkah yang dekat menuju apa yang kita inginkan, sayangnya kita mengharuskan user menjadi admin sebelum kita mengamankan function kita
# # idealnya kita ingin sesuatu yang mengecek tingkat akses pengguna saat kita memamnggil function tersebut
# # kita akan merombak function

# user = {"username": "jose", "access_levels": "guest"}

# def get_admin_password():
#   return "1234"

# # Jadi inilah dekorator
# def make_secure(func):
#   # function secure_function, tidak mengambil parameter apapun, hanya digunakan untuk mengecek dan kemudian memanggil "func"
#   def secure_function():
#     if user["access_levels"] == "admin":
#       return func()
#     else:
#       return f"No admin permission for {user["username"]}"
  
#   return secure_function

# get_admin_password = make_secure(get_admin_password)


# # Menerapkan dekorator kita membuat function get_admin_password() tidak bisa diakses kecuali dengan akses admin
# print(get_admin_password())
