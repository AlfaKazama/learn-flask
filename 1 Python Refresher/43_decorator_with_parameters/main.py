# Kita akan menamahbahkan parameter untuk decorator sendiri
# kita akan membuat function yang akan meretrun decorator, ini akan memungkinkan kita untuk memriksa access level

import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):
  def decorator(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
      if user["access_level"] == access_level:
        return func(*args, **kwargs)
      else:
        return f"No {access_level} permission for {user["username"]}"
    
    return secure_function
  return decorator


# 2 fungsi ini decorated
@make_secure("admin")
def get_admin_password():
  return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
  return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())

print(len("Halo Dunia"))
