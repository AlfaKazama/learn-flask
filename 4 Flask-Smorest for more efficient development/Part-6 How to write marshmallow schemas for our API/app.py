from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

# Kita harus mendaftarkan Blueprints dengan API, beberapa opsi konfigurasi:
# propagate exceptions adalah konfiurasi flask yang menyatakan bahwa jika ada pengecualian yang tersembunyi didalam ekstensi flask, untuk disebarkan main app, sehingga kita dapat melihatnya.
app.config["PROPAGATE_EXCEPTIONS"] = True
# app title adalah judul yang akan ada di dokumentasi kita dari, dan api version merupakan versi API yang kita kerjakan
app.config["API_TITLE"] = "Storest REST API"
app.config["API_VERSION"] = "v1"
# openapi adalah standar yang digunakan untuk dokumentasi API dan kita memberitahu flask-smorest untuk menggunakan versi 3.0.3
app.config["OPENAPI_VERSION"] = "3.0.3"
# openapi url prefix hanya memberi tahu flask-smorest dimana "root" API berada, kita menggunakan "/" karena awalnya dimulai dari itu
app.config["OPENAPI_URL_PREFIX"] = "/"
# dan akhirnya beberapa konfigurasi dokumentasi-> swagger-ui path ,dan swager-ui-url. ini membebri tahu flask-smorest untuk menggunakan swagger pada dokumentasi yang ada di swagger-ui. Namun ia perlu membuat kode swagger dari suatu tempat, sehingga dapat menampilkan dokumentasi dan pada url tersebutlah code itu berada
# buka swagger: http://127.0.0.1:5000/swagger-ui
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Kita harus mengimport API pada app yang berasal dari flask-smorest
# ini akan menghubungkan ekstensi flask-smorest pada flask app
api = Api(app)

# kita akan menggunakan blueprint
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)