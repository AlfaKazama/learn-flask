from flask.views import MethodView
from flask_smorest import abort, Blueprint

from flask_jwt_extended import jwt_required ## kita perlu mengimport ini

from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema # mengimport schema

blp = Blueprint("items", __name__, description="Operations on items")



@blp.route("/item/<int:item_id>")
class Item(MethodView):
  # kita juga melakukan requiring jwt
  @jwt_required()
  @blp.response(200, ItemSchema)
  def get(self, item_id):
    item = ItemModel.query.get_or_404(item_id)
    return item
  
  # kita juga melakukan requiring jwt
  @jwt_required()
  def delete(self, item_id): 
    item = ItemModel.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Item deleted."}

  # kita juga melakukan requiring jwt
  @jwt_required()
  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    item = ItemModel.query.get(item_id)
    if item:
      item.price = item_data["price"]
      item.name = item_data["name"]
    
    else:
      item = ItemModel(id=item_id, **item_data)
  
    db.session.add(item)
    db.session.commit()

    return item

@blp.route("/item")
class itemList(MethodView):

  # kita juga melakukan requiring jwt
  @jwt_required()
  @blp.response(200, ItemSchema(many=True))
  def get(self):
      return ItemModel.query.all()
  

  ## Jika user tidak login dan tidak mengirimkan (send) acces token kepada kita, mereka tidak akan dapat membuat item baru
  # jadi kita tidak dapat call endpoint kecuali kita send JWT
  # jika kita create item maka akan error, Yang kita harus lakukan adalah mengiri bearer token (token pembawa), kita tidak menaruhnya di JSON body, kita menambahkannya di header
  @jwt_required()
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