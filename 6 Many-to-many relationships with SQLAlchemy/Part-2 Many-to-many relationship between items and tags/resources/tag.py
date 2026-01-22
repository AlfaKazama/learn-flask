from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import TagModel, StoreModel, ItemModel
from schemas import TagSchema, TagAndItemSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/store/<string:store_id>/tag")
class TagsInStore(MethodView):
  ## get akan memberi kita list of tags registered under the store
  @blp.response(200, TagSchema(many=True))
  def get(self, store_id):
    store = StoreModel.query.get_or_404(store_id)
    return store.tags.all()

  @blp.arguments(TagSchema)
  @blp.response(201, TagSchema)
  def post(self, tag_data, store_id):
    # # Ini akan memberi tahu apakah ada tag lain yang memiliki store id yang sama dan nama tag yang sama, lalu kita akan membatalkannya, ini terpakai jika pada TagModel kita tidak memakai unique pada column name.
    # if TagModel.query.filter(TagModel.store_id == store_id, TagModel.name == tag_data["name"]).first():
    #   abort(400, message="A tag with that name already exist in that store.")
    tag = TagModel(**tag_data, store_id=store_id)

    try:
      db.session.add(tag)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(
        500,
        message=str(e)
      )
    
    return tag
  

## Mendapatkan tag berdasarkan id nya
@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
  @blp.response(200, TagSchema)
  def get(self, tag_id):
    tag = TagModel.query.get_or_404(tag_id)
    return tag
  


## Kita menambahkan kelas lain untuk linking (menautkan) tags ke item, atau unliking (menghapus) tautan tag dari item

# ini akan mengambil item_id dan tag_id, dan yang akan dilakukan adalah menambahkan baris ke table "items_tags" saat kita link item ke tag.
# atau menghapus baris pada tabel "item_tags" saat kita ingin unlink item dari tag
@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
  @blp.response(201, TagSchema)
  ## linking tag to item
  def post(self, item_id, tag_id):

    # memastikan item dan tag ada, jika tidak ada akan 404
    item = ItemModel.query.get_or_404(item_id)
    tag = TagModel.query.get_or_404(tag_id)

    # dan jika ada maka:
    # kita akan bekerja dengan tabel sekunder tersebut dengan SQLAlchemy
    # kita memperlakukan item.tags sebagai "list" dan secara otomatis ItemModel akan memperhatikan perubahan yang dibutuhkan
    item.tags.append(tag)

    # jika kesalahan tidka terjadi kita akan mereturn "tag"
    try :
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred while inserting the tag.")
      
    return tag
  
  ## unliking tag from item
  # ini akan mirip dengan yang kita lakukan pada linking
  @blp.response(200, TagAndItemSchema)
  def delete(self, item_id, tag_id):
    item = ItemModel.query.get_or_404(item_id)
    tag = TagModel.query.get_or_404(tag_id)

    item.tags.remove(tag)

    try:
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred while inserting the tag.")
    
    return {"message": "Item removed from tag", "itemm": item, "tag": tag}



@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
  ## Mengambil informasi tentang tag tertentu
  blp.response(200, TagSchema)
  def get(self, tag_id):
    tag = TagModel.query.get_or_404(tag_id)
    return tag
  
  ## Menghapus tag
  # perhatikan banyak decorator yang digunakan
  @blp.response(
    202,
    description="Deletes a tag if no item is tagged with it.",
    example={"message": "Tag deleted."}
  )
  @blp.alt_response(404, description="Tag not found")
  @blp.alt_response(
    400,
    description="Returned if the tag is assigned to one or more items. In this case, the tag is not deleted."
  )
  def delete(self, tag_id):
    tag = TagModel.query.get_or_404(tag_id)

    if not tag.items:
      db.session.delete(tag)
      db.session.commit()
      return {"message": "Tag deleted."}
    abort(
      400,
      message="Could not delete tag. Make sure tag is not associated with any items, then try again."
    )