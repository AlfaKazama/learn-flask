import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema # mengimport schema

blp = Blueprint("items", __name__, description="Operations on items")


# Kita akan mendecorate flask-smorest responses dengan marshmallow schema, sehingga kita dapat meneruskan data yang kita return ke schema, dan melakukan hal hal seperti filtering field, casting dan lain sebagainya.
# kita akan menentukan apa yang akan direturn untuk setiap status code, dan ini juga akan mengisi dokumentasi

@blp.route("/item/<string:item_id>")
class Item(MethodView):
  # ini adalah rensponse sukses, code statusnya adalah 200, dan akan meneruskan apa yang di return ke Schema
  @blp.response(200, ItemSchema)
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

  # kita juga menentukan response, dalam menempatkan decorator renspons, pastikan untuk menempatkannya lebih dalam didalam dibanding decorator dengan satu arguments 
  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    try:
      item = items[item_id] # perubahan pada item, juga akan mempengharui items. karna dictionary itu mutable
      item |= item_data # menggabungkan dua dictionary
      return item
    except KeyError:
      abort(404, message="Item not found")

@blp.route("/item")
class itemList(MethodView):
  # Pakai ItemSchema, tapi dengan many=True (artinya bentuknya list/kumpulan item, bukan 1 objek tunggal)
  @blp.response(200, ItemSchema(many=True))
  def get(self):
    # Method ini sebelumnya akan mengembalikan list, kita akan mengubahnya menjadi seperti ini. 
    return items.values() 
  
  # Kita juga menambahkan decorator response
  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
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