import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

# Kita juga akan membuat decorator response seperti pada item.py
# kita tidak perlu decorate pada delete, karna delete hanya mengembalikan pesan saja.

@blp.route("/store/<string:store_id>")
class Store(MethodView):
  @blp.response(200, StoreSchema)
  def get(self, store_id):
    try:
      return stores[store_id]
    except KeyError:
      return abort(404, message="Store not found.")

  def delete(self, store_id):
    try:
      del stores[store_id] # mendelete dictionary
      return {"message": "Store deleted."}
    except KeyError:
      abort(404, message="Store not found")

@blp.route("/store")
class StoreList(MethodView):
  @blp.response(200, StoreSchema(many=True))
  def get(self):
    return stores.values()

  # Menambahkan schema
  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
    for store in stores.values():
      if store_data["name"] == store["name"]:
        abort(400, message="Store already exists.")
    store_id = uuid.uuid4().hex #fad4adadsad5as5dsad -> akan menjadi long string yang uniq
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store, 201

