import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stores


## Blue print pada flask-smorest digunakan untuk membagi API menjadi beberapa segmen 
blp = Blueprint("stores", __name__, description="Operations on stores")

## Method view digunakan untuk membuat class yang methodnya route to spesific endpoints
# ini akan menghubungkan flask-smorest dengan flask mehtodview, sehingga kita dapat membuat get request mengarah ke endpoint "/store/<string:store_id>" begitu juga pada delete request.
@blp.route("/store/<string:store_id>")
class Store(MethodView):
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

##  Kita akan membuat method view yang yang lainnya karena endpoint dan routenya berbeda
@blp.route("/store")
class StoreList(MethodView):
  def get(self):
    return {"stores": list(stores.values())}

  def post(self):
    store_data = request.get_json()
    if "name" not in store_data:
      abort(
        400,
        message="Bad request. Ensure 'name' is included in the JSON payload."
      )
    for store in stores.values():
      if store_data["name"] == store["name"]:
        abort(400, message="Store already exists.")
    store_id = uuid.uuid4().hex #fad4adadsad5as5dsad -> akan menjadi long string yang uniq
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store, 201

