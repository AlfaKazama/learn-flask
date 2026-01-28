from flask.views import MethodView
from flask_smorest import Blueprint, abort

# ini akan menghash password yang dikirim user/client menjadi tumpukan karakter dan angka yang tidak dapat dibaca dan kemudian kita akan menyimpannya kedalam database
# dan ketika user ingin login kembali, akan membandingkan password yang masuk tadi dari user dengan yang sudah kita simpan pada database, dan memastikannya cocok
from passlib.hash import pbkdf2_sha256 


# acces token adalah kombinasi angka dan karakter yang akan kita generate di server, kita akan mengirimkannya ke client
# dan satu satu nya cara mendapatkan  access token ini adalah dengan memberikan user dan password yang benar (login denan benar)
# jadi jika login berahasil (client mengirimkan username dan password yang benar) maka kita akan mengirimkan mereka access token
# client akan menyimpan access token tersebut, dan pada setiap request client akan mengirimkan nya kembali kepada kita (server)
from flask_jwt_extended import create_access_token

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
  

## end point login agar mendapatkan acces token
@blp.route("/login")
class UserLogin(MethodView):
  @blp.arguments(UserSchema)
  def post(self, user_data):
    # Pengecekan apakan username benar (ada)
    user = UserModel.query.filter(
      UserModel.username == user_data["username"]
    ).first()

    # Lalu pengecekan password benar atau tidak, ini akan memerika apaka kedua sandi hash cocok
    if user and pbkdf2_sha256.verify(user_data["password"], user.password):
        # jika valid maka:
        access_token = create_access_token(identity=user.id)
        # Perhatikan, pada "identity=user.id" ini berarti kita menyimpan user id dalam jwt
        # jwt yang diterima client adalah jwt yang berisi user id yang telah login.
        # jadi siapaun yang memiliki jwt response tersebut dapat mengirimkannya kembali kepada kita

        """
          Jadi misalnya katakanlah kita memiliki end point buy, dan end point itu mengambil jwt, dan kemudia membeli item menggunakan user id, jadi dapat membuat user dengan id tersebut dapat membeli barang tersebut. ID yang disimpan dalam jwt adalah yang akan membeli item yang dimaksud.

          Jadi penting bahwa JWT itu harus bersifat private dan aman, itu tidak dibagikan kepada siapapun. Karena memiliki jwt berarti user telah login dan oleh karena itu siapun yang berpura pura memiliki JWT dapat berpura pura menjadi pengguna yang telah login

          Ketika kita receive (menerima) JWT, kita tahu siapa pemilit JWT tersebut. Ini penting karena memungkinkan kita untuk melakukan tindakan yang berbeda untuk user yang berbeda (different actions for different users)
        """

        return {"access_token": access_token}
    
    # jika salah username dan password maka
    abort(401, message="Invalid credentials.")



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