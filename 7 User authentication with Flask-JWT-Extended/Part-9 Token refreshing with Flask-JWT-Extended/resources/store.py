import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

# Kita juga akan membuat decorator response seperti pada item.py
# kita tidak perlu decorate pada delete, karna delete hanya mengembalikan pesan saja.

@blp.route("/store/<int:store_id>")
class Store(MethodView):
  @jwt_required()
  @blp.response(200, StoreSchema)
  def get(self, store_id):
    # kita melakukan hal yang mirip seperti pada itemm
    store = StoreModel.query.get_or_404(store_id)
    return store

  ## Mendelete model dari database
  @jwt_required()
  def delete(self, store_id):
    # store = StoreModel.query.get_or_404(store_id)
    # db.session.delete(store)
    # db.session.commit()
    # return {"message": "Store deleted."}
  
    store = StoreModel.query.get_or_404(store_id)
    db.session.delete(store)
    db.session.commit()
    return {"message": "Store deleted"}, 200

@blp.route("/store")
class StoreList(MethodView):

  ## kita melakukan hal yang sama seperti pada item
  @jwt_required()
  @blp.response(200, StoreSchema(many=True))
  def get(self):
    return StoreModel.query.all()

  # Menambahkan schema
  @jwt_required()
  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
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

