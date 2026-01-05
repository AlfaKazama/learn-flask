import uuid
from flask import Flask, request, abort
# from flask_smorest import abort
from db import items, stores


app = Flask(__name__)

#####

@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
  return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
  store_data = request.get_json()
  if "name" not in store_data:
    abort(
      400,
      description="Bad request. Ensure 'name' is included in the JSON payload."
    )
  for store in stores.values():
    if store_data["name"] == store["name"]:
      abort(400, description="Store already exists.")
  store_id = uuid.uuid4().hex #fad4adadsad5as5dsad -> akan menjadi long string yang uniq
  store = {**store_data, "id": store_id}
  stores[store_id] = store

  return store, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
  try:
    return stores[store_id]
  except KeyError:
    return abort(404, description="Store not found.")


@app.get("/item")
def get_all_items():
  return {"items": list(items.values())}


@app.post("/item")
def create_item():
  item_data = request.get_json()
  # Here not ony we need to validate data exist,
  # BUl also what type of data. Pirce should be a float,
  # for example
  if(
    "price" not in item_data
    or "store_id" not in item_data
    or "name" not in item_data
  ):
    abort(400, description="Bad request. Ensure 'price', 'store_id', 'name' are included in the JSON payload.")
  for item in items.values():
    if(
      item_data["name"] == item["name"]
      and item_data["store_id"] == item["store_id"]
    ):
      abort(400, description="Item already exist.")

  if item_data["store_id"] not in stores:
    return abort(404, description="Store not found.")
  
  item_id = uuid.uuid4().hex
  item = {**item_data, "id": item_id}
  items[item_id] = item
  
  return item, 201


@app.get("/item/<string:item_id>")
def get_item(item_id):
  try:
    return items[item_id]
  except KeyError:
    return abort(404, description="Item not found.")

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
  try:
    del items[item_id] # mendelete dictionary
    return {"message": "Item deleted."}
  except KeyError:
    abort(404, description="Item not found")

@app.put("/item/<string:item_id>")
def update_item(item_id):
  item_data = request.get_json()
  if "price" not in item_data or "name" not in item_data:
    abort(400, description="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")
  # if "store_id" in item_data:
  #   for store in stores.values():
  #     if item_data["store_id"] not in stores:
  #       abort(400, description="Store id not found")
  try:
    item = items[item_id] # perubahan pada item, juga akan mempengharui items. karna dictionary itu mutable
    item |= item_data # menggabungkan dua dictionary
    return item
  except KeyError:
    abort(404, description="Item not found")
