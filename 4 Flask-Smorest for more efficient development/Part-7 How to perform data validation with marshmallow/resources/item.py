import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema # mengimport schema

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
  def get(self, item_id):
    try:
      return items[item_id]
    except KeyError:
      return abort(404, message="Item not found.")
  
  def delete(self, item_id):
    try:
      del items[item_id] # mendelete dictionary
      return {"message": "Item deleted."}
    except KeyError:
      abort(404, message="Item not found")

  # Kita juga melakukan hal yang sama pada put method seperti pada post method
  @blp.arguments(ItemUpdateSchema)
  def put(self, item_data, item_id):
    try:
      item = items[item_id] # perubahan pada item, juga akan mempengharui items. karna dictionary itu mutable
      item |= item_data # menggabungkan dua dictionary
      return item
    except KeyError:
      abort(404, message="Item not found")

@blp.route("/item")
class itemList(MethodView):
  def get(self):
    return {"items": list(items.values())}

  ## Menggunakan validasi dari schema
  # pada method post parameter second setelah self, parameter item_data akan berisi JSON, yang merupakan data field validasi yang diminta schema
  # Jadi JSON yang dikirim client di passing melalui ItemSchema, lalu akan mengecek field, dan tipe data field valid atau tidak. Dan akan memberikan method, argumen, yanng merupakan valid dictionary
  # Melakukan hal ini akan menambahkan beberapa informasi tentang apa yang di expected pada SWagger UI documentation
  @blp.arguments(ItemSchema)
  def post(self, item_data):
    for item in items.values():
      if(
        item_data["name"] == item["name"]
        and item_data["store_id"] == item["store_id"]
      ):
        abort(400, message="Item already exist.")

    if item_data["store_id"] not in stores:
      return abort(404, message="Store not found.")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    
    return item, 201