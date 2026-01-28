import os
import secrets

from flask import Flask
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
  
  ## Membuat instance dari JWTManager, kita juga perlu menerapkan secret key
  # secret key digunakan untuk signing JWT (menandatangani jwt), ini berfungsi untuk memastikan user tidak membaut JWT mereka sendiri di tempat lain. Ini mencegah gangguan pada JWT
  # Jadi ini penrting karena JWT akan menyimpan beberapa informasi, dan kita tidak ingin user dapat mengubah informasi tersebut lalu mengirimkan nya kembali kepada kita, berpura pura seperti kitalah yang menciptakan JWT
  # Penting bahwa secret key yang aman itu dengan membuat random secret ke yang panjang dan aman. Kita dapat menggunakan semacam secret generation software. di python kita dapat mengimport secret module. Pada contoh dibawah kita menggunakan length 128 bit pada secrest key. 
  
  # app.confit["JWT_SECRET_KEY"] = "alfa"
  # Namun kita tidak ingin mengubah secret key setiap kali kita merestrat/run app, yang ingin kita lakukaan adalah generate value, salin itu, dan kita gunakan sebagai secret key.
  # app.confit["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)  

  # jadi kita akan generete kode lewat console python dan menggunakannnya. 
  # namun secret key juga normalnya tidak disimpan didalam code, biasanya akan disimpan pada environtment variable. Kita akan membahasnya nanti, namun untuk saat ini kita akan menggunakannya pada code.
  # app.confit["JWT_SECRET_KEY"] = "56020317158279505731000734988698429450"


  # Namun kita akan menggunakan key yang mudah terlebih dahulu
  app.config["JWT_SECRET_KEY"] = "alfa"
  jwt = JWTManager(app)



  with app.app_context():
    db.create_all()

  # kita akan menggunakan blueprint
  api.register_blueprint(ItemBlueprint)
  api.register_blueprint(StoreBlueprint)
  api.register_blueprint(TagBluePrint)
  api.register_blueprint(UserBluePrint)

  return app
