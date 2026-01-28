from db import db


## Kita membuat tag model dengan nama table "tags" yang memiliki column id, name, store_id, store

class TagModel(db.Model):
  __tablename__ = "tags"


  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

  store = db.relationship("StoreModel", back_populates="tags")
  
  # menambhakan ini untuk menghubungkan satu dengan yang lain dan kita perlu menambahkan secondary
  # secondary ini merujuk pada table secondary yang kita buat yaitu table "items_tags"
  items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")