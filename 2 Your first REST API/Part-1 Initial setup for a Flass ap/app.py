from flask import Flask

# ini akan mencipakan flask app dan melakukan banyak hal untuk kita
# kita mendifisikan endpoint apapun di "app" ini, yang akan menerima data(accept data) dan return response
# menjalankan "app" akan membuat end point tersedia untuk client
# menjalankan "app" selalu menjadi hal yang kita ingin lakukan untuk menggunakan flask
# kita akan menuliskan "flask" run pada terminal. memastikan bahwa terminal memiliki  virutal environtment yang aktif dan memastikan kita berada pada folder yang bersi "app.py"
app = Flask(__name__)


# Kalau @app.route() tidak ada, maka Flask tidak bisa memastikan app kamu valid untuk dijalankan.
@app.route("/")
def home():
  return "Hello, Flask!"

print("Hello")