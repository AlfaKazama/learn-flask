from db import db


# ini terlihat identik seperti yang kita lakukna pada item.py
# mulai dari import, lalu kita membuat class StoreModel yang inherit (mewarisi) db.Model, tentukan nama table   

class StoreModel(db.Model):
  __tablename__ = "stores"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)

  # Ketika kita menghapus store, semua item yang terkait dengan store harus juga dihapus. Karena asumsinya item tersebut berada di store, jadi kalau store tutup/terhapus, semua item juga akan terhapus
  # untuk melakukan ini kita akan menggunakan "CASCADE"
  # dengan mneggunkan cascade ini brarti kita akan menghapus store dan item yang terkait akan terhapus
  items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
  