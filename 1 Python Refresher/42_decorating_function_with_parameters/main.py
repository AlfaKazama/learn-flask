import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
  @functools.wraps(func)
  def secure_function(panel):
    if user["access_level"] == "admin":
      return func(panel)
    else:
      return f"No admin permission for {user["username"]}"
  
  return secure_function

@make_secure
def get_password(panel):
  if panel == "admin":
    return "1234"
  elif panel == "billing":
    return "super_secure_passworrd"


# ketika kita memanggil function ini, kita harus passing argument untuk panel, tetapi function get_password sebenarnya tidak akan menerima argument tersebut, kita perlu menambahkan parameter panel pada secure_function 
print(get_password("billing"))



#################################################################################################################
# # Namun cara diatas bukanlah cara yang baik, karena kita telah memasangkan decorator pada make_secure ke function get_password
# # itu berarti kita tidak dapat menggunakannya ke function lain yang menerima argument yang berbeda
# # perhatikan pada secure_function kita menggunakan *args, **kwargs. ini membuat secure_function tidak peduli argument apa yang dimasukkan

# import functools

# user = {"username": "jose", "access_level": "admin"}


# def make_secure(func):
#   @functools.wraps(func)
#   def secure_function(*args, **kwargs):
#     if user["access_level"] == "admin":
#       return func(*args, **kwargs)
#     else:
#       return f"No admin permission for {user["username"]}"
  
#   return secure_function

# @make_secure
# def get_password(panel):
#   if panel == "admin":
#     return "1234"
#   elif panel == "billing":
#     return "super_secure_passworrd"


# # ketika kita memanggil function ini, kita harus passing argument untuk panel, tetapi function get_password sebenarnya tidak akan menerima argument tersebut, kita perlu menambahkan parameter panel pada secure_function 
# print(get_password("billing"))
