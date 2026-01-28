from flask.views import MethodView
from flask_smorest import Blueprint, abort

# ini akan menghash password yang dikirim user/client menjadi tumpukan karakter dan angka yang tidak dapat dibaca dan kemudian kita akan menyimpannya kedalam database
# dan ketika user ingin login kembali, akan membandingkan password yang masuk tadi dari user dengan yang sudah kita simpan pada database, dan memastikannya cocok
from passlib.hash import pbkdf2_sha256 

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users")

## end point register
@blp.route("/register")
class UserRegister(MethodView):
  @blp.arguments(UserSchema)
  def post(self, user_data):
    # kita perlu mengecek apakah username unique atau tidak
    # Di sini kita bisa melewatkan langkah ini dan nantinya akan menemui kesalahan IntegrityError saat menyisipkan data ke dalam database. Itu mungkin akan menjadi solusi yang lebih ringkas.
    if UserModel.query.filter(UserModel.username == user_data["username"]).first():
      abort(409, message="A user with that username already exists.")

    user = UserModel(
      username=user_data["username"],
      # kita ingin melakukan hash. mengkonversinya terlebih dahulu sebelum memasukkannya ke dalam databse
      password=pbkdf2_sha256.hash(user_data["password"])
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User created successfully."}, 201
  

## Endpoint get dan delete user
@blp.route("/user/<int:user_id>")
class User(MethodView):
  @blp.response(200, UserSchema)
  def get(self, user_id):
    user = UserModel.query.get_or_404(user_id)
    return user
  
  def delete(self, user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted"}, 200