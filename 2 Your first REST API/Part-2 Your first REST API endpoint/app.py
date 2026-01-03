from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def home():
#   return "Hello, Flask!"


## saat ini kita akan menyimpan data pada list
stores = [
  {
    "name": "My Store",
    "items": [
      {
        "name": "Chair",
        "price": "15.99",
      }
    ]
  },
]

# kita dapat membuat end point pertama kita yang akan return data store saat client request (memintanya)
# ini bisa desebut first end point, atau first route
# kita akan mengakses alamat flass app disertai endpoint /store 
# API ini akan mengembalikan JSON stores
@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
  return {"stores": stores}