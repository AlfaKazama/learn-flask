from flask import Flask
from flask_smorest import Api

import os
from db import db
import models # disinilah __ini__.py pada models jadi berguna, karena kia bisa import langsung seperti ini


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


# kita selalu membuat flask app di app.py, tapi lebih baik mendefinisikan function yang membuat, menyiapkan dan mengonfigurasi flask app, kita akan membuat function sehingga kita dapat memanggil saat function ini dibutuhkan. Dan ini termasuk ketika kita ingin menulis test (pengujian) untuk flask app kita.
# kita akan memanggil function ini untuk mendapatkan new flask app, jadi kita tidak perlu run app.py untuk mendapatkan new flask app
# penamaan functionnya terserah

# parameter "db_url=" utuk meneruskan URL databse yang ingin kita hubungkan
def create_app(db_url=None):
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Storest REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

  # menggunakan flask SQLAlchemy dan mendefinisikan dan menambahkannya ke flask app
  # valuenya adalah conncetion string ke database, semua penyedia database seperti MySQL, PostgresSQL, SQLite atau apapun. dan memiliki infromasi yang diperlukan agar client terhubung(connected) ke database,dalam kasus ini flask app adalah client. 
  # jadi stringnya berisi semua informasi yang datavase perlukan untuk melakukan connection. itu termasuk username, the database password, tempat database disimpan (database hosted) dan beberapa informasi lainnnya. 
  # kita dapat menggunakan SQLite
  # app.config["SQLALCHEMY_DATABASE_URI"] = "//sqlite:///data.db" # ini akan membuat file benama data.db dan akan menyimpan data kita disana

  # jika "db_url" ada maka akan digunakan, namun jika tidak ada maka :
  # akan mencoba mengakses DATABASE_URL environment variable, jika ada akan digunakan, jika tidak ada maka akan menggunakan SQLite variable secara default
  app.config["SQLALCHEMY_DATABASE_URI"] = db_url or  os.getenv("DATABASE_URL", "//sqlite:///data.db")
  app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False # fungsi nya cari sendiri diinternet, ga harus tau fungsinya
  
  # Menginisialisasi estensi FLask SQLAlchemy ektension, memberikan flask "app" sehingga dapat menghubungkan flask app ke SQLAlchemy
  db.init_app(app)

  api = Api(app)

  # setiap kali kita memulai the "app" dan membuat request menggunakan insomnia, ssebelum first request ditangani kita perlu menjalankan kode ini
  # ini akan membuat semua table di database kita, jika table suda ada, maka table tersebut tidak akan dibuat 
  # jadi ini akan berjalan jika tablenya belum ada
  # ingat bahwa SQLAlchemy tahu table mana yang harus dibuat, karena kita sudah mengimport model 
  with app.app_context():
    db.create_all()

  # kita akan menggunakan blueprint
  api.register_blueprint(ItemBlueprint)
  api.register_blueprint(StoreBlueprint)

  return app


## Ini masih error karena kita mencoba menghapus import pada item.py dan store.py, kita akan perbaiki di next materi