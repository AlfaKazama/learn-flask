import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

# Kita juga akan membuat decorator response seperti pada item.py
# kita tidak perlu decorate pada delete, karna delete hanya mengembalikan pesan saja.

@blp.route("/store/<string:store_id>")
class Store(MethodView):
  @blp.response(200, StoreSchema)
  def get(self, store_id):
    raise NotImplementedError("Listing items is not implemented.")

  def delete(self, store_id):
    raise NotImplementedError("Listing items is not implemented.")

@blp.route("/store")
class StoreList(MethodView):
  @blp.response(200, StoreSchema(many=True))
  def get(self):
    raise NotImplementedError("Listing items is not implemented.")

  # Menambahkan schema
  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
    # kita melakukan hal yang sama seperti pada item
    # tapi ada sedikit perbedaan
    store = StoreModel(**store_data)
    try:
      db.session.add(store)
      db.session.commit()
    except IntegrityError:
      abort(
        400,
        message="A store with that name already exists."
      )
    except SQLAlchemyError:
      abort(500, message="An error ouccurred creating store")
    
    return store

