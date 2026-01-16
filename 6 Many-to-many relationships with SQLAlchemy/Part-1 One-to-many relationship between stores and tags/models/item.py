from db import db

# ini akan menjadi mapping antara baris dalam tabel (row in table) ke class python
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    # Sesuatu yang harus dicatat pada titik ini, SQLite tidak menerepakan batasan foreign keys, kita akan sadar saat menguji API. 
    # Kita dapat membaut ItemModel yang memiliki store id yang tidak terkait dengan table stores
    # Ini tidak maslaahh di SQLite, namun tidak di Postgres. Ini manfaat SQLite untuk pengujian, tapi ini juga dapat menggigit kita.
    # Kita harus ingat saat kita menggunakan Postgres kita tidak dapat membuat ItemModel hingga kita membuat store yang akan dikaitkan denganya
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="items")