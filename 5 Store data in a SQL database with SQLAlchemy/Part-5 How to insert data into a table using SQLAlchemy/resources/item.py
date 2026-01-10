import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema # mengimport schema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
  @blp.response(200, ItemSchema)
  def get(self, item_id):
    raise NotImplementedError("Listing items is not implemented.")
  
  def delete(self, item_id):
    raise NotImplementedError("Listing items is not implemented.")

  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    raise NotImplementedError("Listing items is not implemented.")

@blp.route("/item")
class itemList(MethodView):
  @blp.response(200, ItemSchema(many=True))
  def get(self):
      raise NotImplementedError("Listing items is not implemented.")
  
  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    # pengecekan dilakukan pada item models, dan kita akan bekerja dengan ItemModel object (bukan dictionary seperti sebelumnya)
    # kita mulai dengan ItemModel dan kita akan meneruskan data yang kita terima dalam post method dengan dua tanda bintang (two asterisks), ini untuk mengubah dictionary menjadi keyword arguments
    # dan ketika kita membuat Class ItemModel, semua kolom dapat dipassing sebagai keyword arguments, mereka diperlukan kecuali kolom yang memiliki default argument. contohnya seperti kolom "id" kita tidak perlu memasukkan nilai karena akan otomatis dibuat oleh database. Sedangkan 3 kolom lainnya tidak memilki nilai default, jadi kita 3 kolom tersebut akan dipassing pada **item_data. jadi "**item_data" akan menyertakan name, price, store_id
    item = ItemModel(**item_data)

    # Jadi ketika kita membuat ItemModel yang tidak menyimpan ke database, dan tidak memeriksa unique column tertentu, kita harus benar benar menaruhnya dalama database agar hal itu terjadi
    # jadi ketika kita membuat ItemModel colum ID tidak aakan diberi nilai samapai kita menyimpannya ke dalam database 

    # beginilah cara menambahkan sesuatu ke dalam database, kita add lalu kita commit
    # jika tidak terjadi error, file data.db akan memikili infromasi tambahan (data)
    try:
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred inserting the item.")

    return item