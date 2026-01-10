from db import db


# ini terlihat identik seperti yang kita lakukna pada item.py
# mulai dari import, lalu kita membuat class StoreModel yang inherit (mewarisi) db.Model, tentukan nama table   

class StoreModel(db.Model):
  __tablename__ = "stores"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  # items back_populates ke store dan store back_populates ke items
  # lazy="dynamic" berati bahwa items disini tidak akan diambil dari database hingga kita memerintahkannya
  items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
  