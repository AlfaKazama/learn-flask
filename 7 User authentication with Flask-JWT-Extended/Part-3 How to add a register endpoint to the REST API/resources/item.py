import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema # mengimport schema

blp = Blueprint("items", __name__, description="Operations on items")



@blp.route("/item/<int:item_id>")
class Item(MethodView):
  @blp.response(200, ItemSchema)
  def get(self, item_id):
    item = ItemModel.query.get_or_404(item_id)
    return item
  
  # Mendelete model dari database
  def delete(self, item_id): 
    item = ItemModel.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Item deleted."}

  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    # disini kita mengmabil item
    item = ItemModel.query.get(item_id)
    # dan ini adalah cara kita memperbaharui item, jika item tersebut ada kita hanya perlu passing price dan name saja
    # item akan di update sesuai perubahan, dan tidak akan membuat item baru
    if item:
      item.price = item_data["price"]
      item.name = item_data["name"]
    
    # dan item tidak ada, maka kita kan membuat item baru, id diambil dari url, dan field lain diambil dari json body(**item_data)
    else:
      item = ItemModel(id=item_id, **item_data)

    """
    proses if diatas sebenarnya kurang bagus, lebih bagus seperti ini =>

    if item:
    if "name" in item_data:
        item.name = item_data["name"]
    if "price" in item_data:
        item.price = item_data["price"]
    if "store_id" in item_data:
        item.store_id = item_data["store_id"]
    
    """
  
    db.session.add(item)
    db.session.commit()

    return item

@blp.route("/item")
class itemList(MethodView):

  # retrieve list model kita kita akan menggunakan query all
  @blp.response(200, ItemSchema(many=True))
  def get(self):
      return ItemModel.query.all()
  
  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    item = ItemModel(**item_data)
    try:
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred inserting the item.")

    return item