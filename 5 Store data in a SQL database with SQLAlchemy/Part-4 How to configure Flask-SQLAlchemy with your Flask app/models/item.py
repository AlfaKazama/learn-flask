from db import db

# ini akan menjadi mapping antara baris dalam tabel (row in table) ke class python
class ItemModel(db.Model):
  __tablename__ = "items"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False) 
  price = db.Column(db.Float(precision=2), unique=False, nullable=False)

  # One many relationship, Setiap item memiliki satu store yang terkait dengannnya, tetapi setiap store dapat memiliki banyak item yang terkait dengannya.
  # Contoh: jika kita membuat lima item dan semuanya memiliki value store_id yang sama, tetapi satu store memilki lima item
  # Sekarang kita dapat memberi tahu SQLAlchemy, yang akan memberi tahu SQL database kita, bahwa store_id adalah "foreign key". Yang brarti mapping dari table ke table lain
  # dengan menggunakan foreignkey kita tidak bisa membuat item yang memiliki nilai store_id yang sama dalam stores table
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
  store = db.relationship("StoreModel", back_populates="items")