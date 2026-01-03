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

@app.post("/store")
def create_store():

  reques_data = request.get_json()
  news_store = {"name": reques_data["name"], "items": []}
  stores.append(news_store)

  return news_store, 201

## Bagaimana mengcodekan flask sehingga URL atau end point, bahwa client request dapat bersifat dinamis, sehingga ketika client mengirim POST, kita dapat mengambil bagian end point terakhir. Kita menganggap bagian end poit terakhir adalah store name yang diinginkan client

# name pada URL dinamis, akan di passing pada parameter "name" pada function create_item
# /item kita menggunakannya  dengan POST request untuk membuat item 
@app.post("/store/<string:name>/item")
def create_item(name):
  request_data = request.get_json()  # ambil JSON yang masuk
  for store in stores:
    if store["name"] == name:
      new_item = {"name": request_data["name"], "price": request_data["price"]}
      store["items"].append(new_item)
      return new_item, 201
  return {"message": "Store not found"}, 404