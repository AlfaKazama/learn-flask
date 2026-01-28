import os
import secrets

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
# import models # disinilah __ini__.py pada models jadi berguna, karena kia bisa import langsung seperti ini


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBluePrint
from resources.user import blp as UserBluePrint

def create_app(db_url=None):
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Storest REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

  app.config["SQLALCHEMY_DATABASE_URI"] = (
    db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
  )
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
  db.init_app(app)

  api = Api(app)
  
  app.config["JWT_SECRET_KEY"] = "alfa"
  jwt = JWTManager(app)

  ## jwt claims, kita dapat menambahkan informasi tambahan / extra infomration ke JWT selain "subject" yang berarti user id. Maksudnya informasi tambahan ini dapat berupa apapun yang kita inginkan

  # dan ini adalah function yang berjalan setiap kali kita membuat access token jwt
  # parameter identity sama halnya dengan paramere pada code ini => access_token = create_access_token(identity=str(user.id))
  @jwt.additional_claims_loader
  def add_claims_to_jwt(identity):
    # ini sekedar contoh aja, indetity bukan cara cek terbaik siapaa yang harus menjadi admin atau tidak tapi cara yang terbaik adalah melihat ke dalam database apakah pengguna adalah admin sebelum menyimpan infromasi di JWT
    if int(identity) == 1:
      return {"is_admin": True}
    return {"is_admin": False}


  ## Kita melakukan beberapa configuration, Kita menambakan 3 functions dibawah jtw manager
  # harus return berupa JSON dan code status, tidak bisa dictionary. Jadi kita harus mengimport jsonify dari flask

  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
    # ini akan dikembalikan saat jwt telah expired / kadaluarsa namun tetap dicoba oleh client
    return (
      jsonify({"message": "The token has expired.", "error": "token_expired"}), 401,
    )
  
  @jwt.invalid_token_loader
  def invalid_token_callback(error):
    # token idak valid, atau karena user mencoba mengubahnya
    return(
      jsonify(
        {"message": "Signature verification failed.", "error": "invalid_token"}
      ), 401,
    )
  
  @jwt.unauthorized_loader
  def missing_token_callback(error):
    # token missing 
    return (
      jsonify(
        {
          "description": "Request does not contain an access token.",
          "error": "authorization_required",
        }
      ),
      401,
    )



  with app.app_context():
    db.create_all()

  # kita akan menggunakan blueprint
  api.register_blueprint(ItemBlueprint)
  api.register_blueprint(StoreBlueprint)
  api.register_blueprint(TagBluePrint)
  api.register_blueprint(UserBluePrint)

  return app
