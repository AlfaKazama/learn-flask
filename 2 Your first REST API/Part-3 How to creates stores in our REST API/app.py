from flask import Flask, request

app = Flask(__name__)

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

@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
  return {"stores": stores}

## membuat end point untuk menangani POST request
@app.post("/store")
def create_store():
  
  # request.get_json() ini dari flask dan kita mengimportnya
  # reques_data ini akan menyimpan data json dari body
  reques_data = request.get_json()
  news_store = {"name": reques_data["name"], "items": []}
  stores.append(news_store)
  
  # kita mengembalikan new_store dan status code, status default adalah 200, yang berarti semua ok berjalan dengan baik 
  # tapi disini kita menggunakan "201" yang berarti "saya sudah menerimanya(receive) datanya dan saya akan create store"
  return news_store, 201